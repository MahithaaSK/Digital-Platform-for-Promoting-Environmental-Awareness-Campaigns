# Dummy Q&A Data for EcoAware Assistant

This document explains the dummy Q&A data for pre-built questions and AI responses related to climate change, trees, and environmental campaigns.

## Overview

**15 Pre-built Q&A Pairs** covering:
- ✅ Climate change impacts & solutions (7 pairs)
- ✅ Trees & deforestation (6 pairs) 
- ✅ Environmental campaigns (2 pairs)

## Files Generated

1. **`seed_qa_data.py`** - Standalone script that generates JSON export of all Q&A pairs
2. **`seed_qa_database.py`** - Database integration script with data structure and implementation guide
3. **`dummy_qa_data.json`** - JSON export of all Q&A pairs (ready for frontend)
4. **`DUMMY_QA_README.md`** - This file

## Q&A Categories & Topics

### Climate Change (7 Q&As)
1. What are the main causes of climate change?
2. How does climate change affect weather patterns?
3. What can individuals do to reduce their carbon footprint?
4. Is climate change reversible?
5. How does renewable energy help combat climate change?
6. How can I participate in tree planting campaigns?
7. What is the Climate March 2025 campaign about?

### Conservation & Trees (6 Q&As)
8. What happens when we cut down all trees?
9. Why is deforestation a major environmental issue?
10. What are the main causes of deforestation?
11. Which tree species grow well in tropical forests?
12. What are the best native tree species for forest restoration?
13. How long does it take for a forest to regenerate naturally?

### Pollution Control & Recycling (2 Q&As)
14. What does the River Cleanup Drive campaign do exactly?
15. How do I participate in the e-waste collection drive?

## Data Structure

Each Q&A pair contains:

```json
{
  "question": "What are the main causes of climate change?",
  "response": "Climate change is primarily caused by human activities...",
  "category": "Climate Change",
  "source": "Aura Assistant"
}
```

**Response Characteristics:**
- Average length: 3,039 characters
- Well-structured with bullet points and formatting
- Practical, actionable information
- Links to existing campaigns when relevant
- Includes specific facts and statistics

## How to Integrate

### Option 1: Add to Database (Recommended)

**Step 1: Extend `models.py`**

Add this model to store pre-built Q&As:

```python
class PreBuiltQA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    response = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(100), default='Aura Assistant')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PreBuiltQA {self.id}: {self.question[:50]}...>'
```

**Step 2: Create seeding function in `init_db.py`**

```python
from seed_qa_database import QA_PAIRS

def seed_qa_data():
    """Seed pre-built Q&A pairs into database"""
    for qa_data in QA_PAIRS:
        qa = PreBuiltQA(
            question=qa_data['question'],
            response=qa_data['response'],
            category=qa_data['category'],
            source=qa_data['source']
        )
        db.session.add(qa)
    db.session.commit()
    print(f"✓ Seeded {len(QA_PAIRS)} Q&A pairs")
```

**Step 3: Call in seed_database() or separately**

```python
def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # ... existing seeding code ...
        
        seed_qa_data()  # Add this line
```

### Option 2: Use JSON file directly (Frontend)

Load `dummy_qa_data.json` on the frontend:

```javascript
// Load pre-built questions for quick access
async function loadPrebuiltQuestions() {
  const response = await fetch('/static/dummy_qa_data.json');
  const questions = await response.json();
  displayQuickButtons(questions);
}
```

### Option 3: Use as Gemini API Fallback

Add to the Aura system prompt:

```python
AURA_SYSTEM_PROMPT = """Your purpose is to help users with environmental questions...

You have access to these pre-built responses for common questions:
[Insert Q&A data here]

If API fails, use these fallback responses."""
```

## Implementation Examples

### API Endpoint: Get all Q&As

```python
@app.route('/api/aura/prebuilt-qa')
def get_prebuilt_qa():
    questions = PreBuiltQA.query.all()
    return jsonify([
        {
            'id': q.id,
            'question': q.question,
            'category': q.category,
            'response': q.response,
            'source': q.source
        }
        for q in questions
    ])
```

### API Endpoint: Get by category

```python
@app.route('/api/aura/qa/<category>')
def get_qa_by_category(category):
    questions = PreBuiltQA.query.filter_by(category=category).all()
    return jsonify([
        {'id': q.id, 'question': q.question, 'category': q.category}
        for q in questions
    ])
```

### Frontend: Display quick buttons

```html
<div id="quick-questions" style="margin-bottom: 1rem;">
    <h5>Quick Questions:</h5>
    <div id="question-buttons" style="display: flex; flex-wrap: wrap; gap: 0.5rem;"></div>
</div>

<script>
async function loadQuickQuestions() {
    const response = await fetch('/api/aura/prebuilt-qa');
    const questions = await response.json();
    
    const container = document.getElementById('question-buttons');
    questions.forEach(q => {
        const btn = document.createElement('button');
        btn.className = 'btn btn-sm btn-outline';
        btn.textContent = q.question;
        btn.onclick = () => {
            document.getElementById('aura-input').value = q.question;
            document.getElementById('aura-form').dispatchEvent(new Event('submit'));
        };
        container.appendChild(btn);
    });
}
loadQuickQuestions();
</script>
```

