# EcoAware Deployment Guide

## 🚀 Quick Start - Deploy to Render (Recommended)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "EcoAware production ready"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ecoaware.git
git push -u origin main
```

### Step 2: Connect to Render
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the repo and branch (main)
5. Fill in these settings:
   - **Name:** ecoaware-app (or your choice)
   - **Environment:** Python 3
   - **Build Command:** Auto-detected from render.yaml
   - **Start Command:** Auto-detected from render.yaml
   - **Plan:** Free

### Step 3: Add Environment Variables
In Render dashboard, add these environment variables:
```
FLASK_ENV=production
FLASK_DEBUG=0
GEMINI_API_KEY=your_actual_api_key_here
SECRET_KEY=generate_a_strong_random_key
DATABASE_URL=postgresql://user:pass@localhost/ecoaware
```

**Generate a strong SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

### Step 4: Deploy
- Click "Create Web Service"
- Render auto-deploys from git pushes
- Your app will be live at `https://ecoaware-app-xxxx.onrender.com`

---

## Alternative: Deploy to Heroku

### Step 1: Install Heroku CLI
```bash
# Windows: Download from https://devcenter.heroku.com/articles/heroku-cli
# Or use chocolatey:
choco install heroku-cli
```

### Step 2: Login & Deploy
```bash
heroku login
heroku create ecoaware-app
git push heroku main
```

### Step 3: Add Environment Variables
```bash
heroku config:set GEMINI_API_KEY=your_key
heroku config:set SECRET_KEY=your_strong_key
heroku config:set FLASK_ENV=production
```

### Step 4: Set up Database
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

---

## PythonAnywhere (Easiest - No Git Needed)

1. Go to https://www.pythonanywhere.com
2. Create free account
3. Upload your project files via Web Interface
4. Create a Flask web app
5. Configure:
   - Source code: `/home/username/ecoaware/app.py`
   - WSGI file: Auto-generated
6. Add environment variables in Web tab → Environment variables
7. Reload web app

---

## Pre-Deployment Checklist

### ✅ Files Ready
- [x] `requirements.txt` - Contains all dependencies + gunicorn
- [x] `Procfile` - Heroku/Render configuration
- [x] `.gitignore` - Excludes unnecessary files
- [x] `wsgi.py` - WSGI entry point
- [x] `render.yaml` - Render-specific config
- [x] `.env.example` - Template for environment variables

### ✅ Code Ready
- [x] `app.py` - Flask application with all routes
- [x] `models.py` - SQLAlchemy models
- [x] `dummy_qa_data.json` - Pre-built Q&A responses
- [x] `templates/` - All HTML templates
- [x] `static/` - CSS and JS files

### ✅ Database
- [ ] Update `models.py` to use PostgreSQL in production:
  ```python
  if os.getenv('DATABASE_URL'):
      app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
  ```

### ✅ Environment
- [x] Copy `.env.example` → `.env` (local development)
- [ ] Generate strong `SECRET_KEY`
- [ ] Add valid `GEMINI_API_KEY`
- [ ] Set `FLASK_ENV=production` on deployed server

---

## Production Configuration

### Update app.py for Production:

```python
# At the top of app.py
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Use environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///ecoaware.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Disable debug in production
DEBUG = os.getenv('FLASK_DEBUG', '0') == '1'
```

### At the end of app.py:

```python
if __name__ == '__main__':
    # This won't run on Render/Heroku, but good for local testing
    app.run(
        debug=os.getenv('FLASK_ENV') == 'development',
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000))
    )
```

---

## Database Migration (SQLite → PostgreSQL)

When moving from SQLite to PostgreSQL in production:

### Option 1: Fresh Database
```bash
# On production server
python init_db.py
```

### Option 2: Migrate Existing Data
```bash
# Export from SQLite
sqlite3 ecoaware.db .dump > backup.sql

# Import to PostgreSQL
psql postgresql://user:pass@host/ecoaware < backup.sql
```

---

## Monitoring & Logs

### Render Logs:
```
https://dashboard.render.com → Select App → Logs
```

### Heroku Logs:
```bash
heroku logs --tail
```

### PythonAnywhere Logs:
```
Web → Log Files (in Web tab)
```

---

## Troubleshooting

### Issue: "Module not found"
**Solution:** Update `requirements.txt`
```bash
pip freeze > requirements.txt
```
Then commit and push.

### Issue: "No such file or directory: dummy_qa_data.json"
**Solution:** Ensure file is committed to git:
```bash
git add dummy_qa_data.json
git commit -m "Add dummy QA data"
git push
```

### Issue: "GEMINI_API_KEY not set"
**Solution:** Add environment variable in platform dashboard
- Render: Settings → Environment Variables
- Heroku: `heroku config:set GEMINI_API_KEY=your_key`
- PythonAnywhere: Web → Environment Variables

### Issue: Database connection error
**Solution:** 
1. Ensure `DATABASE_URL` is set correctly
2. For Render: Use auto-provisioned PostgreSQL
3. Test connection locally with same DATABASE_URL

---

## Security Best Practices

1. **Never commit `.env` file** - Use `.env.example` template
2. **Generate strong SECRET_KEY** - Use `secrets.token_hex(32)`
3. **Use HTTPS** - Automatic on Render/Heroku
4. **Keep dependencies updated** - `pip install --upgrade` regularly
5. **Validate all user inputs** - Already done in app
6. **Use environment variables** - For all sensitive data

---

## Performance Tips

1. **Enable caching** - Add `flask-caching` for frequently accessed data
2. **Optimize database queries** - Index common search fields
3. **Use CDN for static files** - Render/Heroku can serve static files
4. **Monitor API calls** - Gemini API has rate limits
5. **Enable gzip compression** - Added via gunicorn

---

## Next Steps After Deployment

1. Test all features on production
2. Set up error monitoring (Sentry)
3. Configure automated backups (database)
4. Set up continuous deployment from main branch
5. Monitor logs regularly
6. Plan scaling strategy

---

## Contact Support

- **Render Support:** https://render.com/docs
- **Heroku Docs:** https://devcenter.heroku.com
- **Flask Docs:** https://flask.palletsprojects.com
- **SQLAlchemy:** https://docs.sqlalchemy.org

---

**Status:** 🟢 Ready to Deploy  
**Last Updated:** 2026-04-06
