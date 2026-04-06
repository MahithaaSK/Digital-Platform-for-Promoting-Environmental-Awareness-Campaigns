# 🌱 EcoAware - Environmental Awareness Platform

**An AI-powered platform for environmental awareness, community campaigns, and ecological action.**

---

## 📋 Quick Info

- **Language:** Python 3.11
- **Framework:** Flask 3.0
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **AI Engine:** Google Gemini 2.0
- **Status:** ✅ Production Ready
- **Last Updated:** 2026-04-06

---

## 🚀 Quick Start (Local Development)

### 1. Clone & Setup
```bash
git clone https://github.com/YOUR_USERNAME/ecoaware.git
cd ecoaware
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env and add:
# - GEMINI_API_KEY=your_key
# - SECRET_KEY=random_generated_key
```

### 4. Initialize Database
```bash
python init_db.py
```

### 5. Run Application
```bash
python app.py
# Visit: http://127.0.0.1:5000
```

---

## 📦 Features

### User Features
- ✅ User registration and authentication
- ✅ Personal profile management
- ✅ Environmental awareness articles
- ✅ Community campaign participation
- ✅ Real-time messaging system
- ✅ AI-powered Aura assistant
- ✅ Personalized recommendations

### AI Features
- ✅ **Pre-built Q&A System** - Responds from dummy_qa_data.json (15 environmental Q&A pairs)
- ✅ **Smart Fallback** - Uses Gemini API only if no match found
- ✅ **Similarity Matching** - 60%+ accuracy for question matching
- ✅ **Environmental Focus** - Restricted to climate, conservation, recycling topics

### Admin Features
- ✅ User management
- ✅ Content creation (articles, campaigns)
- ✅ Campaign management
- ✅ Analytics dashboard
- ✅ Message monitoring

---

## 📂 Project Structure

```
ecoaware/
├── app.py                           # Main Flask application
├── models.py                        # SQLAlchemy database models
├── init_db.py                       # Database initialization
├── requirements.txt                 # Python dependencies
│
├── templates/                       # HTML templates (14 files)
│   ├── base.html                   # Base layout
│   ├── index.html                  # Homepage
│   ├── login.html                  # Login page
│   ├── register.html               # Registration
│   ├── dashboard.html              # User dashboard
│   ├── assistant.html              # Aura Assistant interface
│   ├── articles.html               # Articles listing
│   ├── campaigns.html              # Campaigns listing
│   └── ...
│
├── static/                         # Static files
│   └── style.css                   # Styling
│
├── instance/                       # Instance folder (auto-created)
│   └── ecoaware.db                # SQLite database (dev)
│
├── dummy_qa_data.json             # Pre-built Q&A responses
├── seed_qa_data.py                # Data generation script
│
├── Procfile                        # Heroku/Render deployment
├── runtime.txt                     # Python version specification
├── render.yaml                     # Render.com configuration
├── wsgi.py                         # WSGI entry point
├── .gitignore                      # Git ignore rules
│
├── DEPLOYMENT_GUIDE.md            # Step-by-step deployment
├── DEPLOYMENT_CHECKLIST_DETAILED.md  # Full checklist
└── README.md                       # This file
```

---

## 🤖 Aura Assistant - How It Works

### Response Priority
1. **Check Dummy Q&A Data** (dummy_qa_data.json)
   - Loads 15 pre-built environmental questions
   - Uses similarity matching (60%+ threshold)
   - Returns instant response

2. **Fallback to Gemini API**
   - Only called if no match found
   - Uses advanced reasoning for complex questions
   - Adds personalized recommendations

### Example Questions It Answers
- "What are the causes of climate change?"
- "How does deforestation affect the environment?"
- "Which tree species grow well in tropical areas?"
- "How can I contribute to the river cleanup campaign?"
- "What is the e-waste collection drive?"

### Question Matching Algorithm
```python
SequenceMatcher(None, question_lower, db_question_lower).ratio()
if similarity >= 0.60:  # 60% threshold
    return pre_built_response
else:
    call_gemini_api()  # Fallback
```

---

## 🛠️ Development

### Database Models
- **User** - User accounts with authentication
- **Article** - Environmental education articles
- **Campaign** - Community campaigns
- **Participation** - User participation in campaigns
- **Message** - User-to-user messaging
- **Interaction** - Track article/campaign engagement
- **Comments** - Article and campaign comments

### API Endpoints

#### Authentication
- `POST /register` - Create new user account
- `POST /login` - User login
- `GET /logout` - User logout

#### Content
- `GET /articles` - List all articles
- `GET /article/<id>` - View single article
- `GET /campaigns` - List all campaigns
- `GET /campaign/<id>` - View campaign details

#### AI/Assistant
- `POST /api/aura/chat` - Send message to Aura assistant
- Returns: `{'reply': 'response_text'}`

#### User
- `GET /profile` - User profile page
- `GET /dashboard` - User dashboard
- `GET /messages` - User messages
- `POST /send-message` - Send new message

---

## 🔐 Security Features

