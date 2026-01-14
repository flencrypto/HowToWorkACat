import streamlit as st
from database import KittenGuideDB
from content_loader import load_sample_content
import os

# Page configuration
st.set_page_config(
    page_title="How To Work A Cat 🐱",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UK-themed, mobile-friendly design
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E2E2E;
        margin-bottom: 1rem;
    }
    .urgency-now {
        background-color: #ff4444;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .urgency-today {
        background-color: #E39A3B;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .urgency-monitor {
        background-color: #8FAF9A;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .guide-card {
        border: 1px solid #B8B8B8;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #FFFFFF;
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
def init_database():
    """Initialize database and load sample content if needed."""
    db_path = "kitten_guide.db"
    db = KittenGuideDB(db_path)
    
    # Load sample content if database is empty
    if len(db.get_all_guides()) == 0:
        load_sample_content(db)
    
    return db

db = init_database()

# Main page
st.markdown('<div class="main-header">🐱 How To Work A Cat</div>', unsafe_allow_html=True)
st.markdown("### A playful, UK-toned guide for first-time kitten owners")

# Quick panic buttons
st.markdown("#### 🆘 Quick Help (Panic Mode)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("😿 Not eating", use_container_width=True):
        st.session_state['selected_guide'] = 'not-eating'
        st.switch_page("pages/guide_viewer.py")

with col2:
    if st.button("🚽 Litter disasters", use_container_width=True):
        st.session_state['selected_guide'] = 'litter-tray-basics'
        st.switch_page("pages/guide_viewer.py")

with col3:
    if st.button("😾 Biting/scratching", use_container_width=True):
        st.session_state['selected_guide'] = 'biting-hands'
        st.switch_page("pages/guide_viewer.py")

with col4:
    if st.button("🏃 Zoomies at 3am", use_container_width=True):
        st.session_state['selected_guide'] = 'zoomies-2am'
        st.switch_page("pages/guide_viewer.py")

# Emergency card - always visible
with st.expander("🔴 **WHEN TO CALL VET NOW** - Click to expand", expanded=False):
    emergency_guide = db.get_guide("emergency-vet-now")
    if emergency_guide:
        st.markdown(emergency_guide.markdown_body)

st.markdown("---")

# Navigation guide
st.markdown("### 📱 Navigation")
st.markdown("""
Use the **sidebar** to navigate through the app:

- 🏠 **Home** - You are here! Quick panic buttons and overview
- 📚 **Kitten Ops Manual** - Step-by-step onboarding for your first days
- 🔍 **Search** - Find help for specific issues
- 📖 **Library** - Browse all guides by topic
- ⭐ **Saved** - Your bookmarked guides for quick access
- 🆘 **Emergency** - When to call a vet NOW

**First time here?** Start with the Kitten Ops Manual to get set up properly from day one.
""")

# Featured guides
st.markdown("### ✨ Start Here")
featured_ids = ["first-24-hours", "litter-tray-basics", "emergency-vet-now"]
featured_guides = [db.get_guide(gid) for gid in featured_ids if db.get_guide(gid)]

for guide in featured_guides:
    with st.container():
        st.markdown(f'<div class="guide-card">', unsafe_allow_html=True)
        
        # Urgency badge if applicable
        if guide.urgency:
            urgency_class = f"urgency-{guide.urgency.lower()}"
            st.markdown(f'<span class="{urgency_class}">{guide.urgency}</span>', unsafe_allow_html=True)
        
        st.markdown(f"#### {guide.title}")
        st.markdown(f"*{guide.summary}*")
        
        # Topic badges
        topic_html = " ".join([f'<span class="topic-badge">{topic}</span>' for topic in guide.topics])
        st.markdown(topic_html, unsafe_allow_html=True)
        
        if st.button(f"Read guide", key=f"read_{guide.id}", use_container_width=True):
            st.session_state['selected_guide'] = guide.id
            st.switch_page("pages/guide_viewer.py")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<small>
**Disclaimer**: This app provides general guidance based on RSPCA and Cats Protection advice. 
It is not a substitute for professional veterinary advice. When in doubt, always consult your vet.
</small>
""", unsafe_allow_html=True)
