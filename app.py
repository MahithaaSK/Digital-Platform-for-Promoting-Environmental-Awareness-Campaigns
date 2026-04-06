from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Article, Campaign, Participation, Interaction, ArticleComment, CampaignComment, Message
from sqlalchemy import desc, or_, and_
import random
import os
from dotenv import load_dotenv
import json
from difflib import SequenceMatcher

try:
    import google.generativeai as genai
    GENAI_IMPORT_ERROR = None
except Exception as e:
    genai = None
    GENAI_IMPORT_ERROR = e

# Load environment variables
load_dotenv()

# Flask & Database Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Support PostgreSQL in production, SQLite in development
database_url = os.getenv('DATABASE_URL')
if database_url:
    # Fix for SQLAlchemy 2.0+ PostgreSQL URI format
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecoaware.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY and genai is not None:
    genai.configure(api_key=GEMINI_API_KEY)
    # Use currently supported Gemini model names for v1beta.
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
    except Exception:
        model = genai.GenerativeModel('gemini-flash-latest')
    AURA_SYSTEM_PROMPT = """You are Aura, an AI-powered Smart Health Surveillance and Early Warning Assistant.
Your purpose is to help detect, monitor, and prevent outbreaks of water-borne diseases in rural and tribal communities.

Core Responsibilities:
1. Collect and analyze health reports (symptoms like diarrhea, fever, vomiting, jaundice) from ASHA workers, clinics, and volunteers.
2. Accept water quality readings (pH, turbidity, bacterial presence, TDS, etc.) from IoT sensors or manual test kits.
3. Use AI reasoning to detect unusual symptom clusters or unsafe water conditions and predict outbreak risks (low, medium, high).
4. Provide real-time alerts to health officials and community leaders when outbreak risk is detected.
5. Generate multilingual awareness tips for villagers on hygiene, safe water practices, and disease prevention.
6. Answer officials' queries with summarized insights (hotspots, number of cases, villages at risk, recommended interventions).
7. Communicate with ASHA workers in simple and clear instructions, confirming data received and next actions.
8. Be able to switch tone:
- For Officials: formal, concise, with data insights.
- For ASHA/Community: simple, supportive, and motivational.

Interaction Rules:
- Always prioritize accuracy and clarity in health-related advice.
- If outbreak risk is high, immediately warn: High risk detected in [village]. Notify officials now.
- If only preventive education is needed, provide practical hygiene tips.
- Keep answers short and direct unless asked for detailed explanation.
- If input is unclear, ask for clarification instead of guessing.
- Respect privacy: never share personal data unless explicitly asked by an official user.

You are the digital health guardian for rural communities."""
    aura_generation_config = {
        "temperature": 0.9,
        "top_p": 0.9,
        "max_output_tokens": 4096,
    }
    aura_model = genai.GenerativeModel(
        model_name='gemini-2.0-flash',
        generation_config=aura_generation_config
    )
else:
    model = None
    aura_model = None
    AURA_SYSTEM_PROMPT = ""
    if GENAI_IMPORT_ERROR:
        print(f"⚠️  Warning: google.generativeai import failed ({GENAI_IMPORT_ERROR}). AI recommendations will be limited.")
    elif not GEMINI_API_KEY:
        print("⚠️  Warning: GEMINI_API_KEY not found. AI recommendations will be limited.")

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# -------------------------------------------------------
# Context processor — inject unread count into all templates
# -------------------------------------------------------
@app.context_processor
def inject_unread():
    if current_user.is_authenticated:
        return dict(unread_count=current_user.unread_message_count())
    return dict(unread_count=0)

