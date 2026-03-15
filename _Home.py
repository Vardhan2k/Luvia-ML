import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Luvia ML", 
    page_icon="🌌", 
    layout="wide")

current_dir = Path(__file__).parent
logo_path = current_dir / "static" / "luvia-logo-large.png"

if logo_path.exists():
# 1. Use st.logo to guarantee it sits ABOVE the navigation menu
    st.logo(
        image=str(logo_path), 
        size = "large",
        link="https://www.linkedin.com/in/srivarsrihari/"
        )
else:
    st.sidebar.markdown("## :material/scatter_plot: **Luvia ML**")
    st.sidebar.caption("Forge your intelligence.")
    

# Router only - No text here!
pg = st.navigation([
    st.Page("pages/home_page.py", title="Home", icon=":material/home:"),
    st.Page("pages/exploration.py", title="Exploration", icon=":material/analytics:"),
    st.Page("pages/refinery.py", title="Refinery", icon=":material/architecture:"),
    st.Page("pages/forge.py", title="Forge", icon=":material/model_training:"),
    st.Page("pages/predict.py", title="Predict", icon=":material/online_prediction:"),
    st.Page("pages/credits.py", title="Credits", icon=":material/history_edu:"),
])

if 'df' not in st.session_state:
    st.session_state['df'] = None

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        
        /* Force solid white */
        background-color: #f0f0ec !important;
        opacity: 1 !important;

        color: #212121;
        text-align: center;
        font-family: "SpaceGrotesk";
        font-size: 12px;
        padding: 10px;
        
        /* Ensure the main app content doesn't bleed through or get cut off */
        .stApp {
        margin-bottom: 50px;
        }
        
    a {
        cursor: link !important;
    }
    </style>
    
    <div class="footer">
        © Built by SriVardhan SriHari | <a href="https://www.linkedin.com/in/srivarsrihari/" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)


pg.run()