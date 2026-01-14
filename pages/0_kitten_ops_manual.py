"""Kitten Ops Manual - onboarding flow for new kitten owners."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Kitten Ops Manual - How to Work a Cat",
    page_icon="📋",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .step-card {
        border: 2px solid #3498db;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #f0f8ff;
    }
    .step-complete {
        border-color: #27ae60;
        background-color: #d4edda;
    }
    .step-number {
        background-color: #3498db;
        color: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
        margin-right: 1rem;
    }
    .progress-bar {
        background-color: #e0e0e0;
        border-radius: 10px;
        height: 20px;
        margin: 1rem 0;
    }
    .progress-fill {
        background-color: #27ae60;
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
@st.cache_resource
def get_db():
    return KittenGuideDB()

db = get_db()

st.title("📋 Kitten Ops Manual")
st.markdown("### Your step-by-step guide to bringing home a kitten")

# Initialize progress in session state
if 'ops_manual_progress' not in st.session_state:
    st.session_state['ops_manual_progress'] = set()

# Define the onboarding steps
steps = [
    {
        'id': 'step1',
        'title': 'Before bringing kitten home',
        'guide_id': 'first-24-hours',
        'description': 'Set up safe room, buy supplies, kitten-proof house',
        'checklist': [
            'Choose a "base camp" room (bedroom or bathroom)',
            'Buy litter tray, litter, food bowls, kitten food',
            'Remove toxic plants (lilies, etc.)',
            'Hide cables and small objects',
            'Set up bed/hideaway spots'
        ]
    },
    {
        'id': 'step2',
        'title': 'First 24 hours: tiny flatmate protocol',
        'guide_id': 'first-24-hours',
        'description': 'Let kitten settle, establish base camp, monitor eating/drinking',
        'checklist': [
            'Place kitten in safe room',
            'Show them litter tray',
            'Leave food and water',
            'Sit quietly, let them approach',
            'No visitors for 48 hours'
        ]
    },
    {
        'id': 'step3',
        'title': 'Litter tray setup',
        'guide_id': 'litter-tray-basics',
        'description': 'Master the shared bathroom protocol',
        'checklist': [
            'Position tray away from food',
            'Use unscented clumping litter',
            'Show kitten the tray location',
            'Scoop twice daily',
            'Praise when they use it'
        ]
    },
    {
        'id': 'step4',
        'title': 'Feeding routine',
        'guide_id': 'not-eating',
        'description': 'Establish meal times and monitor appetite',
        'checklist': [
            'Feed kitten food (not adult cat food)',
            '3-4 small meals per day for kittens under 6 months',
            'Fresh water always available',
            'Clean bowls daily',
            'Monitor eating - if refuses food 24hrs, call vet'
        ]
    },
    {
        'id': 'step5',
        'title': 'Play & boundaries',
        'guide_id': 'biting-hands',
        'description': 'Teach good play behaviour from day one',
        'checklist': [
            'Use wand toys, not hands',
            'Stop play if they bite',
            '2x 15-min play sessions daily',
            'Tire them out before bed',
            'Never encourage hand biting'
        ]
    },
    {
        'id': 'step6',
        'title': 'Scratching solutions',
        'guide_id': 'scratching-furniture',
        'description': 'Issue legal scratching licence',
        'checklist': [
            'Get sturdy scratching post',
            'Place near where they scratch',
            'Try different textures (sisal, cardboard)',
            'Praise when they use it',
            'Trim claws every 2-3 weeks'
        ]
    },
    {
        'id': 'step7',
        'title': 'Sleep schedule',
        'guide_id': 'zoomies-2am',
        'description': 'Negotiate energy budget and bedtime',
        'checklist': [
            'Play before YOUR bedtime',
            'Small meal before bed',
            'Ignore nighttime zoomies',
            'Keep bedroom door shut',
            'Be consistent - takes 2-3 weeks'
        ]
    },
    {
        'id': 'step8',
        'title': 'Health basics',
        'guide_id': 'emergency-vet-now',
        'description': 'Know when to worry and when to call vet',
        'checklist': [
            'Save vet number in phone',
            'Know emergency vet location',
            'Monitor eating, drinking, toileting daily',
            'Check for fleas weekly',
            'Read emergency guide'
        ]
    },
    {
        'id': 'step9',
        'title': 'Gradual house expansion',
        'guide_id': None,
        'description': 'Let kitten explore more rooms once confident',
        'checklist': [
            'Wait until kitten is eating, playing, using tray reliably',
            'Open one new room at a time',
            'Supervise exploration',
            'Keep base camp available',
            'Don\'t rush - some kittens take weeks'
        ]
    },
    {
        'id': 'step10',
        'title': 'Socialisation',
        'guide_id': None,
        'description': 'Introduce to people, sounds, experiences',
        'checklist': [
            'Once settled (after 1 week), gradual introductions',
            'Short, positive visitor sessions',
            'Gentle handling daily',
            'Expose to household sounds',
            'Always let them retreat to safe room'
        ]
    }
]

# Calculate progress
completed_steps = len(st.session_state['ops_manual_progress'])
total_steps = len(steps)
progress_percentage = (completed_steps / total_steps) * 100

# Progress bar
st.markdown(f"### Progress: {completed_steps}/{total_steps} steps completed")
st.markdown(f"""
<div class="progress-bar">
    <div class="progress-fill" style="width: {progress_percentage}%"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Display steps
for idx, step in enumerate(steps, 1):
    step_id = step['id']
    is_complete = step_id in st.session_state['ops_manual_progress']
    card_class = "step-card step-complete" if is_complete else "step-card"
    
    with st.container():
        st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f'<span class="step-number">{idx}</span>', unsafe_allow_html=True)
            st.markdown(f"### {step['title']}", unsafe_allow_html=False)
            st.markdown(f"*{step['description']}*")
            
            # Checklist
            with st.expander("📝 Checklist", expanded=not is_complete):
                for item in step['checklist']:
                    st.markdown(f"- {item}")
            
            # Link to guide if available
            if step['guide_id']:
                if st.button(f"📖 Read full guide", key=f"guide_{step_id}", use_container_width=True):
                    st.session_state['selected_guide'] = step['guide_id']
                    st.switch_page("pages/guide_viewer.py")
        
        with col2:
            if is_complete:
                if st.button("✅ Done", key=f"toggle_{step_id}", use_container_width=True):
                    st.session_state['ops_manual_progress'].remove(step_id)
                    st.rerun()
            else:
                if st.button("Mark done", key=f"toggle_{step_id}", use_container_width=True):
                    st.session_state['ops_manual_progress'].add(step_id)
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Completion message
if completed_steps == total_steps:
    st.balloons()
    st.success("🎉 Congratulations! You've completed the Kitten Ops Manual! Your kitten is lucky to have such a prepared human.")

# Footer tips
st.markdown("---")
st.info("""
💡 **Tips:**
- Work through these steps at your own pace
- It's OK to jump around based on your needs
- The first 2 weeks are the hardest - it gets easier!
- When in doubt, check the emergency guide or ring your vet
""")
