# Copilot Instructions — How to Work a Cat

This repository contains "How to Work a Cat", an offline-first Python/Streamlit kitten care guide with SQLite database backend.

## Goals
- Keep the app offline-first: core content, diagrams, and search must work without network.
- Prefer small, reviewable PRs with tests when test infrastructure exists.
- Follow existing patterns and file organization; do not introduce new architectures unless requested.
- Maintain UK spelling and warm, reassuring tone in all content.

## Architecture Overview

```
Streamlit Web App (app.py)
├── Pages (pages/*.py)
│   ├── Home (panic buttons, quick access)
│   ├── Kitten Ops Manual (onboarding checklist)
│   ├── Search (full-text local search)
│   ├── Library (browse by topic)
│   ├── Saved (bookmarks)
│   └── Emergency (red flags)
├── Database Layer (database.py)
│   └── SQLite: guides, diagrams, bookmarks, search index
├── Models (models.py)
│   └── Data classes: Guide, Diagram, Step, etc.
└── Content Loader (content_loader.py)
    └── Sample kitten-care guides
```

## How to Build & Test

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Testing
- No automated test suite currently exists
- Manual testing required: run the app and verify functionality
- Test all major user journeys:
  - Search functionality
  - Navigation between pages
  - Bookmark save/load
  - Content display and formatting

### Linting
- Follow PEP 8 Python style guide
- Use type hints where practical (see models.py for examples)
- If adding linting tools, prefer: `pylint`, `flake8`, or `black`

## Coding Standards

### Python Best Practices
- Use type hints for function parameters and return values
- Prefer dataclasses for data models (see models.py)
- Use docstrings for modules, classes, and non-trivial functions
- Keep functions focused and single-purpose
- Avoid global mutable state

### Streamlit Patterns
- Use `st.cache_data` for expensive computations or data loading
- Initialize database connection with `check_same_thread=False` for SQLite
- Keep page files in `pages/` directory with numeric prefixes for ordering
- Use consistent styling with custom CSS in markdown blocks

### Database Patterns
- SQLite is the only database; no external DB services
- Store all content in local database for offline access
- Use parameterized queries to prevent SQL injection
- Index frequently searched fields (title, tags, topics)
- Keep database schema migrations simple and documented

### UK Tone & Content
- Always use UK spelling: behaviour, favourite, colour, recognise, organise
- Maintain warm, reassuring, lightly sarcastic tone
- Include analogies and metaphors for complex concepts
- Every guide should have: "Why this matters", red flags, practical steps
- Clear urgency markers: 🔴 Now, 🟠 Today, 🟡 Monitor

## Offline-First Rules

**Critical**: This app must work completely offline after initial load.

- Never require network for core user journeys (Guide, Search, Library, Saved, Emergency)
- All content must be bundled in the SQLite database or local files
- Search must be entirely local (no API calls)
- Images/diagrams should be ASCII art or embedded in markdown
- No CDN dependencies, no external API calls, no analytics that break offline

## Search Implementation

- Search is local only (SQLite full-text search)
- Supports filtering by: age range, topic, urgency
- Ranking should be deterministic and based on:
  - Title matches (highest priority)
  - Tag matches
  - Body text matches
  - Urgency boost for emergency content
- Keep search index updated when content changes

## Data Models

Key data structures (see `models.py`):
- `Guide`: Main content unit with title, markdown body, topics, urgency
- `Diagram`: Visual guides (ASCII art with captions)
- `Step`: Individual step in onboarding flow
- `Bookmark`: User-saved guides
- `SearchResult`: Search result with scoring

## File Organization

```
/
├── app.py                 # Main Streamlit app & home page
├── database.py            # SQLite database management
├── models.py              # Data classes
├── content_loader.py      # Sample content initialization
├── pages/                 # Streamlit pages (auto-discovered)
│   ├── 0_kitten_ops_manual.py
│   ├── 1_search.py
│   ├── 2_library.py
│   ├── 3_saved.py
│   ├── 4_emergency.py
│   └── guide_viewer.py
├── requirements.txt       # Python dependencies
└── .streamlit/           # Streamlit config (gitignored)
```

## Common Tasks

### Adding a New Guide
1. Create a `Guide` object in `content_loader.py`
2. Include: title, summary, markdown body, topics, urgency level
3. Add appropriate age ranges if relevant
4. Test search indexing and filtering

### Adding a New Page
1. Create `pages/N_page_name.py` (N = order number)
2. Import necessary components from database/models
3. Use consistent page header and navigation patterns
4. Test mobile responsiveness

### Modifying Database Schema
1. Update schema in `database.py` `_init_db()`
2. Update corresponding model in `models.py`
3. Consider migration path for existing databases
4. Update CRUD operations to match new schema

## PR Expectations

- Keep changes focused and minimal
- Add docstrings for new functions/classes
- Manual test all affected user journeys
- Include screenshots for UI changes
- Avoid unrelated formatting changes
- Update README.md if adding major features
- Ensure offline-first principles are maintained

## Security & Safety

- No hardcoded secrets or API keys
- Sanitize any user input (though currently minimal user input)
- Keep emergency/urgency markers accurate and visible
- Clearly distinguish "call vet NOW" vs "monitor" advice
- Don't introduce dependencies with known vulnerabilities

## Deployment Notes

- Primary platform: Streamlit Community Cloud (free)
- Alternative: Docker deployment (Dockerfile included)
- Not compatible with static site hosts (Netlify, GitHub Pages)
- See DEPLOYMENT.md for detailed deployment options

## What NOT to Do

- ❌ Don't add network dependencies for core features
- ❌ Don't change UK spelling to US spelling
- ❌ Don't remove or weaken emergency/red flag warnings
- ❌ Don't add complex build systems or frameworks
- ❌ Don't introduce breaking changes to database schema without migration
- ❌ Don't add dependencies that break offline functionality
- ❌ Don't modify the warm, reassuring tone to be clinical or harsh
