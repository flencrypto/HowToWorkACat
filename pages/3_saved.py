"""Saved guides page - user bookmarks (v2)."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Saved - How to Work a Cat",
    page_icon="⭐",
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
        --cat-yellow: #F5C842;
    }
    .saved-hero {
        background: linear-gradient(135deg, #F5C842 0%, #F07A33 100%);
        border-radius: 14px;
        padding: 1.4rem 2rem;
        color: white;
        margin-bottom: 1.2rem;
    }
    .saved-hero h2 { margin: 0; font-size: 2rem; font-weight: 900; }
    .saved-hero p  { margin: 0.3rem 0 0; opacity: 0.9; }
    .guide-card {
        border: none;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        margin: 0.6rem 0;
        background-color: #FFFFFF;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
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
    .urgency-now {
        background-color: var(--cat-red);
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .urgency-today {
        background-color: var(--cat-orange);
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
@st.cache_resource
def get_db():
    return KittenGuideDB()

db = get_db()

st.markdown("""
<div class="saved-hero">
  <h2>⭐ Saved Guides</h2>
  <p>Your bookmarked guides — ready for the next crisis at any hour</p>
</div>
""", unsafe_allow_html=True)

# Get bookmarked guides
bookmarked_guides = db.get_bookmarked_guides()

if not bookmarked_guides:
    st.info("You haven't saved any guides yet. Browse the library or search for guides and click the ☆ Save button.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔍 Search Guides", use_container_width=True):
            st.switch_page("pages/1_search.py")
    with col2:
        if st.button("📖 Browse Library", use_container_width=True):
            st.switch_page("pages/2_library.py")
else:
    st.markdown(f"### {len(bookmarked_guides)} saved guide(s)")
    
    for guide in bookmarked_guides:
        with st.container():
            st.markdown('<div class="guide-card">', unsafe_allow_html=True)
            
            # Urgency badge
            if guide.urgency:
                urgency_class = f"urgency-{guide.urgency.lower()}"
                st.markdown(f'<span class="{urgency_class}">{guide.urgency}</span>', unsafe_allow_html=True)
            
            st.markdown(f"### {guide.title}")
            st.markdown(f"*{guide.summary}*")
            
            # Topic badges
            if guide.topics:
                topic_html = " ".join([f'<span class="topic-badge">{topic}</span>' for topic in guide.topics])
                st.markdown(topic_html, unsafe_allow_html=True)
            
            # Analogy preview
            if guide.analogy_cards:
                st.caption(f"💡 {guide.analogy_cards[0]}")
            
            # Action buttons
            btn_col1, btn_col2 = st.columns([3, 1])
            with btn_col1:
                if st.button(f"Read guide", key=f"read_{guide.id}", use_container_width=True):
                    st.session_state['selected_guide'] = guide.id
                    st.switch_page("pages/guide_viewer.py")
            with btn_col2:
                if st.button(f"🗑️ Remove", key=f"remove_{guide.id}", use_container_width=True):
                    db.remove_bookmark(guide.id)
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
