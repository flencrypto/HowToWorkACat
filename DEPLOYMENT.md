# DEPLOYMENT.md

## How to Deploy "How To Work A Cat" Streamlit App

### ⚠️ Important: Netlify is NOT Compatible

**Netlify cannot host this application** because:
- Netlify is designed for static sites (HTML, CSS, JavaScript)
- This is a Python/Streamlit web application that requires a Python runtime
- Streamlit apps need a server to run Python code

### ✅ Recommended: Streamlit Community Cloud (FREE)

**Best option** for deploying Streamlit apps with zero configuration:

1. **Prerequisites:**
   - GitHub account
   - This repository pushed to GitHub
   - No credit card required!

2. **Deployment Steps:**
   ```
   1. Visit https://share.streamlit.io
   2. Sign in with GitHub
   3. Click "New app"
   4. Select:
      - Repository: [your-username]/[your-repo-name]
      - Branch: main (or your branch)
      - Main file path: app.py
   5. Click "Deploy!"
   ```

3. **Your app will be live at:**
   ```
   https://[your-chosen-name].streamlit.app
   ```

4. **Features:**
   - Automatic deployments from GitHub
   - Free SSL certificate
   - Built-in monitoring
   - Resource limits: Suitable for this app size

### Alternative Deployment Options

#### Option 1: Docker on Railway/Render/Cloud Run

1. **Use the included Dockerfile:**
   ```bash
   docker build -t kitten-guide .
   docker run -p 8501:8501 kitten-guide
   ```

2. **Deploy to Railway:**
   - Connect GitHub repo
   - Railway auto-detects Dockerfile
   - Click deploy

3. **Deploy to Render:**
   - New Web Service from Docker
   - Connect repo
   - Deploy

4. **Deploy to Google Cloud Run:**
   ```bash
   gcloud run deploy kitten-guide --source .
   ```

#### Option 2: Heroku (requires Procfile)

Create `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

Deploy:
```bash
heroku create your-app-name
git push heroku main
```

#### Option 3: Azure App Service

```bash
az webapp up --name kitten-guide --runtime "PYTHON:3.12"
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Access at: http://localhost:8501
```

### Environment Variables

This app currently doesn't require any environment variables, but for future use:

**Streamlit Cloud:**
- Add secrets in the Streamlit Cloud dashboard
- Access via `st.secrets["KEY_NAME"]`

**Docker/Other platforms:**
- Set environment variables in deployment config
- Access via `os.environ.get("KEY_NAME")`

### Database

The app uses SQLite (file: `kitten_guide.db`):
- Created automatically on first run
- Pre-populated with sample content
- Persists between restarts on most platforms
- For Streamlit Cloud: Use st.cache_resource for database connection

### Troubleshooting

**App won't start:**
- Check Python version (requires 3.8+)
- Verify all dependencies in requirements.txt
- Check logs for import errors

**Database issues:**
- Ensure write permissions for app directory
- For cloud deployments, consider using persistent volume

**Performance:**
- App loads sample data on first run
- Database queries are optimized
- Should handle moderate traffic fine

### Support

For deployment issues:
- Streamlit Community: https://discuss.streamlit.io
- GitHub Issues: Create an issue in this repo
- Documentation: https://docs.streamlit.io/streamlit-community-cloud

### Cost Comparison

| Platform | Cost | Notes |
|----------|------|-------|
| Streamlit Cloud | FREE | Best for Streamlit apps |
| Railway | $5-10/mo | Includes database |
| Render | FREE tier available | Good alternative |
| Google Cloud Run | Pay per use | Very cheap for low traffic |
| Heroku | $7/mo minimum | Requires paid dyno |
| Azure | Varies | Good for enterprise |

**Recommendation:** Start with Streamlit Community Cloud (free), migrate to Railway or Render if you need more resources.
