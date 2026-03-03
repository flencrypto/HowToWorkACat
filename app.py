import streamlit as st
from database import KittenGuideDB
from content_loader import load_sample_content
import os
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="How to Work a Cat 🐱 v2",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# V2 CSS — vibrant, playful, warm palette
st.markdown("""
<style>
    /* ---- Global palette ---- */
    :root {
        --cat-orange:  #F07A33;
        --cat-teal:    #3AAFA9;
        --cat-purple:  #7B5EA7;
        --cat-red:     #E84040;
        --cat-yellow:  #F5C842;
        --cat-green:   #5BAD8B;
        --cat-dark:    #2C2C3E;
        --cat-light:   #FDF7F2;
    }

    /* ---- Hero header ---- */
    .v2-hero {
        background: linear-gradient(135deg, var(--cat-purple) 0%, var(--cat-orange) 100%);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        color: white;
        margin-bottom: 1.5rem;
    }
    .v2-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 900; letter-spacing: -1px; }
    .v2-hero p  { font-size: 1.15rem; margin: 0.4rem 0 0; opacity: 0.92; }

    /* ---- Wisdom card ---- */
    .wisdom-card {
        background: linear-gradient(120deg, #fff9f0 0%, #ffe8cc 100%);
        border-left: 5px solid var(--cat-orange);
        border-radius: 10px;
        padding: 1rem 1.4rem;
        margin-bottom: 1.2rem;
        font-style: italic;
        font-size: 1.05rem;
        color: #3a2a00;
    }

    /* ---- Chaos meter ---- */
    .chaos-bar-outer {
        background: #e0e0e0;
        border-radius: 20px;
        height: 22px;
        overflow: hidden;
        margin: 0.4rem 0 0.2rem;
    }
    .chaos-bar-inner {
        height: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, var(--cat-green), var(--cat-yellow), var(--cat-orange), var(--cat-red));
        transition: width 0.5s ease;
    }

    /* ---- Panic buttons ---- */
    .panic-label {
        font-size: 0.78rem;
        color: #666;
        text-align: center;
        margin-top: 2px;
    }

    /* ---- Guide cards ---- */
    .guide-card-v2 {
        border: none;
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        margin: 0.6rem 0;
        background: #fff;
        box-shadow: 0 3px 12px rgba(0,0,0,0.08);
        transition: box-shadow 0.2s;
    }
    .guide-card-v2:hover { box-shadow: 0 6px 20px rgba(0,0,0,0.14); }

    /* ---- Urgency badges ---- */
    .urgency-now {
        background-color: var(--cat-red);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.3rem;
    }
    .urgency-today {
        background-color: var(--cat-orange);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.3rem;
    }
    .urgency-monitor {
        background-color: var(--cat-green);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.3rem;
    }

    /* ---- Topic badges ---- */
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

    /* ---- Stats row ---- */
    .stat-box {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    }
    .stat-number { font-size: 2rem; font-weight: 900; color: var(--cat-purple); }
    .stat-label  { font-size: 0.82rem; color: #666; }

    /* ---- Nav cards ---- */
    .nav-card {
        border-radius: 12px;
        padding: 0.9rem 1rem;
        margin: 0.3rem 0;
        background: var(--cat-light);
        border-left: 4px solid var(--cat-orange);
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Cat wisdom pool ────────────────────────────────────────────────────────────
CAT_WISDOMS = [
    "🐾 *\"A kitten that hides under the bed is not plotting your downfall — they're just terrified. Give it 48 hours.\"*",
    "🐾 *\"Your kitten does not hate you. They hate the new smell of everything, including you. This is temporary.\"*",
    "🐾 *\"Zoomies at 2am are not a personal attack. They are a feature, not a bug. Play before bed to patch it.\"*",
    "🐾 *\"The litter tray is a privilege, not a right. Keep it clean or accept the consequences on your duvet.\"*",
    "🐾 *\"Hands are not toys. Hands are sacred. Your future self will thank you for establishing this rule now.\"*",
    "🐾 *\"Cats do not meow at each other. They only meow at humans. Congratulations — you have been accepted.\"*",
    "🐾 *\"If your kitten brings you a toy, they are teaching you to hunt. Be grateful. Pretend to be impressed.\"*",
    "🐾 *\"Slow blinking back at a cat is the feline equivalent of a firm handshake and a genuine smile.\"*",
    "🐾 *\"A purring kitten on your laptop is not an inconvenience. It is a privilege. Adjust your posture.\"*",
    "🐾 *\"The cardboard box you were going to recycle is now a palace. Accept this. Order more things online.\"*",
    "🐾 *\"Kittens sleep 16 hours a day. Humans average 7. They are clearly doing something right.\"*",
    "🐾 *\"If a kitten shows you their belly, it is a test of your self-control. You will almost certainly fail.\"*",
]

# ── ASCII cat art ──────────────────────────────────────────────────────────────
CAT_ART = r"""
   /\_____/\
  /  o   o  \
 ( ==  ^  == )
  )         (
 (           )
( (  )   (  ) )
(__(__)___(__)__)
"""

# ── Chaos level labels ─────────────────────────────────────────────────────────
def chaos_level(manual_steps_done: int, bookmarks: int, total_steps: int = 10) -> tuple:
    """Return (pct, label, emoji) describing current kitten chaos level."""
    score = max(0, total_steps - manual_steps_done)
    pct = int((score / total_steps) * 100)
    if pct >= 80:
        return pct, "MAXIMUM CHAOS", "🔥"
    elif pct >= 60:
        return pct, "Moderate mayhem", "😅"
    elif pct >= 40:
        return pct, "Manageable madness", "😬"
    elif pct >= 20:
        return pct, "Mostly civilised", "😊"
    else:
        return pct, "Zen cat parent", "🧘"

# ── Init database ──────────────────────────────────────────────────────────────
@st.cache_resource
def init_database():
    """Initialise database and load sample content if needed."""
    db_path = "kitten_guide.db"
    db = KittenGuideDB(db_path)
    if len(db.get_all_guides()) == 0:
        load_sample_content(db)
    return db

db = init_database()

# ──────────────────────────────────────────────────────────────────────────────
# HERO HEADER
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="v2-hero">
    <h1>🐱 How to Work a Cat &nbsp;<sup style="font-size:1.1rem;opacity:0.8">v2</sup></h1>
    <p>The offline-first survival guide for humans newly owned by a kitten 🏴󠁧󠁢󠁥󠁮󠁧󠁿</p>
</div>
""", unsafe_allow_html=True)

