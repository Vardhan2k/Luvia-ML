import streamlit as st
from pathlib import Path


# Router only - No text here!
pg = st.navigation([
    st.Page("pages/home_page.py", title="Home", icon=":material/home:"),
    st.Page("pages/exploration.py", title="Exploration", icon=":material/analytics:"),
    st.Page("pages/refinery.py", title="Refinery", icon=":material/architecture:"),
    st.Page("pages/forge.py", title="Forge", icon=":material/model_training:"),
    st.Page("pages/predict.py", title="Predict", icon=":material/online_prediction:"),
    st.Page("pages/credits.py", title="Credits", icon=":material/history_edu:"),
])


# 1. Find the logo path FIRST (Standard Python, not a Streamlit command)
current_dir = Path(__file__).parent
logo_path = current_dir / "static" / "luvia-logo-large.png"

st.set_page_config(
    page_title="Luvia ML", 
    page_icon=str(logo_path) if logo_path.exists() else ":material/scatter_plot:", 
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
    
# --- HIDE STREAMLIT BRANDING & STATUS ---
st.markdown("""
    <style>
        /* Hide the top-right hamburger menu and the footer "Made with Streamlit" */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Hide the "Running..." status indicator at the top right */
        div[data-testid="stStatusWidget"] {
            visibility: hidden;
            display: none;
        }
        
        /* Optional: Removes the top padding to make the UI tighter */
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- ESCAPE HATCH TO MAIN PORTFOLIO (Themed) ---
st.sidebar.markdown(
    """
    <style>
        .portfolio-back-btn {
            display: inline-block; /* Keeps it compact, not full width */
            padding: 0.3rem 0.7rem;
            background-color: #fafafa; /* Removes the heavy black box */
            color: #09090b !important; /* Subtle zinc text */
            border-radius: 8px; /* Smooth pill shape */
            font-weight: 500;
            font-size: 0.75rem;
            border: 1px solid #d3d2ca; /* Subtle border */
            text-decoration: none !important;
            transition: all 0.2s ease;
            margin-bottom: 0.5rem;
            font-family: 'Geist Mono', monospace; /* Techy vibe */
        }
        .portfolio-back-btn:hover {
            color: #10b981 !important; /* Portfolio Emerald Green */
            border-color: #10b981;
            background-color: rgba(16, 185, 129, 0.1); /* Very slight green glow */
        }
    </style>
    
    <div style="text-align: left; padding-left: 0.5rem;">
        <a href="https://scriptedbysri.dev" target="_self" class="portfolio-back-btn">
            ← ScriptedBySri.dev
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

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