## Using in Aura Assistant

### Option 1: Enhanced System Prompt

Include Q&A data in the Gemini system prompt for better context:

```python
AURA_SYSTEM_PROMPT = """You are Aura, an environmental AI assistant...

Common questions and responses you should follow:
[Formatted Q&A list]

Use these as templates for similar questions."""
```

### Option 2: Intelligent Fallback

When Gemini API has issues:

```python
def get_aura_response(user_message):
    try:
        # Try API first
        response = aura_model.generate_content(user_message)
        return response.text
    except Exception as e:
        # Fallback to pre-built Q&A
        for qa in QA_PAIRS:
            if similar_question(user_message, qa['question']):
                return qa['response']
        return "I'm temporarily unable to generate a response. Please try again."
```

### Option 3: Hybrid approach

```python
def get_smart_response(user_message):
    # Find relevant pre-built Q&A for context
    context = find_related_qa(user_message)
    
    # Include in Gemini prompt
    enhanced_prompt = f"""
    User question: {user_message}
    
    Related information:
    {context}
    
    Provide a comprehensive answer..."""
    
    return aura_model.generate_content(enhanced_prompt).text
```

## Data Usage Guide

### For Climate Change Education
- Use questions 1-5 and 12-13 for learning modules
- Reference in blog posts and articles
- Include in email newsletters

### For Campaign Promotion  
- Use questions 6-8, 14-15 for campaign pages
- Link pre-built responses from campaign descriptions
- Show in event details

### For Chatbot Enhancement
- Load questions as quick-access buttons
- Use as training data for better responses
- Include in fallback system

### For Mobile App
- Download JSON and store locally
- Display offline when needed
- Sync with database when online

## File Structure

```
seed_qa_data.py              # Generates JSON export
seed_qa_database.py          # Database integration code
dummy_qa_data.json          # Generated Q&A in JSON format
DUMMY_QA_README.md          # This documentation
```

## Running the Scripts

### Generate JSON only:

```bash
python seed_qa_data.py
# Creates: dummy_qa_data.json
```

### See database integration info:

```bash
python seed_qa_database.py
# Shows: Data structure, usage guide
```

## Example Queries & Responses

### Question: "What are the main causes of climate change?"
✓ **Gets:** Full breakdown of 6 major causes with details
✓ **Length:** 839 characters
✓ **Category:** Climate Change

### Question: "Which trees grow well in tropical forests?"
✓ **Gets:** Specific canopy trees, mid-story species, restoration tips
✓ **Length:** 2,671 characters  
✓ **Category:** Conservation

### Question: "How do I participate in tree planting campaigns?"
✓ **Gets:** Finding campaigns, participation levels, impact metrics
✓ **Length:** 3,704 characters
✓ **Category:** Climate Change

## Statistics

- **Total Q&A Pairs:** 15
- **Total Characters:** 45,585 words (~200 KB)
- **Average Response:** 3,039 characters
- **Longest Response:** 7,022 characters (E-waste campaign)
- **Shortest Response:** 839 characters (Climate causes)
- **Categories:** 4 (Climate Change, Conservation, Pollution Control, Recycling)

## Best Practices

### ✅ DO:
- Pre-load Q&A data on app startup
- Cache in memory for quick access
- Update responses when information changes
- Link to specific campaigns when mentioned
- Use as reference/training data

### ❌ DON'T:
- Hardcode in HTML templates
- Display raw JSON to users
- Use outdated campaign dates
- Forget to update links to campaigns
- Replace live Gemini API without fallback

## Future Enhancements

1. **Add More Categories:**
   - Pollution control (5+ Q&As)
   - Energy solutions (5+ Q&As)
   - Conservation (5+ Q&As)

2. **Language Support:**
   - Translate to Spanish, French, Hindi, Mandarin
   - Localize campaign information

3. **Video Integration:**
   - Link to educational videos for each topic
   - Embed in assistant responses

4. **Interactive Elements:**
   - Carbon calculator (from Q&A data)
   - Quiz based on responses
   - Campaign participation tracker

5. **Analytics:**
   - Track which questions users ask
   - Monitor campaign engagement
   - Improve response quality based on feedback

## Troubleshooting

**JSON not loading?**
- Check file path in frontend code
- Verify CORS headers if loading from different domain
- Check browser console for errors

**Q&A displaying but responses blank?**
- Ensure database model includes 'response' field
- Check migration files created the column
- Verify query returns full object

**Campaigns in responses not matching reality?**
- Update dates/locations in responses when campaigns change
- Create script to auto-update campaign references
- Consider storing campaign IDs instead of names

**API fallback not working?**
- Add error handling for API failures
- Ensure Q&A_PAIRS is imported correctly
- Test similarity matching function

## Support & Feedback

For issues or improvements:
1. Check data in `dummy_qa_data.json`
2. Verify database schema matches model
3. Test with `seed_qa_database.py` first
4. Check browser console for JavaScript errors

## License

These responses are created for the EcoAware application and can be freely used within the project.

---

**Last Updated:** 2025-04-06  
**Format Version:** 1.0  
**Status:** Ready for Production
