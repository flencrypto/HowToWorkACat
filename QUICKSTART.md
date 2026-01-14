# Quick Start Guide

## How to Work a Cat 🐱

A playful, UK-toned, offline-first kitten-care guide built with Streamlit.

### Running Locally

```bash
# 1. Clone the repository
git clone <repository-url>
cd moduletemplate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

# 4. Open your browser to http://localhost:8501
```

### Deploy to Streamlit Cloud (Recommended - FREE)

1. **Fork/Clone** this repository to your GitHub account
2. **Visit** [share.streamlit.io](https://share.streamlit.io)
3. **Sign in** with GitHub
4. **Click** "New app"
5. **Configure:**
   - Repository: Your forked repo
   - Branch: `main`
   - Main file path: `app.py`
6. **Click** "Deploy!"

Your app will be live at `https://[your-app-name].streamlit.app`

### Deploy with Docker

```bash
# Build the image
docker build -t kitten-guide .

# Run the container
docker run -p 8501:8501 kitten-guide

# Access at http://localhost:8501
```

### Why NOT Netlify?

**Netlify only supports static sites** (HTML, CSS, JavaScript). This is a **Python/Streamlit application** that requires:
- Python runtime environment
- Server to execute Python code
- Active process to handle requests

**Recommended platforms instead:**
- ✅ Streamlit Community Cloud (FREE, best for Streamlit)
- ✅ Railway (easy Docker deployment)
- ✅ Render (free tier available)
- ✅ Google Cloud Run (pay-per-use)
- ✅ Heroku (requires paid plan)

### Features

- 🔍 **Offline Search**: Full-text search with filters
- 📚 **Kitten Ops Manual**: Step-by-step onboarding checklist
- 🆘 **Panic Buttons**: Quick access to common issues
- 💾 **Offline-first**: All content bundled locally
- 📱 **Mobile-friendly**: Responsive design
- ⭐ **Bookmarks**: Save your favorite guides

### Project Structure

```
moduletemplate/
├── app.py                      # Main Streamlit app
├── database.py                 # SQLite database management
├── models.py                   # Data models
├── content_loader.py           # Sample content
├── pages/                      # Streamlit multi-page app
│   ├── 0_kitten_ops_manual.py
│   ├── 1_search.py
│   ├── 2_library.py
│   ├── 3_saved.py
│   ├── 4_emergency.py
│   └── guide_viewer.py
├── .streamlit/                 # Streamlit configuration
│   └── config.toml
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration
└── DEPLOYMENT.md               # Detailed deployment guide
```

### Tech Stack

- **Framework**: Streamlit 1.23.1
- **Database**: SQLite3
- **Data**: Pandas 2.0.3
- **Language**: Python 3.12

### Support

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

For issues or questions, create an issue in this repository.

### License

See LICENSE file for details.
