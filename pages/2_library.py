"""Library page - browse guides by topic."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Library - How To Work A Cat",
    page_icon="📖",
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

st.title("📖 Guide Library")
st.markdown("Browse all kitten-care guides organised by topic")

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

# Topic overview
with st.sidebar:
    st.markdown("### 📚 Topics Overview")
    if st.button("All Topics", use_container_width=True):
        st.session_state["library_selected_topic"] = "All Topics"
        st.rerun()
    for topic in sorted(topics.keys()):
        count = len(topics[topic])
        if st.button(f"{topic} ({count})", key=f"sidebar_{topic}", use_container_width=True):
            st.session_state["library_selected_topic"] = topic
            st.rerun()
