"""Emergency page - when to call vet NOW (v2)."""
import streamlit as st
from database import KittenGuideDB

st.set_page_config(
    page_title="Emergency - How to Work a Cat",
    page_icon="🆘",
    layout="wide"
)

# V2 CSS for emergency styling
st.markdown("""
<style>
    .emergency-hero {
        background: linear-gradient(135deg, #E84040 0%, #b01010 100%);
        border-radius: 14px;
        padding: 1.8rem 2rem;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .emergency-hero h1 { font-size: 2.4rem; margin: 0; font-weight: 900; }
    .emergency-hero p  { margin: 0.5rem 0 0; font-size: 1.1rem; opacity: 0.92; }
    .warning-box {
        border: 3px solid #E84040;
        border-radius: 12px;
        padding: 1rem;
        background-color: #fff5f5;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
@st.cache_resource
def get_db():
    return KittenGuideDB()

db = get_db()

# Emergency header
st.markdown("""
<div class="emergency-hero">
  <h1>🔴 EMERGENCY GUIDE 🔴</h1>
  <p>When to call the vet <em>right now</em> — not in the morning, not after a Google — <strong>now</strong></p>
</div>
""", unsafe_allow_html=True)

# Get emergency guide
emergency_guide = db.get_guide("emergency-vet-now")

if emergency_guide:
    st.markdown(emergency_guide.markdown_body)
else:
    st.error("Emergency guide not found in database")

# Quick emergency contact section
st.markdown("---")
st.markdown("## 📞 Save These Numbers NOW")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Your Vet Details
    Save these in your phone right now:
    """)
    
    if 'vet_name' not in st.session_state:
        st.session_state['vet_name'] = ''
    if 'vet_phone' not in st.session_state:
        st.session_state['vet_phone'] = ''
    if 'vet_emergency_phone' not in st.session_state:
        st.session_state['vet_emergency_phone'] = ''
    
    vet_name = st.text_input("Vet practice name", value=st.session_state['vet_name'])
    vet_phone = st.text_input("Regular hours phone", value=st.session_state['vet_phone'])
    vet_emergency = st.text_input("Emergency/after hours phone", value=st.session_state['vet_emergency_phone'])
    
    if st.button("💾 Save my vet details"):
        st.session_state['vet_name'] = vet_name
        st.session_state['vet_phone'] = vet_phone
        st.session_state['vet_emergency_phone'] = vet_emergency
        st.success("✅ Saved! Now add them to your phone contacts too.")

with col2:
    st.markdown("""
    ### UK Emergency Resources
    
    **PDSA** (if you qualify)
    📞 0800 731 2502
    
    **Vets Now** (emergency provider)
    🌐 Google "Vets Now near me"
    
    **RSPCA advice line**
    📞 0300 1234 999
    (Not emergency vet, but can advise)
    
    **Poison helpline**
    📞 01202 509000
    (Animal PoisonLine - £30 fee)
    """)

# Quick decision tree
st.markdown("---")
st.markdown("## 🤔 Decision Tree: Is This an Emergency?")

with st.expander("My kitten won't eat or drink", expanded=False):
    st.markdown("""
    **How long?**
    - **Under 12 hours**: Monitor closely, try different foods
    - **12-24 hours no drinking**: Ring vet NOW
    - **24+ hours no eating**: Vet appointment TODAY
    - **Not drinking AND lethargic**: EMERGENCY - go to vet NOW
    """)

with st.expander("My kitten is vomiting", expanded=False):
    st.markdown("""
    **How many times?**
    - **Once or twice, still active**: Monitor, withhold food 2 hours, then small amounts
    - **More than twice in 24 hours**: Ring vet
    - **Blood in vomit**: EMERGENCY
    - **Vomiting AND lethargic**: EMERGENCY
    - **Projectile vomiting**: Ring vet NOW
    """)

with st.expander("My kitten has diarrhoea", expanded=False):
    st.markdown("""
    **Check severity:**
    - **Soft poo, still active**: Monitor, may be food change
    - **Watery diarrhoea**: Ring vet same day
    - **Blood in diarrhoea**: EMERGENCY
    - **Diarrhoea AND not drinking**: EMERGENCY
    - **Lasting 24+ hours**: Vet appointment needed
    """)

with st.expander("My kitten is breathing strangely", expanded=False):
    st.markdown("""
    **ANY breathing problems = EMERGENCY**
    - Panting (cats don't pant unless in distress)
    - Rapid breathing at rest
    - Open mouth breathing
    - Blue or pale gums
    - Wheezing or struggling
    
    🚨 GO TO VET IMMEDIATELY - DO NOT WAIT
    """)

with st.expander("My kitten can't urinate", expanded=False):
    st.markdown("""
    **🚨 BLOCKED BLADDER = LIFE THREATENING EMERGENCY**
    
    Signs:
    - Straining to wee with nothing coming out
    - Crying in litter tray
    - Going to tray repeatedly
    - Licking genital area excessively
    
    This can be FATAL within hours. GO TO VET NOW.
    """)

# Reminder
st.markdown("---")
st.warning("""
**Remember**: Vets want you to call. You're not wasting their time. 
Kittens can deteriorate very quickly. When in doubt, ring. Always.
""")