# -------------------------------------------------------
# AI Recommendation Engine
# -------------------------------------------------------
def get_recommendations(user):
    interactions = Interaction.query.filter_by(user_id=user.id).all()
    participations = Participation.query.filter_by(user_id=user.id).all()
    
    categories_freq = {}
    for inter in interactions:
        if inter.article:
            cat = inter.article.category
            categories_freq[cat] = categories_freq.get(cat, 0) + 1
    for part in participations:
        if part.campaign:
            cat = part.campaign.category
            categories_freq[cat] = categories_freq.get(cat, 0) + 2

    sorted_categories = sorted(categories_freq.keys(), key=lambda k: categories_freq[k], reverse=True)
    viewed_ids = [i.article_id for i in interactions]
    joined_ids = [p.campaign_id for p in participations]
    
    rec_articles, rec_campaigns = [], []
    if sorted_categories:
        top = sorted_categories[0]
        af = [Article.category == top]
        if viewed_ids: af.append(~Article.id.in_(viewed_ids))
        rec_articles = Article.query.filter(*af).limit(3).all()
        
        cf = [Campaign.category == top]
        if joined_ids: cf.append(~Campaign.id.in_(joined_ids))
        rec_campaigns = Campaign.query.filter(*cf).limit(2).all()

    if len(rec_articles) < 3:
        fallback = Article.query.filter(~Article.id.in_(viewed_ids + [a.id for a in rec_articles])).limit(3 - len(rec_articles)).all()
        rec_articles.extend(fallback)
    if len(rec_campaigns) < 2:
        fallback = Campaign.query.filter(~Campaign.id.in_(joined_ids + [c.id for c in rec_campaigns])).limit(2 - len(rec_campaigns)).all()
        rec_campaigns.extend(fallback)
        
    return rec_articles, rec_campaigns

def get_ai_post_suggestions(user):
    """Get AI-powered content suggestions using Gemini API"""
    interactions = Interaction.query.filter_by(user_id=user.id).all()
    participations = Participation.query.filter_by(user_id=user.id).all()
    
    categories_freq = {}
    for inter in interactions:
        if inter.article:
            categories_freq[inter.article.category] = categories_freq.get(inter.article.category, 0) + 1
    for part in participations:
        if part.campaign:
            categories_freq[part.campaign.category] = categories_freq.get(part.campaign.category, 0) + 2
    
    # Use Gemini to generate personalized suggestions
    if model and categories_freq:
        sorted_cats = sorted(categories_freq, key=lambda k: categories_freq[k], reverse=True)
        user_interests = ", ".join(sorted_cats[:3])
        
        try:
            prompt = f"""Based on user interests in {user_interests}, generate 4 engaging blog post ideas for an environmental awareness platform called 'EcoAware'. 
            Each idea should be a catchy, thought-provoking title that would encourage users to read and engage with environmental content.
            Format: Return only the 4 titles, one per line, without numbering."""
            
            response = model.generate_content(prompt)
            suggestions = [s.strip() for s in response.text.split('\n') if s.strip()]
            return suggestions[:4] if suggestions else get_fallback_suggestions()
        except Exception as e:
            print(f"Gemini API error: {e}")
            return get_fallback_suggestions()
    
    return get_fallback_suggestions()

def get_fallback_suggestions():
    """Fallback suggestions when Gemini API is unavailable"""
    all_suggestions = {
        "Climate Change": [
            "Why your city needs a climate action plan",
            "How to calculate your home's carbon footprint",
            "5 everyday habits that hurt the climate most",
            "The hidden carbon cost of streaming services",
        ],
        "Recycling": [
            "The truth about plastic recycling in your city",
            "How to set up a zero-waste kitchen",
            "Upcycling ideas for common household waste",
            "Why wishcycling harms more than it helps",
        ],
        "Renewable Energy": [
            "Is solar power right for your home?",
            "How community wind projects work",
            "The pros and cons of hydroelectric power",
            "Understanding your green energy tariff",
        ],
        "Conservation": [
            "Plants that support pollinators in your garden",
            "How to build a hedgehog highway in your fence",
            "The best nature reserves near cities to visit",
            "Why old-growth forests cannot be replaced",
        ],
        "Pollution Control": [
            "How air quality affects your sleep and health",
            "The invisible pollution in your drinking water",
            "Noise pollution: the overlooked environmental threat",
            "5 ways to reduce indoor air pollution",
        ],
    }
    
    all_flat = [s for lst in all_suggestions.values() for s in lst]
    return random.sample(all_flat, 4)


