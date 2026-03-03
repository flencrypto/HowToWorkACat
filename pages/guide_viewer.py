"""Guide viewer page - displays individual guide content (v2)."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Guide - How to Work a Cat",
    page_icon="🐱",
    layout="wide"
)

# V2 CSS
st.markdown("""
<style>
    :root {
        --cat-orange: #F07A33;
        --cat-teal:   #3AAFA9;
        --cat-purple: #7B5EA7;
        --cat-red:    #E84040;
        --cat-green:  #5BAD8B;
    }
    .guide-hero {
        background: linear-gradient(135deg, var(--cat-teal) 0%, var(--cat-purple) 100%);
        border-radius: 14px;
        padding: 1.5rem 2rem;
        color: white;
        margin-bottom: 1.2rem;
    }
    .guide-hero h1 { margin: 0; font-size: 1.9rem; font-weight: 900; }
    .guide-hero p  { margin: 0.3rem 0 0; opacity: 0.9; font-size: 1.05rem; }

    .urgency-now {
        background-color: var(--cat-red);
        color: white;
        padding: 0.3rem 0.9rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.85rem;
        display: inline-block;
        margin-bottom: 0.6rem;
    }
    .urgency-today {
        background-color: var(--cat-orange);
        color: white;
        padding: 0.3rem 0.9rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.85rem;
        display: inline-block;
        margin-bottom: 0.6rem;
    }
    .topic-badge {
        display: inline-block;
        background-color: var(--cat-teal);
        color: white;
        padding: 0.2rem 0.55rem;
        border-radius: 12px;
        font-size: 0.78rem;
        margin-right: 0.3rem;
        margin-bottom: 0.3rem;
    }
    .do-dont-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    .do-box {
        flex: 1;
        background: #f0fbf6;
        border: 2px solid var(--cat-green);
        border-radius: 10px;
        padding: 0.8rem 1rem;
    }
    .dont-box {
        flex: 1;
        background: #fff5f5;
        border: 2px solid var(--cat-red);
        border-radius: 10px;
        padding: 0.8rem 1rem;
    }
    .do-box h4, .dont-box h4 { margin: 0 0 0.4rem; }
    .related-card {
        border-radius: 10px;
        padding: 0.7rem 1rem;
        background: #f9f9f9;
        border: 1px solid #e0e0e0;
        margin-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
@st.cache_resource
def get_db():
    return KittenGuideDB()

db = get_db()

# Get selected guide from session state
guide_id = st.session_state.get('selected_guide')

if not guide_id:
    st.warning("No guide selected. Please go back to the home page and select a guide.")
    if st.button("← Back to Home"):
        st.switch_page("app.py")
    st.stop()

# Load the guide
guide = db.get_guide(guide_id)

if not guide:
    st.error(f"Guide '{guide_id}' not found.")
    if st.button("← Back to Home"):
        st.switch_page("app.py")
    st.stop()

# Back button and bookmark
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("app.py")

with col3:
    is_bookmarked = db.is_bookmarked(guide.id)
    if is_bookmarked:
        if st.button("⭐ Saved", use_container_width=True):
            db.remove_bookmark(guide.id)
            st.rerun()
    else:
        if st.button("☆ Save", use_container_width=True):
            db.add_bookmark(guide.id)
            st.rerun()

# Track guide as read
if 'guides_read' not in st.session_state:
    st.session_state['guides_read'] = set()
st.session_state['guides_read'].add(guide.id)

# Hero card
urgency_html = ""
if guide.urgency:
    urgency_class = f"urgency-{guide.urgency.lower()}"
    urgency_html = f'<span class="{urgency_class}">⚠️ {guide.urgency.upper()}</span><br><br>'

topic_html = " ".join([f'<span class="topic-badge">{t}</span>' for t in guide.topics])

age_html = ""
if guide.age_min_weeks is not None or guide.age_max_weeks is not None:
    age_min = guide.age_min_weeks or 0
    age_max = guide.age_max_weeks or "any age"
    age_html = f'<br><small>📅 Relevant for kittens: {age_min}–{age_max} weeks</small>'

st.markdown(f"""
<div class="guide-hero">
{urgency_html}<h1>{guide.title}</h1>
<p>{guide.summary}</p>
{age_html}
</div>
{topic_html}
""", unsafe_allow_html=True)

st.markdown("---")

# Main content
st.markdown(guide.markdown_body)

# Do / Don't visual cards (if available)
if guide.do_list or guide.dont_list:
    st.markdown("---")
    do_items   = "".join([f"<li>✅ {item}</li>" for item in guide.do_list])
    dont_items = "".join([f"<li>❌ {item}</li>" for item in guide.dont_list])
    st.markdown(f"""
<div class="do-dont-row">
  <div class="do-box">
    <h4>✅ Do</h4>
    <ul style="margin:0;padding-left:1.2rem">{do_items}</ul>
  </div>
  <div class="dont-box">
    <h4>❌ Don't</h4>
    <ul style="margin:0;padding-left:1.2rem">{dont_items}</ul>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Display analogy cards if available
if guide.analogy_cards:
    st.markdown("### 🎯 Human Analogy")
    for card in guide.analogy_cards:
        st.info(card)

# Navigation to related guides
st.markdown("### 📚 Related Topics")
related_col1, related_col2, related_col3 = st.columns(3)

# Suggest guides based on topics
all_guides = db.get_all_guides()
related = [g for g in all_guides if g.id != guide.id and any(t in guide.topics for t in g.topics)][:3]

if related:
    for idx, rel_guide in enumerate(related):
        with [related_col1, related_col2, related_col3][idx]:
            if st.button(f"📖 {rel_guide.title}", key=f"related_{rel_guide.id}", use_container_width=True):
                st.session_state['selected_guide'] = rel_guide.id
                st.rerun()
else:
    st.caption("No related guides found.")
