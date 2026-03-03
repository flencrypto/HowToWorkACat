"""Search page - find guides by keywords and filters (v2)."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Search - How to Work a Cat",
    page_icon="🔍",
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
    }
    .search-hero {
        background: linear-gradient(135deg, #F07A33 0%, #7B5EA7 100%);
        border-radius: 14px;
        padding: 1.4rem 2rem;
        color: white;
        margin-bottom: 1.2rem;
    }
    .search-hero h2 { margin: 0; font-size: 2rem; font-weight: 900; }
    .search-hero p  { margin: 0.3rem 0 0; opacity: 0.9; }
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
<div class="search-hero">
  <h2>🔍 Search Guides</h2>
  <p>Find help for your kitten challenge — no judgement, we've all been there</p>
</div>
""", unsafe_allow_html=True)

# Quick search chips
st.markdown("#### 🚨 Quick Searches")
chip_col1, chip_col2, chip_col3, chip_col4 = st.columns(4)

with chip_col1:
    if st.button("Not eating", use_container_width=True):
        st.session_state['search_query'] = 'eating food'

with chip_col2:
    if st.button("Litter issues", use_container_width=True):
        st.session_state['search_query'] = 'litter tray'

with chip_col3:
    if st.button("Biting", use_container_width=True):
        st.session_state['search_query'] = 'biting'

with chip_col4:
    if st.button("Scratching", use_container_width=True):
        st.session_state['search_query'] = 'scratching'

chip_col5, chip_col6, chip_col7, chip_col8 = st.columns(4)

with chip_col5:
    if st.button("Hiding", use_container_width=True):
        st.session_state['search_query'] = 'hiding scared'

with chip_col6:
    if st.button("Zoomies", use_container_width=True):
        st.session_state['search_query'] = 'zoomies 2am night'

with chip_col7:
    if st.button("First 24 hours", use_container_width=True):
        st.session_state['search_query'] = 'first day home'

with chip_col8:
    if st.button("Emergency", use_container_width=True):
        st.session_state['search_query'] = 'vet emergency'

st.markdown("---")

# Search filters
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    search_query = st.text_input(
        "Search for help",
        value=st.session_state.get('search_query', ''),
        placeholder="e.g., kitten won't eat, litter tray training, biting hands..."
    )
    if search_query:
        st.session_state['search_query'] = search_query

with col2:
    topic_filter = st.selectbox(
        "Topic",
        ["All Topics", "Behaviour", "Health", "Feeding", "Litter", "Play", "Sleep", "Emergency", "Onboarding", "Enrichment"]
    )

with col3:
    urgency_filter = st.selectbox(
        "Urgency",
        ["All", "Now", "Today", "Monitor"]
    )

# Perform search
if search_query:
    topic = None if topic_filter == "All Topics" else topic_filter
    urgency = None if urgency_filter == "All" else urgency_filter
    
    results = db.search_guides(search_query, topic=topic, urgency=urgency)
    
    st.markdown(f"### Found {len(results)} result(s)")
    
    if results:
        for guide in results:
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
                
                if st.button(f"Read guide", key=f"search_{guide.id}", use_container_width=True):
                    st.session_state['selected_guide'] = guide.id
                    st.switch_page("pages/guide_viewer.py")
                
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No guides found. Try different search terms or browse the library.")
        if st.button("📖 Browse Library"):
            st.switch_page("pages/2_library.py")
else:
    # Show all guides if no search
    st.markdown("### 💡 Browse All Guides")
    st.caption("Or use the search box above to find specific help")
    
    all_guides = db.get_all_guides()
    
    for guide in all_guides[:5]:  # Show first 5
        with st.container():
            st.markdown('<div class="guide-card">', unsafe_allow_html=True)
            
            if guide.urgency:
                urgency_class = f"urgency-{guide.urgency.lower()}"
                st.markdown(f'<span class="{urgency_class}">{guide.urgency}</span>', unsafe_allow_html=True)
            
            st.markdown(f"### {guide.title}")
            st.markdown(f"*{guide.summary}*")
            
            if guide.topics:
                topic_html = " ".join([f'<span class="topic-badge">{topic}</span>' for topic in guide.topics])
                st.markdown(topic_html, unsafe_allow_html=True)
            
            if st.button(f"Read guide", key=f"browse_{guide.id}", use_container_width=True):
                st.session_state['selected_guide'] = guide.id
                st.switch_page("pages/guide_viewer.py")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    if len(all_guides) > 5:
        st.caption(f"... and {len(all_guides) - 5} more guides")
        if st.button("📖 View All in Library"):
            st.switch_page("pages/2_library.py")