# Daily cat wisdom (rotates based on day-of-year + year so it varies each year)
_now = datetime.now()
wisdom_index = (_now.timetuple().tm_yday + _now.year) % len(CAT_WISDOMS)
st.markdown(f'<div class="wisdom-card">💬 <strong>Cat Wisdom of the Day</strong><br>{CAT_WISDOMS[wisdom_index]}</div>',
            unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# STATS ROW
# ──────────────────────────────────────────────────────────────────────────────
all_guides = db.get_all_guides()
bookmarked = db.get_bookmarked_guides()
manual_done = len(st.session_state.get('ops_manual_progress', set()))
guides_read = len(st.session_state.get('guides_read', set()))

stat_c1, stat_c2, stat_c3, stat_c4 = st.columns(4)
with stat_c1:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{len(all_guides)}</div>'
                f'<div class="stat-label">📚 guides available</div></div>', unsafe_allow_html=True)
with stat_c2:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{guides_read}</div>'
                f'<div class="stat-label">👁️ guides read</div></div>', unsafe_allow_html=True)
with stat_c3:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{len(bookmarked)}</div>'
                f'<div class="stat-label">⭐ saved</div></div>', unsafe_allow_html=True)
with stat_c4:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{manual_done}/10</div>'
                f'<div class="stat-label">✅ ops steps done</div></div>', unsafe_allow_html=True)

st.markdown("")

# ──────────────────────────────────────────────────────────────────────────────
# CHAOS LEVEL METER
# ──────────────────────────────────────────────────────────────────────────────
chaos_pct, chaos_label, chaos_emoji = chaos_level(manual_done, len(bookmarked))
st.markdown(f"#### {chaos_emoji} Current Kitten Chaos Level: **{chaos_label}**")
st.markdown(f"""
<div class="chaos-bar-outer">
  <div class="chaos-bar-inner" style="width:{chaos_pct}%"></div>
</div>
<small style="color:#888">Complete more steps in the Kitten Ops Manual to reduce chaos. Probably.</small>
""", unsafe_allow_html=True)

st.markdown("---")

# ──────────────────────────────────────────────────────────────────────────────
# PANIC BUTTONS
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("#### 🆘 Panic Mode — tap what's going wrong *right now*")

panic_col1, panic_col2, panic_col3, panic_col4 = st.columns(4)

with panic_col1:
    if st.button("😿 Not eating", use_container_width=True, help="Kitten gone on hunger strike?"):
        st.session_state['selected_guide'] = 'not-eating'
        st.switch_page("pages/guide_viewer.py")
    st.markdown('<div class="panic-label">Gone on hunger strike</div>', unsafe_allow_html=True)

with panic_col2:
    if st.button("🚽 Litter disasters", use_container_width=True, help="Wee on your duvet again?"):
        st.session_state['selected_guide'] = 'litter-tray-basics'
        st.switch_page("pages/guide_viewer.py")
    st.markdown('<div class="panic-label">Missed the tray (again)</div>', unsafe_allow_html=True)

with panic_col3:
    if st.button("😾 Biting/scratching", use_container_width=True, help="Tiny murder mittens activated?"):
        st.session_state['selected_guide'] = 'biting-hands'
        st.switch_page("pages/guide_viewer.py")
    st.markdown('<div class="panic-label">Murder mittens activated</div>', unsafe_allow_html=True)

