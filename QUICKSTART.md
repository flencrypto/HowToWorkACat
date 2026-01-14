# Quick Start Guide

## How to Work a Cat 🐱

A playful, UK-toned, offline-first kitten-care guide built with Streamlit.

### Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/flencrypto/HowToWorkACat.git
cd HowToWorkACat

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

# 4. Open your browser to http://localhost:8501
```

**What happens on first run:**
```
┌─────────────────────────────────────┐
│ 1. Database created (kitten_guide.db)│
│ 2. Sample content loaded             │
│ 3. App starts on port 8501           │
│ 4. Open browser automatically        │
└─────────────────────────────────────┘
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

**Platform Selection Guide:**
```
Need FREE hosting?
    ↓
    YES → Streamlit Community Cloud ✅
    ↓
    NO → Continue
         ↓
    Have Docker experience?
         ↓
         YES → Railway or Google Cloud Run ✅
         ↓
         NO → Render (simple UI) ✅
```

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
HowToWorkACat/
├── app.py                      # 🏠 Main Streamlit app & home page
├── database.py                 # 💾 SQLite database management
├── models.py                   # 📦 Data models (Guide, Diagram, etc.)
├── content_loader.py           # 📚 Sample kitten-care content
│
├── pages/                      # 📄 Multi-page app sections
│   ├── 0_kitten_ops_manual.py # Step-by-step onboarding
│   ├── 1_search.py            # Full-text search
│   ├── 2_library.py           # Browse by topic
│   ├── 3_saved.py             # Bookmarked guides
│   ├── 4_emergency.py         # Emergency vet guide
│   └── guide_viewer.py        # Individual guide display
│
├── .streamlit/                 # ⚙️ Streamlit configuration
│   └── config.toml            # Theme & server settings
│
├── requirements.txt            # 📋 Python dependencies
├── Dockerfile                  # 🐳 Container configuration
├── README.md                   # 📖 Main documentation
├── QUICKSTART.md              # 🚀 Quick start guide
└── DEPLOYMENT.md              # 🌐 Detailed deployment guide
```

**Key Files Explained:**
- **app.py**: Entry point with panic buttons and featured guides
- **database.py**: Handles all SQLite operations (CRUD for guides, bookmarks)
- **content_loader.py**: Pre-loads 7+ comprehensive kitten-care guides
- **pages/**: Each file creates a sidebar navigation item automatically

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
