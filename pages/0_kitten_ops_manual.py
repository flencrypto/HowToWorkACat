"""Kitten Ops Manual - onboarding flow for new kitten owners (v2)."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Kitten Ops Manual - How to Work a Cat",
    page_icon="📋",
    layout="wide"
)

# V2 CSS
st.markdown("""
<style>
    :root {
        --cat-orange: #F07A33;
        --cat-green:  #5BAD8B;
        --cat-purple: #7B5EA7;
        --cat-red:    #E84040;
    }
    .ops-hero {
        background: linear-gradient(135deg, #3AAFA9 0%, #7B5EA7 100%);
        border-radius: 14px;
        padding: 1.5rem 2rem;
        color: white;
        margin-bottom: 1.2rem;
    }
    .ops-hero h2 { margin: 0; font-size: 2rem; font-weight: 900; }
    .ops-hero p  { margin: 0.3rem 0 0; opacity: 0.9; }

    .step-card {
        border: 2px solid #e0d0f8;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        margin: 0.6rem 0;
        background-color: #FFFFFF;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .step-complete {
        border-color: var(--cat-green);
        background-color: #f0fbf6;
    }
    .step-number {
        background: linear-gradient(135deg, var(--cat-orange), var(--cat-purple));
        color: white;
        border-radius: 50%;
        width: 38px;
        height: 38px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.1rem;
        margin-right: 0.8rem;
        flex-shrink: 0;
    }
    .step-number-done {
        background: var(--cat-green);
    }
    .xp-badge {
        display: inline-block;
        background: linear-gradient(90deg, var(--cat-orange), var(--cat-purple));
        color: white;
        padding: 0.2rem 0.65rem;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    .rank-banner {
        background: linear-gradient(90deg, #fff8e7, #ffe0b2);
        border-left: 5px solid var(--cat-orange);
        border-radius: 10px;
        padding: 0.8rem 1.2rem;
        margin: 1rem 0;
        font-size: 1.05rem;
    }
    .progress-outer {
        background: #e0e0e0;
        border-radius: 20px;
        height: 24px;
        overflow: hidden;
        margin: 0.6rem 0;
    }
    .progress-inner {
        height: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, var(--cat-green), var(--cat-orange));
        transition: width 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
@st.cache_resource
def get_db():
    return KittenGuideDB()

db = get_db()

# ── Rank system ────────────────────────────────────────────────────────────────
RANKS = [
    (0,  "🥚 Total Beginner",         "You've read the title. Respect."),
    (2,  "🐣 Nervous New Parent",      "Two steps in. The kitten is alive. Progress!"),
    (4,  "😬 Cautiously Optimistic",   "Four steps done. The litter tray situation is improving."),
    (6,  "🙂 Getting the Hang of It",  "Six steps complete. Your kitten tolerates you now."),
    (8,  "😎 Seasoned Kitten Wrangler","Eight steps! You can now locate the kitten in under 3 minutes."),
    (10, "🏆 Certified Cat Butler",    "All 10 steps! Your kitten has accepted you as staff."),
]

def get_rank(done: int) -> tuple:
    for threshold, label, flavour in reversed(RANKS):
        if done >= threshold:
            return label, flavour
    return RANKS[0][1], RANKS[0][2]

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ops-hero">
  <h2>📋 Kitten Ops Manual</h2>
  <p>Your step-by-step guide to bringing home a kitten — earn XP as you go</p>
</div>
""", unsafe_allow_html=True)

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
            'Buy [litter tray](https://amzn.to/4pAAnEJ), [litter](https://amzn.to/49vJCBz), food bowls, [kitten food](https://amzn.to/49TqoFQ), and a sturdy cat carrier',
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
xp = completed_steps * 100

rank_label, rank_flavour = get_rank(completed_steps)

# Rank banner
st.markdown(f"""
<div class="rank-banner">
  🎮 <strong>Your Rank:</strong> {rank_label}
  <span class="xp-badge">⚡ {xp} XP</span><br>
  <small style="color:#555">{rank_flavour}</small>
</div>
""", unsafe_allow_html=True)

# Progress bar
st.markdown(f"**Progress: {completed_steps}/{total_steps} steps completed**")
st.markdown(f"""
<div class="progress-outer">
  <div class="progress-inner" style="width:{progress_percentage}%"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Display steps
for idx, step in enumerate(steps, 1):
    step_id = step['id']
    is_complete = step_id in st.session_state['ops_manual_progress']
    card_class = "step-card step-complete" if is_complete else "step-card"
    num_class = "step-number step-number-done" if is_complete else "step-number"
    step_display = "✅" if is_complete else str(idx)
    
    with st.container():
        st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f'<span class="{num_class}">{step_display}</span>', unsafe_allow_html=True)
            title_suffix = ' <span class="xp-badge">+100 XP</span>' if is_complete else ""
            st.markdown(f"### {step['title']}{title_suffix}", unsafe_allow_html=True)
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
