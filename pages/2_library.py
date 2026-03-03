"""Library page - browse guides by topic (v2)."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Library - How to Work a Cat",
    page_icon="📖",
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
    .library-hero {
        background: linear-gradient(135deg, #5BAD8B 0%, #3AAFA9 100%);
        border-radius: 14px;
        padding: 1.4rem 2rem;
        color: white;
        margin-bottom: 1.2rem;
    }
    .library-hero h2 { margin: 0; font-size: 2rem; font-weight: 900; }
    .library-hero p  { margin: 0.3rem 0 0; opacity: 0.9; }
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
<div class="library-hero">
  <h2>📖 Guide Library</h2>
  <p>Every guide, organised by topic — for the calm moments between crises</p>
</div>
""", unsafe_allow_html=True)

# Get all guides
all_guides = db.get_all_guides()

# Manage topic selection in session state
topic_options = ["All Topics"]
# Organize by topic
topics = {}
for guide in all_guides:
    for topic in guide.topics:
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(guide)
        if topic not in topic_options:
            topic_options.append(topic)
topic_options = topic_options[:1] + sorted(topic_options[1:])

if "library_selected_topic" not in st.session_state:
    st.session_state["library_selected_topic"] = "All Topics"

# Topic filter
st.markdown("### Filter by Topic")
selected_topic = st.selectbox(
    "Choose a topic",
    topic_options,
    index=topic_options.index(st.session_state["library_selected_topic"]),
    key="library_selected_topic"
)

if selected_topic == "All Topics":
    guides_to_show = all_guides
else:
    guides_to_show = topics[selected_topic]

st.markdown(f"### Showing {len(guides_to_show)} guide(s)")

# Display guides
for guide in sorted(guides_to_show, key=lambda g: g.title):
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
        
        # Age range
        if guide.age_min_weeks is not None or guide.age_max_weeks is not None:
            age_min = guide.age_min_weeks or 0
            age_max = guide.age_max_weeks or "any age"
            st.caption(f"📅 {age_min}-{age_max} weeks")
        
        # Analogy preview
        if guide.analogy_cards:
            st.caption(f"💡 {guide.analogy_cards[0]}")
        
        if st.button(f"Read guide", key=f"lib_{guide.id}", use_container_width=True):
            st.session_state['selected_guide'] = guide.id
            st.switch_page("pages/guide_viewer.py")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Topic overview in sidebar (display only, filtering handled by selectbox above)
with st.sidebar:
    st.markdown("### 📚 Topics Overview")
    st.markdown(f"**All Topics** ({len(all_guides)} guides)")
    st.markdown("---")
    for topic in sorted(topics.keys()):
        count = len(topics[topic])
        st.markdown(f"**{topic}** ({count} guides)")