def _get_user_interest_categories(user):
    """Rank categories based on user behavior to personalize suggestions."""
    interactions = Interaction.query.filter_by(user_id=user.id).all()
    participations = Participation.query.filter_by(user_id=user.id).all()
    own_articles = Article.query.filter_by(author_id=user.id).all()
    own_campaigns = Campaign.query.filter_by(author_id=user.id).all()

    scores = {}

    for inter in interactions:
        if inter.article:
            cat = inter.article.category
            scores[cat] = scores.get(cat, 0) + 1

    for part in participations:
        if part.campaign:
            cat = part.campaign.category
            scores[cat] = scores.get(cat, 0) + 2

    for a in own_articles:
        scores[a.category] = scores.get(a.category, 0) + 3

    for c in own_campaigns:
        scores[c.category] = scores.get(c.category, 0) + 3

    ranked = [k for k, _ in sorted(scores.items(), key=lambda x: x[1], reverse=True)]
    return ranked


def _is_environment_question(text):
    """Simple keyword gate so Aura only handles environmental topics."""
    if not text:
        return False
    lower = text.lower()
    keywords = [
        'environment', 'climate', 'global warming', 'recycling', 'renewable', 'solar', 'wind', 'conservation',
        'pollution', 'plastic', 'waste', 'compost', 'greenhouse', 'carbon', 'biodiversity', 'wildlife',
        'forest', 'river', 'ocean', 'water quality', 'sustainability', 'eco', 'campaign', 'article',
        'clean energy', 'air quality', 'emission', 'tree', 'nature', 'habitat'
    ]
    return any(k in lower for k in keywords)


def _format_recommendation_block(user):
    """Create a deterministic recommendation block from DB content."""
    rec_articles, rec_campaigns = get_recommendations(user)

    article_lines = []
    for a in rec_articles[:3]:
        article_lines.append(f"- {a.title} ({a.category})")

    campaign_lines = []
    for c in rec_campaigns[:3]:
        campaign_lines.append(f"- {c.title} ({c.category}) on {c.date} at {c.location}")

    parts = ["\n\nSuggested for you from EcoAware:"]
    if campaign_lines:
        parts.append("Campaigns:\n" + "\n".join(campaign_lines))
    if article_lines:
        parts.append("Articles:\n" + "\n".join(article_lines))
    return "\n".join(parts)

# -------------------------------------------------------
# Auth Routes
# -------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists. Please login.', 'warning')
            return redirect(url_for('register'))
        
        photo = f"https://ui-avatars.com/api/?name={name.replace(' ', '+')}&background=random&color=fff&size=128"
        new_user = User(name=name, email=email, password_hash=generate_password_hash(password), profile_photo=photo)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Please check your login details and try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# -------------------------------------------------------
# Dashboard
# -------------------------------------------------------
@app.route('/dashboard')
@login_required
def dashboard():
    rec_articles, rec_campaigns = get_recommendations(current_user)
    ai_suggestions = get_ai_post_suggestions(current_user)
    
    # Event Calendar — campaigns user has joined, sorted by date
    participations = Participation.query.filter_by(user_id=current_user.id).all()
    upcoming_events = sorted([p.campaign for p in participations if p.campaign], key=lambda x: x.date)
    
    # Posts feed — articles from people the user follows, plus own articles
    followed_ids = [u.id for u in current_user.followed.all()] + [current_user.id]
    posts_feed = Article.query.filter(Article.author_id.in_(followed_ids)).order_by(desc(Article.created_at)).limit(10).all()
    
    # People you may know — users not already followed, excluding self
    already_followed_ids = set(followed_ids)
    suggested_people = User.query.filter(~User.id.in_(already_followed_ids)).limit(6).all()
    
    # User's own articles and campaigns
    my_articles = Article.query.filter_by(author_id=current_user.id).order_by(desc(Article.created_at)).all()
    my_campaigns = Campaign.query.filter_by(author_id=current_user.id).order_by(desc(Campaign.created_at)).all()
    
    # Campaigns user joined (not authored)
    joined_campaign_ids = [p.campaign_id for p in participations]
    
    return render_template('dashboard.html',
                           rec_articles=rec_articles,
                           rec_campaigns=rec_campaigns,
                           upcoming_events=upcoming_events,
                           posts_feed=posts_feed,
                           suggested_people=suggested_people,
                           ai_suggestions=ai_suggestions,
                           my_articles=my_articles,
                           my_campaigns=my_campaigns,
                           joined_campaign_ids=joined_campaign_ids)

