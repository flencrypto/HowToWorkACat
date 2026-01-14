"""Saved guides page - user bookmarks."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Saved - How To Work A Cat",
    page_icon="⭐",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .guide-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #f9f9f9;
    }
    .topic-badge {
        display: inline-block;
        background-color: #3498db;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 3px;
        font-size: 0.8rem;
        margin-right: 0.25rem;
    }
    .urgency-now {
        background-color: #ff4444;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 3px;
        font-size: 0.8rem;
    }
    .urgency-today {
        background-color: #ff9800;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 3px;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
@st.cache_resource
def get_db():
    return KittenGuideDB()

db = get_db()

st.title("⭐ Saved Guides")
st.markdown("Your bookmarked guides for quick access")

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
