import streamlit as st

st.set_page_config(page_title="Luvia ML - Credits", page_icon="📜")

# --- HIDE STREAMLIT BRANDING & STATUS ---
st.markdown("""
    <style>
        /* Hide the top-right hamburger menu and the footer "Made with Streamlit" */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Hide the "Running..." status indicator at the top right */
        div[data-testid="stStatusWidget"] {
            visibility: hidden !important;
            display: none !important;
        }
        
        /* Optional: Removes the top padding to make the UI tighter */
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📜 The Librarians")
st.write("Luvia ML is built upon a foundation of world-class open-source software. I extend my deepest gratitude to the creators and maintainers of these projects.")

st.divider()

# --- 🧱 CORE ARCHITECTURE ---
st.subheader("🧱 Core Architecture")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### **PyCaret**
    *The Low-Code ML Library*
    - **Original Creator:** Moez Ali
    - **Role:** The heavy-lifting engine for the Refinery and the Forge.
    - [GitHub](https://github.com/pycaret/pycaret)
    """)

with col2:
    st.markdown("""
    #### **Streamlit**
    *The UI Framework*
    - **Founders:** Adrien Treuille, Thiago Teixeira, Amanda Kelly
    - **Role:** Providing the fluid, interactive interface.
    - [GitHub](https://github.com/streamlit/streamlit)
    """)

st.divider()

# --- 🔍 DATA UNDERSTANDING ---
st.subheader("🔍 Data Understanding")
col_eda1, col_eda2 = st.columns([2, 1])

with col_eda1:
    st.markdown("""
    #### **ydata-profiling** (formerly pandas-profiling)
    *Automated Exploratory Data Analysis*
    - **Inception:** Jos Polfliet (2016)
    - **Maintained by:** YData Labs Inc.
    - **Role:** Powering 'The Oracle' with comprehensive data audits and statistical summaries.
    - [GitHub](https://github.com/ydataai/ydata-profiling)
    """)
    
with col_eda2:
    st.info("**Fun Fact:** It started because Jos was bored of doing the same manual EDA over and over. Now it saves millions of hours for data scientists globally.")

st.divider()

# --- 🧠 THE ECOSYSTEM ---
st.subheader("🧠 The Ecosystem")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**Scikit-Learn**")
    st.caption("Standard-bearer for robust ML algorithms.")

with c2:
    st.markdown("**Pandas**")
    st.caption("The ultimate tool for high-performance data structures.")

with c3:
    st.markdown("**NumPy**")
    st.caption("Fundamental package for scientific computing.")

st.divider()

# --- YOUR PERSONAL CREDIT ---
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        <p style='font-size: 0.9rem; color: #888;'>
            Luvia ML | Version 1.0 <br>
            Developed by <b>SriVardhan SriHari</b> | <a href="https://www.linkedin.com/in/srivarsrihari/" target="_blank">LinkedIn</a>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)