# -------------------------------------------------------
# Content Creation (User)
# -------------------------------------------------------
@app.route('/user/create_article', methods=['POST'])
@login_required
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')
    article = Article(title=title, content=content, category=category, author_id=current_user.id)
    db.session.add(article)
    db.session.commit()
    flash('Article published!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/user/create_campaign', methods=['POST'])
@login_required
def create_campaign():
    title = request.form.get('title')
    description = request.form.get('description')
    category = request.form.get('category')
    date = request.form.get('date')
    location = request.form.get('location')
    campaign = Campaign(title=title, description=description, category=category, date=date, location=location, author_id=current_user.id)
    db.session.add(campaign)
    db.session.commit()
    participation = Participation(user_id=current_user.id, campaign_id=campaign.id)
    db.session.add(participation)
    db.session.commit()
    flash('Campaign created and added to your calendar!', 'success')
    return redirect(url_for('dashboard'))

# -------------------------------------------------------
# Social — Follow / Unfollow
# -------------------------------------------------------
@app.route('/follow/<int:user_id>', methods=['POST'])
@login_required
def follow(user_id):
    user = db.session.get(User, user_id)
    if not user or user == current_user:
        flash("Can't follow that user.", "warning")
        return redirect(request.referrer or url_for('dashboard'))
    current_user.follow(user)
    db.session.commit()
    flash(f'Now following {user.name}!', 'success')
    return redirect(request.referrer or url_for('dashboard'))

@app.route('/unfollow/<int:user_id>', methods=['POST'])
@login_required
def unfollow(user_id):
    user = db.session.get(User, user_id)
    if user:
        current_user.unfollow(user)
        db.session.commit()
        flash(f'Unfollowed {user.name}.', 'info')
    return redirect(request.referrer or url_for('dashboard'))

# -------------------------------------------------------
# People Directory
# -------------------------------------------------------
@app.route('/people')
@login_required
def people():
    all_users = User.query.filter(User.id != current_user.id).all()
    return render_template('people.html', all_users=all_users)

# -------------------------------------------------------
# Profile Page
# -------------------------------------------------------
@app.route('/profile/<int:user_id>')
@login_required
def view_profile(user_id):
    user = db.session.get(User, user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('dashboard'))
    user_articles = Article.query.filter_by(author_id=user_id).order_by(desc(Article.created_at)).all()
    user_campaigns = Campaign.query.filter_by(author_id=user_id).order_by(desc(Campaign.created_at)).all()
    return render_template('profile.html', user=user, user_articles=user_articles, user_campaigns=user_campaigns)

# -------------------------------------------------------
# Articles
# -------------------------------------------------------
@app.route('/articles')
def articles():
    category = request.args.get('category', '')
    query = Article.query
    if category:
        query = query.filter_by(category=category)
    all_articles = query.order_by(desc(Article.created_at)).all()
    categories = ['Climate Change', 'Recycling', 'Renewable Energy', 'Conservation', 'Pollution Control']
    return render_template('articles.html', articles=all_articles, categories=categories, selected=category)

