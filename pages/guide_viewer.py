"""Guide viewer page - displays individual guide content."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Guide - How To Work A Cat",
    page_icon="🐱",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .urgency-now {
        background-color: #ff4444;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .urgency-today {
        background-color: #E39A3B;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .topic-badge {
        display: inline-block;
        background-color: #E39A3B;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 3px;
        font-size: 0.8rem;
        margin-right: 0.25rem;
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

# Display urgency if applicable
if guide.urgency:
    urgency_class = f"urgency-{guide.urgency.lower()}"
    st.markdown(f'<div class="{urgency_class}">⚠️ Urgency: {guide.urgency.upper()}</div>', unsafe_allow_html=True)

# Display title and summary
st.title(guide.title)
st.markdown(f"*{guide.summary}*")

# Topic badges
if guide.topics:
    topic_html = " ".join([f'<span class="topic-badge">{topic}</span>' for topic in guide.topics])
    st.markdown(topic_html, unsafe_allow_html=True)

# Age range if specified
if guide.age_min_weeks is not None or guide.age_max_weeks is not None:
    age_min = guide.age_min_weeks or 0
    age_max = guide.age_max_weeks or "any age"
    st.caption(f"📅 Relevant for kittens: {age_min}-{age_max} weeks")

st.markdown("---")

# Display the main content
st.markdown(guide.markdown_body)

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