with panic_col4:
    if st.button("🏃 Zoomies at 3am", use_container_width=True, help="Ceiling cat is home"):
        st.session_state['selected_guide'] = 'zoomies-2am'
        st.switch_page("pages/guide_viewer.py")
    st.markdown('<div class="panic-label">Ceiling cat is home</div>', unsafe_allow_html=True)

# Emergency expander
with st.expander("🔴 **WHEN TO CALL VET NOW** — expand for red flags", expanded=False):
    emergency_guide = db.get_guide("emergency-vet-now")
    if emergency_guide:
        st.markdown(emergency_guide.markdown_body)

st.markdown("---")

# ──────────────────────────────────────────────────────────────────────────────
# FEATURED GUIDES
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("### ✨ Start Here — the essentials")

featured_ids = ["first-24-hours", "litter-tray-basics", "emergency-vet-now"]
featured_guides = [db.get_guide(gid) for gid in featured_ids if db.get_guide(gid)]

feat_cols = st.columns(len(featured_guides))
for col, guide in zip(feat_cols, featured_guides):
    with col:
        urgency_html = ""
        if guide.urgency:
            urgency_class = f"urgency-{guide.urgency.lower()}"
            urgency_html = f'<span class="{urgency_class}">{guide.urgency}</span><br>'

        topic_html = " ".join([f'<span class="topic-badge">{t}</span>' for t in guide.topics])

        st.markdown(f"""
<div class="guide-card-v2">
{urgency_html}
<strong style="font-size:1rem">{guide.title}</strong><br>
<small style="color:#555">{guide.summary}</small><br><br>
{topic_html}
</div>
""", unsafe_allow_html=True)
        if st.button("Read guide →", key=f"feat_{guide.id}", use_container_width=True):
            st.session_state['selected_guide'] = guide.id
            if 'guides_read' not in st.session_state:
                st.session_state['guides_read'] = set()
            st.session_state['guides_read'].add(guide.id)
            st.switch_page("pages/guide_viewer.py")

st.markdown("---")

# ──────────────────────────────────────────────────────────────────────────────
# NAVIGATION GUIDE
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("### 🗺️ Where to next?")

nav_items = [
    ("📋", "Kitten Ops Manual", "Step-by-step onboarding — start here if the kitten arrived today", "pages/0_kitten_ops_manual.py"),
    ("🔍", "Search",            "Find help for a specific crisis at 2am",                          "pages/1_search.py"),
    ("📖", "Library",           "Browse every guide by topic — no panic required",                 "pages/2_library.py"),
    ("⭐", "Saved",             "Your bookmarked guides — quick access in an emergency",            "pages/3_saved.py"),
    ("🆘", "Emergency",        "When to ring the vet RIGHT NOW — keep this bookmarked",            "pages/4_emergency.py"),
]

nav_c1, nav_c2 = st.columns(2)
for i, (icon, name, desc, page) in enumerate(nav_items):
    col = nav_c1 if i % 2 == 0 else nav_c2
    with col:
        st.markdown(f'<div class="nav-card">{icon} <strong>{name}</strong><br>'
                    f'<small style="color:#555">{desc}</small></div>', unsafe_allow_html=True)
        if st.button(f"Go to {name}", key=f"nav_{name}", use_container_width=True):
            st.switch_page(page)

# ──────────────────────────────────────────────────────────────────────────────
# FUN RANDOM CAT FACT SIDEBAR
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🐱 Cat Fact")
    fun_facts = [
        "Cats can make over 100 different sounds. Dogs can only make about 10.",
        "A group of kittens is called a *kindle*. A group of adult cats is a *clowder*.",
        "Cats spend 70% of their lives asleep. They are basically furry philosophers.",
        "Your cat's nose print is unique — like a human fingerprint, but cuter.",
        "Cats can't taste sweetness. They have no sweet taste receptors at all.",
        "The technical term for a cat's hairball is a *trichobezoar*. It sounds more impressive than it is.",
        "Cats always land on their feet due to a reflex called the *righting reflex* — but please don't test this.",
        "Ancient Egyptians shaved their eyebrows in mourning when their cat died.",
        "A cat called Stubbs was the mayor of Talkeetna, Alaska for 20 years.",
        "Cats have 32 muscles in each ear. You have 6. They can hear you opening a crisp packet from two floors up.",
    ]
    _fact_now = datetime.now()
    fact_index = (_fact_now.timetuple().tm_yday + _fact_now.hour) % len(fun_facts)
    st.info(fun_facts[fact_index])
    st.markdown("<small>*Updates hourly*</small>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<small style="color:#999">
<strong>Disclaimer:</strong> This app provides general guidance based on RSPCA and Cats Protection advice.
It is not a substitute for professional veterinary advice. When in doubt, always consult your vet.<br>
<em>How to Work a Cat v2 — because kittens don't come with a manual, so we wrote one.</em>
</small>
""", unsafe_allow_html=True)