@app.route('/article/<int:article_id>')
def view_article(article_id):
    article = Article.query.get_or_404(article_id)
    if current_user.is_authenticated:
        existing = Interaction.query.filter_by(user_id=current_user.id, article_id=article_id).first()
        if not existing:
            db.session.add(Interaction(user_id=current_user.id, article_id=article_id))
            db.session.commit()
    # Related articles same category
    related = Article.query.filter(Article.category == article.category, Article.id != article.id).limit(3).all()
    # Similar posts - by engagement/likes
    similar = Article.query.filter(Article.category == article.category, Article.id != article.id).order_by(desc(Article.likes)).limit(5).all()
    return render_template('view_article.html', article=article, related=related, similar=similar)

# -------------------------------------------------------
# Article Like & Comments
# -------------------------------------------------------
@app.route('/article/<int:article_id>/like', methods=['POST'])
@login_required
def like_article(article_id):
    article = Article.query.get_or_404(article_id)
    article.likes = (article.likes or 0) + 1
    db.session.commit()
    return redirect(url_for('view_article', article_id=article_id))

@app.route('/article/<int:article_id>/comment', methods=['POST'])
@login_required
def comment_article(article_id):
    body = request.form.get('body', '').strip()
    if body:
        comment = ArticleComment(body=body, article_id=article_id, author_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added!', 'success')
    return redirect(url_for('view_article', article_id=article_id))

@app.route('/article/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_article_comment(comment_id):
    comment = ArticleComment.query.get_or_404(comment_id)
    article_id = comment.article_id
    if comment.author_id == current_user.id or current_user.role == 'admin':
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted.', 'info')
    return redirect(url_for('view_article', article_id=article_id))

# -------------------------------------------------------
# Campaigns
# -------------------------------------------------------
@app.route('/campaigns')
def campaigns():
    category = request.args.get('category', '')
    query = Campaign.query
    if category:
        query = query.filter_by(category=category)
    all_campaigns = query.order_by(desc(Campaign.created_at)).all()
    participated_ids = []
    if current_user.is_authenticated:
        participated_ids = [p.campaign_id for p in Participation.query.filter_by(user_id=current_user.id).all()]
    categories = ['Climate Change', 'Recycling', 'Renewable Energy', 'Conservation', 'Pollution Control']
    return render_template('campaigns.html', campaigns=all_campaigns, participated_ids=participated_ids,
                           categories=categories, selected=category)

@app.route('/campaign/<int:campaign_id>')
def view_campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    participated_ids = []
    if current_user.is_authenticated:
        participated_ids = [p.campaign_id for p in Participation.query.filter_by(user_id=current_user.id).all()]
    participant_count = Participation.query.filter_by(campaign_id=campaign_id).count()
    return render_template('view_campaign.html', campaign=campaign,
                           participated_ids=participated_ids, participant_count=participant_count)

@app.route('/participate/<int:campaign_id>', methods=['POST'])
@login_required
def participate(campaign_id):
    campaign = db.session.get(Campaign, campaign_id)
    if not campaign:
        return redirect(url_for('campaigns'))
    existing = Participation.query.filter_by(user_id=current_user.id, campaign_id=campaign_id).first()
    if not existing:
        db.session.add(Participation(user_id=current_user.id, campaign_id=campaign_id))
        db.session.commit()
        flash(f'Joined "{campaign.title}"! Added to your calendar.', 'success')
    return redirect(request.referrer or url_for('campaigns'))

# -------------------------------------------------------
# Campaign Comments
# -------------------------------------------------------
@app.route('/campaign/<int:campaign_id>/comment', methods=['POST'])
@login_required
def comment_campaign(campaign_id):
    body = request.form.get('body', '').strip()
    if body:
        comment = CampaignComment(body=body, campaign_id=campaign_id, author_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added!', 'success')
    return redirect(url_for('view_campaign', campaign_id=campaign_id))

@app.route('/campaign/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_campaign_comment(comment_id):
    comment = CampaignComment.query.get_or_404(comment_id)
    campaign_id = comment.campaign_id
    if comment.author_id == current_user.id or current_user.role == 'admin':
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted.', 'info')
    return redirect(url_for('view_campaign', campaign_id=campaign_id))

# -------------------------------------------------------
# Messaging
# -------------------------------------------------------
@app.route('/messages')
@login_required
def messages():
    # Get all conversation partners
    sent = db.session.query(Message.receiver_id).filter_by(sender_id=current_user.id).distinct()
    received = db.session.query(Message.sender_id).filter_by(receiver_id=current_user.id).distinct()
    partner_ids = set([r[0] for r in sent] + [r[0] for r in received])
    partners = User.query.filter(User.id.in_(partner_ids)).all()
    return render_template('messages.html', partners=partners, selected_user=None, conversation=[])

@app.route('/messages/<int:user_id>', methods=['GET', 'POST'])
@login_required
def conversation(user_id):
    other = db.session.get(User, user_id)
    if not other:
        flash('User not found.', 'danger')
        return redirect(url_for('messages'))

    if request.method == 'POST':
        body = request.form.get('body', '').strip()
        if body:
            msg = Message(body=body, sender_id=current_user.id, receiver_id=user_id)
            db.session.add(msg)
            db.session.commit()
        return redirect(url_for('conversation', user_id=user_id))

    # Mark received messages as read
    Message.query.filter_by(sender_id=user_id, receiver_id=current_user.id, is_read=False).update({'is_read': True})
    db.session.commit()

    conv = Message.query.filter(
        or_(
            and_(Message.sender_id == current_user.id, Message.receiver_id == user_id),
            and_(Message.sender_id == user_id, Message.receiver_id == current_user.id)
        )
    ).order_by(Message.created_at).all()

    sent = db.session.query(Message.receiver_id).filter_by(sender_id=current_user.id).distinct()
    received = db.session.query(Message.sender_id).filter_by(receiver_id=current_user.id).distinct()
    partner_ids = set([r[0] for r in sent] + [r[0] for r in received])
    partners = User.query.filter(User.id.in_(partner_ids)).all()

    return render_template('messages.html', partners=partners, selected_user=other, conversation=conv)

# -------------------------------------------------------
# Aura Assistant (Voice + Chat)
# -------------------------------------------------------

# Load dummy Q&A data from JSON file
def load_dummy_qa_data():
    """Load pre-built Q&A data from JSON file"""
    try:
        qa_file = os.path.join(os.path.dirname(__file__), 'dummy_qa_data.json')
        if os.path.exists(qa_file):
            with open(qa_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading dummy QA data: {e}")
    return []

def find_matching_qa(user_question, qa_data):
    """Find a matching Q&A from the dummy data based on similarity"""
    if not qa_data or not user_question:
        return None
    
    user_question_lower = user_question.lower()
    best_match = None
    best_ratio = 0
    threshold = 0.5  # Minimum similarity threshold
    
    for qa_pair in qa_data:
        question = qa_pair.get('question', '').lower()
        # Calculate similarity ratio
        ratio = SequenceMatcher(None, user_question_lower, question).ratio()
        
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = qa_pair
    
    # Return match if similarity is above threshold
    if best_ratio >= threshold:
        print(f"✓ Found matching Q&A (similarity: {best_ratio:.2%})")
        return best_match
    
    return None

@app.route('/assistant')
@login_required
def assistant():
    return render_template('assistant.html')

@app.route('/api/aura/chat', methods=['POST'])
@login_required
def aura_chat():
    data = request.get_json(silent=True) or {}
    message = (data.get('message') or '').strip()

    if not message:
        return jsonify({'error': 'Message is required.'}), 400

    # Aura is intentionally restricted to environmental awareness only.
    if not _is_environment_question(message):
        fallback_reply = (
            "I focus only on environmental awareness topics in EcoAware. "
            "Please ask about climate, recycling, conservation, pollution control, renewable energy, "
            "or request campaign/article suggestions."
        )
        return jsonify({'reply': fallback_reply + _format_recommendation_block(current_user)})

    # ✓ FIRST: Try to find matching answer in dummy Q&A data
    print(f"\n[AURA] Received question: {message}")
    print("[AURA] Checking dummy Q&A database...")
    
    qa_data = load_dummy_qa_data()
    matching_qa = find_matching_qa(message, qa_data)
    
    if matching_qa:
        print(f"✓ Using pre-built response from dummy_qa_data.json")
        reply = matching_qa.get('response', '')
        reply = reply + _format_recommendation_block(current_user)
        return jsonify({'reply': reply})
    
    print("[AURA] No matching Q&A found, falling back to Gemini API...")
    
    # FALLBACK: Use Gemini API if no match found in dummy data
    interests = _get_user_interest_categories(current_user)
    interest_text = ', '.join(interests[:5]) if interests else 'No strong preference detected yet'

    campaigns = Campaign.query.order_by(desc(Campaign.created_at)).limit(25).all()
    articles = Article.query.order_by(desc(Article.created_at)).limit(25).all()

    campaign_context = "\n".join(
        [f"- {c.title} | {c.category} | {c.date} | {c.location}" for c in campaigns]
    )
    article_context = "\n".join(
        [f"- {a.title} | {a.category}" for a in articles]
    )

    if not aura_model:
        offline_reply = (
            "Aura AI is currently offline, but I can still guide you with environmental awareness and "
            "recommend content from this platform."
        )
        return jsonify({'reply': offline_reply + _format_recommendation_block(current_user)})

    try:
        prompt = (
            f"{AURA_SYSTEM_PROMPT}\n\n"
            "You must obey these strict rules:\n"
            "1) Answer only environmental awareness related questions.\n"
            "2) If user asks non-environment topic, politely refuse and redirect to environmental topics.\n"
            "3) When suggesting campaigns or articles, use only items from the provided EcoAware database context.\n"
            "4) Personalize suggestions using the user's preferences.\n\n"
            f"User preference categories: {interest_text}\n\n"
            "EcoAware campaigns:\n"
            f"{campaign_context}\n\n"
            "EcoAware articles:\n"
            f"{article_context}\n\n"
            "Keep response concise and actionable.\n\n"
            f"User input:\n{message}\n\n"
            "Aura response:"
        )
        response = aura_model.generate_content(prompt)
        reply = (response.text or '').strip()
        if not reply:
            reply = 'I could not generate a response. Please try again.'
        reply = reply + _format_recommendation_block(current_user)
        return jsonify({'reply': reply})
    except Exception as e:
        print(f"Aura response error: {e}")
        fallback_reply = (
            "Aura service is temporarily unavailable. I can still help with environmental awareness and "
            "platform recommendations."
        )
        return jsonify({'reply': fallback_reply + _format_recommendation_block(current_user)})

# -------------------------------------------------------
# Admin
# -------------------------------------------------------
@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('dashboard'))
    all_articles = Article.query.order_by(desc(Article.created_at)).all()
    all_campaigns = Campaign.query.order_by(desc(Campaign.created_at)).all()
    return render_template('admin_dashboard.html', articles=all_articles, campaigns=all_campaigns)

# -------------------------------------------------------
# AI Content Suggestions API
# -------------------------------------------------------
@app.route('/api/ai-content-suggestion', methods=['POST'])
@login_required
def ai_content_suggestion():
    """Generate AI content suggestions for articles or campaigns"""
    if not model:
        data = request.json or {}
        content_type = data.get('type')
        entity_type = data.get('entity_type')
        category = data.get('category', 'Environment')
        if content_type == 'title':
            if entity_type == 'campaign':
                return {'suggestions': [f'{category} Action Drive', f'Community {category} Mission', f'{category} Awareness Campaign'], 'type': 'title'}
            return {'suggestions': [f'Why {category} Matters Now', f'Practical Guide to {category}', f'Common Myths About {category}'], 'type': 'title'}
        if content_type == 'description':
            if entity_type == 'campaign':
                return {'suggestions': f'Join our {category} campaign to create measurable local impact through community action and awareness.', 'type': 'description'}
            return {'suggestions': f'This article explores key challenges and practical solutions in {category}, with clear steps readers can apply today.', 'type': 'description'}
        return {'error': 'Invalid content type'}, 400
    
    data = request.json
    content_type = data.get('type')  # 'title', 'description'
    category = data.get('category', '')
    current_text = data.get('current_text', '')
    
    try:
        if content_type == 'title':
            if data.get('entity_type') == 'campaign':
                prompt = f"Generate 3 creative and catchy campaign titles for a {category} environmental initiative. Return only the titles, one per line."
            else:
                prompt = f"Generate 3 engaging blog post titles about {category}. Make them thought-provoking and shareable. Return only the titles, one per line."
        
        elif content_type == 'description':
            if data.get('entity_type') == 'campaign':
                prompt = f"Write a compelling 2-3 sentence description for an environmental campaign about {category}. Make it inspiring and actionable."
            else:
                prompt = f"Write a compelling introduction (2-3 sentences) for an environmental article about {category}."
        
        else:
            return {'error': 'Invalid content type'}, 400
        
        response = model.generate_content(prompt)
        return {
            'suggestions': response.text.strip().split('\n') if content_type == 'title' else response.text.strip(),
            'type': content_type
        }
    except Exception as e:
        print(f"Gemini API error: {e}")
        entity_type = data.get('entity_type')
        if content_type == 'title':
            if entity_type == 'campaign':
                return {'suggestions': [f'{category} Impact Week', f'Clean {category} Initiative', f'Local {category} Volunteer Sprint'], 'type': 'title'}
            return {'suggestions': [f'Understanding {category} in 2026', f'Everyday Actions for {category}', f'How Communities Can Improve {category}'], 'type': 'title'}
        if content_type == 'description':
            if entity_type == 'campaign':
                return {'suggestions': f'This campaign invites residents to collaborate on {category} improvements with simple, practical actions and visible outcomes.', 'type': 'description'}
            return {'suggestions': f'Learn what drives {category} issues and discover realistic actions individuals and communities can take to improve outcomes.', 'type': 'description'}
        return {'error': 'AI generation failed'}, 500

# -------------------------------------------------------
# Similar Posts/Campaigns API
# -------------------------------------------------------
@app.route('/api/similar-articles/<int:article_id>')
def get_similar_articles(article_id):
    """Get articles similar to the current one"""
    article = Article.query.get_or_404(article_id)
    
    # Get articles in same category, sorted by engagement
    similar = Article.query.filter(
        Article.category == article.category,
        Article.id != article.id
    ).order_by(desc(Article.likes)).all()
    
    data = [{
        'id': a.id,
        'title': a.title,
        'category': a.category,
        'likes': a.likes or 0,
        'author': a.author.name if a.author else 'Unknown'
    } for a in similar[:5]]
    
    return jsonify(data)

@app.route('/admin/article/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    if current_user.role != 'admin': return redirect(url_for('dashboard'))
    article = db.session.get(Article, article_id)
    if article:
        db.session.delete(article)
        db.session.commit()
        flash('Article deleted.', 'info')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/campaign/delete/<int:campaign_id>', methods=['POST'])
@login_required
def delete_campaign(campaign_id):
    if current_user.role != 'admin': return redirect(url_for('dashboard'))
    campaign = db.session.get(Campaign, campaign_id)
    if campaign:
        db.session.delete(campaign)
        db.session.commit()
        flash('Campaign deleted.', 'info')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    if __name__ == '__main__':
        with app.app_context():
            db.create_all()
    
        # Production vs Development
        is_production = os.getenv('FLASK_ENV') == 'production'
        debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'
        port = int(os.getenv('PORT', 5000))
    
        app.run(
            debug=debug_mode and not is_production,
            host='0.0.0.0',
            port=port
        )
    if __name__ == '__main__':
        with app.app_context():
            db.create_all()
    
        # Production vs Development
        is_production = os.getenv('FLASK_ENV') == 'production'
        debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'
        port = int(os.getenv('PORT', 5000))
    
        app.run(
            debug=debug_mode and not is_production,
            host='0.0.0.0',
            port=port
        )
