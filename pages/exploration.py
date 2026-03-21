import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
# from streamlit_ydata_profiling import st_profile_report
import streamlit.components.v1 as components

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

st.title("🔍 Step 1: The Oracle (EDA)")

uploaded_file = st.file_uploader("Upload your Dataset", type="csv")

if uploaded_file is not None or st.session_state.get('df') is not None:
    # Only read the CSV if it's a fresh upload
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df 
    else:
        # Otherwise, load it from memory
        df = st.session_state['df']
    
    st.success("Data Uploaded Successfully!")
    
    with st.expander("View Raw Data"):
        st.dataframe(df.head(10), use_container_width=True)
    
    st.divider()
    
    # 2. Automated Report
    st.subheader("📊 Automated Analysis Report")
    
    # Use a spinner so the user knows the app hasn't crashed
    with st.spinner("The Oracle is analyzing your data..."):
        profile = ProfileReport(df, config_file="y_data_config.yaml")
        # st_profile_report(profile)
        report_html = profile.to_html()
        # 2. Prepare the CSS Injection
        # IMPORTANT: Use the exact URL mapping Streamlit uses for static files
        font_url = "app/static/SpaceGrotesk-VariableFont_wght.ttf"
        
        inject_css = f"""
        <style>
            @font-face {{
                font-family: 'SpaceGrotesk';
                src: url('app/static/SpaceGrotesk-VariableFont_wght.ttf') format('truetype');
            }}
            
            /* Remove the Navigation Bar and its container */
            .navbar, nav, .nav, .navbar-fixed-top {{
                display: none !important;
            }}

            /* Apply font to everything but keep default sizes */
            html, body, div, p, span, h1, h2, h3, h4, table, td, th {{
                font-family: 'SpaceGrotesk', sans-serif !important;
            }}

            /* Fix the "Too Big" font in the Overview/Stats tables */
            table, td, th, .stats, .dl-horizontal {{
                font-size: 14px !important;
            }}
            
            /* Make column labels even smaller and cleaner */
            th {{
                font-weight: 600 !important;
                font-size: 13px !important;
            }}

            /* Keep headers appropriately sized */
            h1 {{ font-size: 24px !important; }}
            h2 {{ font-size: 20px !important; }}
            h3 {{ font-size: 18px !important; }}

            /* Transparency & Theme matching */
            body, .container-fluid, .wrapper {{
                background-color: transparent !important;
            }}
            
            .card {{
                background-color: #ffffff99 !important;
                border: none !important;
                box-shadow: none !important;
            }}
            /* Remove any internal scrolling from the report itself */
            html, body {{
                overflow: visible !important;
                height: auto !important;
            }}
            
            /* Ensure the container takes up the full width of the Streamlit page */
            .container-fluid {{
                max-width: 100% !important;
                padding: 0px !important;
            }}
        </style>
        """
        # 3. Combine and Render
        # We prepend the CSS so it overrides the internal Bootstrap styles
        styled_report = inject_css + report_html
        with st.container(height=8000, border=False):
            components.html(styled_report, height=12000, scrolling=True)
else:
    st.info("Please upload a CSV file to begin the transformation.")
