# Gemini AI Integration Setup Guide

## ✅ What's Been Added:

1. **Gemini API Integration** - Your app now uses Google's Gemini AI for intelligent content recommendations
2. **Fallback System** - If Gemini API is unavailable, the app falls back to hardcoded suggestions
3. **Environment Configuration** - Secure API key management via .env file

## 🔑 How to Get Your Gemini API Key:

1. Visit: **https://aistudio.google.com/app/apikey**
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated key
5. Paste it in the `.env` file:
   ```
   GEMINI_API_KEY=your_copied_key_here
   ```

## 📁 Files Modified/Created:

- **.env** - Contains your Gemini API key (keep this secret!)
- **.env.example** - Template for reference
- **requirements.txt** - Added google-generativeai and python-dotenv
- **app.py** - Integrated Gemini API for AI recommendations

## 🚀 How AI Recommendations Work:

When a user views their dashboard, the app now:
1. Analyzes their article interactions and campaign participation
2. Identifies their top environmental interests
3. Sends a prompt to Gemini AI asking for personalized blog post ideas
4. Displays 4 AI-generated content suggestions

**Example Input:** "Climate Change, Recycling, Conservation"  
**AI Output:** 
- "Carbon Footprint Calculator: Know Your Environmental Impact"
- "Plastic-Free Living: 30-Day Challenge Guide"
- "Urban Rewilding: Creating Wildlife Sanctuaries in the City"
- "The Economics of Sustainability in 2025"

## 🔒 Security Notes:

- **Never commit .env to git** - Add `.env` to your `.gitignore`
- The API key is only used server-side, never exposed to browsers
- Each API call is rate-limited by default

## 🧪 Testing:

1. Update your `.env` file with your Gemini API key
2. Restart the Flask app
3. Log in and navigate to your dashboard
4. You'll see AI-generated content suggestions!

## 📊 Optional: Enable Content Assist for Post Creation

To also use Gemini for helping users write article content:

Add a new route to help generate article outlines:
```python
@app.route('/api/generate-outline', methods=['POST'])
@login_required
def generate_outline():
    title = request.json.get('title')
    category = request.json.get('category')
    
    if not model:
        return {'error': 'AI service unavailable'}, 503
    
    try:
        prompt = f"Create a concise 4-point outline for an article titled '{title}' about {category}."
        response = model.generate_content(prompt)
        return {'outline': response.text}
    except Exception as e:
        return {'error': str(e)}, 500
```

## 📞 Troubleshooting:

**"GEMINI_API_KEY not found" warning:**
- Make sure `.env` file exists in the project root
- Restart Flask after adding the API key
- Check that the key is correctly formatted (no extra spaces)

**API calls failing:**
- Verify your API key is active at https://aistudio.google.com
- Check your rate limits (free tier has limits)
- Look at Flask console output for detailed error messages

---

✨ Your app is ready with AI-powered recommendations! 🚀
