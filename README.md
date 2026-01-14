<<<<<<< HEAD
# How To Work A Cat 🐱
=======
# How to Work a Cat 🐱
>>>>>>> main

A playful, UK-toned, offline-first kitten-care guide for first-time kitten owners, families, and temporary fosterers.

## Overview

<<<<<<< HEAD
**How To Work A Cat** is a reassuring, lightly sarcastic guide explaining real kitten needs via analogies, metaphors, and human comparisons. Think: "keep the litter tray like a shared bathroom you'd happily eat toast in" or "you're not a 24/7 chew-toy subscription service".
=======
**How to Work a Cat** is a reassuring, lightly sarcastic guide explaining real kitten needs via analogies, metaphors, and human comparisons. Think: "keep the litter tray like a shared bathroom you'd happily eat toast in" or "you're not a 24/7 chew-toy subscription service".
>>>>>>> main

### Application Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Web App                        │
│                      (app.py)                               │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Home Page  │  │    Search    │  │   Library    │      │
│  │  (Panic     │  │  (Full-text) │  │  (Browse by  │      │
│  │   Buttons)  │  │              │  │    Topic)    │      │
│  └─────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Kitten Ops  │  │    Saved     │  │  Emergency   │      │
│  │   Manual    │  │  Bookmarks   │  │   (Red Flags)│      │
│  └─────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
           ┌───────────────────────┐
           │   Database Layer      │
           │   (database.py)       │
           │                       │
           │  SQLite: Guides,      │
           │  Diagrams, Bookmarks  │
           └───────────────────────┘
                       ▲
                       │
           ┌───────────────────────┐
           │   Content Loader      │
           │  (content_loader.py)  │
           │                       │
           │  Sample kitten-care   │
           │  guides & diagrams    │
           └───────────────────────┘
```

### Core Features

- 🔍 **Offline Search**: Full-text search with filters (age, topic, urgency)
  - Search by keywords, topics, or specific issues
  - Filter by kitten age and urgency level
  - Instant results from local database
  
- 📚 **Kitten Ops Manual**: Step-by-step onboarding checklist for your first 10 steps
  - Day-by-day guidance for the first week
  - Interactive checklists to track progress
  - Essential setup tasks prioritized
  
- 🎨 **Diagram Pack**: Visual guides for safe room setup, body language, poison risks
  - ASCII diagrams for safe room layouts
  - Cat body language decoder charts
  - Visual decision trees for common problems
  - Litter tray placement guides
  
- 🆘 **Panic Buttons**: Quick access to "Not eating", "Litter disasters", "Scratching sofa", etc.
  - One-click access to emergency guides
  - Fast solutions for 3am crises
  - Clear "Do this NOW" steps
  
- 💾 **Offline-first**: All content bundled and searchable without internet
  - No internet required after initial load
  - SQLite database for fast queries
  - Works anywhere, anytime

### Target Users

- First-time kitten owners in panic mode
- Parents with family kitten
- Temporary fosterers
- Anyone facing: biting, scratching, zoomies at 3am, hiding, or litter disasters

### User Journey Flow

```
    New User Arrives
          ↓
    ┌─────────────────┐
    │   Home Page     │ ← Panic buttons for immediate help
    │   🆘 Quick Help │
    └─────────────────┘
          ↓
    First time? → Kitten Ops Manual (Day-by-day guide)
          ↓
    Specific issue? → Search or Library
          ↓
    Found solution? → Bookmark for later (Saved section)
          ↓
    Red flags? → Emergency page (When to call vet NOW)
```

### Content Principles

- UK spelling (behaviour, favourite, colour)
- Every page includes: "Why this matters", "If you're stuck" box, "Do this now" panic steps
- Warm, reassuring tone that's never mean or cruel
- Sourced from RSPCA, Cats Protection, and vetted vet guidance
- Clear red flags for "call a vet NOW" situations

## Installation

### Local Development

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deployment

⚠️ **Important**: This is a Python/Streamlit application. **Netlify cannot host this app** as it only supports static sites.

#### Recommended: Streamlit Community Cloud (FREE & Easy)

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub and click "New app"
4. Select your repository, branch (`main`), and file (`app.py`)
5. Click "Deploy"

Your app will be live at `https://[your-app-name].streamlit.app`

#### Alternative Platforms

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on:
- Docker deployment (Railway, Render, Google Cloud Run)
- Heroku deployment
- Azure App Service
- Self-hosted options

**Quick Docker deployment:**
```bash
docker build -t kitten-guide .
docker run -p 8501:8501 kitten-guide
```

## Usage

Navigate through the sidebar to access:
- **Guide**: Onboarding flows and progress tracking
- **Search**: Find help for specific issues
- **Library**: Browse by topic (Feeding, Litter, Behaviour, Health, Safety)
- **Saved**: Your bookmarked guides
- **Emergency**: When to call a vet NOW

## Safety Framework

Urgency levels clearly marked:
- 🔴 **Now**: Call vet immediately (breathing issues, persistent vomiting, blood in stool)
- 🟠 **Today**: Schedule vet visit today
- 🟡 **Monitor**: Watch and note, mention at next checkup

## License

See LICENSE file for details.