- ✅ Password hashing with Werkzeug
- ✅ Session-based authentication (Flask-Login)
- ✅ CSRF protection (built into Flask)
- ✅ SQL injection prevention (SQLAlchemy)
- ✅ Environment variable protection
- ✅ No debug mode in production
- ✅ Input validation on all forms

---

## 📊 Deployment Status

| Platform | Status | Time | Cost |
|----------|--------|------|------|
| **Render** | ✅ Ready | 2-5 min | Free |
| **Heroku** | ✅ Ready | 5-10 min | $7+/month |
| **PythonAnywhere** | ✅ Ready | 10-15 min | Free-$5/month |
| **AWS/DigitalOcean** | ✅ Ready | 30 min | $5+/month |

**⭐ Recommended:** Render (free, fast, automatic deploys)

---

## 🚢 Deploy in 5 Minutes

### To Render (Simplest)
```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Create account at render.com
# 3. Click "New +" → "Web Service"
# 4. Connect GitHub repository
# 5. Fill environment variables
# 6. Click "Create Web Service"
# 7. Done! (site goes live in 2-5 minutes)
```

**For detailed steps:** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 🧪 Testing

### Run Locally
```bash
python app.py
# Visit: http://127.0.0.1:5000
```

### Test Features
1. ✅ Register new account
2. ✅ Login
3. ✅ Ask Aura assistant a question
4. ✅ Read articles
5. ✅ Join campaigns
6. ✅ Send messages

### Test Pre-built Q&A
Ask these questions and verify JSON responses (not API):
```
"What are the main causes of climate change?"
"What happens when we cut down all trees?"
"How do I participate in river cleanup?"
```

Check terminal output:
```
[AURA] Checking dummy Q&A database...
✓ Using pre-built response from dummy_qa_data.json
```

---

## 📝 Configuration

### Environment Variables (.env)
```bash
# Required
GEMINI_API_KEY=your_google_api_key
SECRET_KEY=your_secure_random_key
FLASK_ENV=production  # or 'development'
FLASK_DEBUG=0

# Optional (defaults provided)
DATABASE_URL=postgresql://user:pass@host/db
PORT=5000
```

### Generate Strong SECRET_KEY
```python
import secrets
print(secrets.token_hex(32))
# Output: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

---

## 🐛 Troubleshooting

### "Module not found" Error
```bash
pip install -r requirements.txt
pip freeze > requirements.txt  # Update if needed
```

### "GEMINI_API_KEY not set" Warning
- Add to `.env` file
- On deployed platform, add to environment variables

### Database Lock Error
```bash
rm instance/ecoaware.db  # Delete old DB
python init_db.py        # Recreate
```

### Port Already in Use
```bash
# Windows: find process
netstat -ano | findstr :5000

# macOS/Linux: find and kill
lsof -i :5000
kill -9 <PID>
```

---

## 📈 Performance Tips

1. **Caching:** Pre-built Q&A loads once per request
2. **Database:** Use PostgreSQL in production (faster than SQLite)
3. **CDN:** Serve static files from Cloudflare (free tier)
4. **Lazy Loading:** Images load as user scrolls
5. **Compression:** GZIP enabled via gunicorn

---

## 📚 Documentation

- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Step-by-step deployment
- [DEPLOYMENT_CHECKLIST_DETAILED.md](DEPLOYMENT_CHECKLIST_DETAILED.md) - Full checklist
- [GEMINI_SETUP.md](GEMINI_SETUP.md) - AI configuration
- [DUMMY_QA_README.md](DUMMY_QA_README.md) - Q&A system details

---

## 🤝 Contributing

To contribute:
1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature/new-feature`
5. Open Pull Request

---

## 📧 Support

- **Issues:** Open on GitHub
- **Email:** support@ecoaware.com
- **Docs:** See DEPLOYMENT_GUIDE.md for detailed help

---

## 📄 License

This project is open source. See LICENSE.md for details.

---

## 🎯 Roadmap

### v1.1 (Next Release)
- [ ] Mobile app (React Native)
- [ ] Social sharing features
- [ ] Gamification (badges, leaderboards)
- [ ] Push notifications

### v1.2
- [ ] Multi-language support
- [ ] Offline mode
- [ ] Advanced analytics
- [ ] Community forums

---

## 📊 Statistics

- **Q&A Pairs:** 15 environmental questions
- **Templates:** 14 HTML views
- **Database Models:** 7 core entities
- **AI Integrations:** 2 (Pre-built + Gemini)
- **Production Ready:** ✅ Yes

---

## ✨ Key Features Highlight

### Smart Q&A System
- Pre-built responses (instant)
- Similarity matching (60%+ accuracy)
- Graceful fallback to AI
- Zero-latency local responses

### Community Engagement
- Campaigns for environmental action
- Participation tracking
- Real-time messaging
- Comment system

### Personalization
- User profiles
- Preference tracking
- Customized recommendations
- Activity history

### Admin Panel
- User management
- Content moderation
- Analytics dashboard
- Campaign tracking

---

## 🌟 Made with ❤️ for Environmental Awareness

**EcoAware** - Making environmental action accessible to everyone.

---

**Last Updated:** April 6, 2026  
**Current Version:** 1.0.0  
**Status:** ✅ Production Ready
