
import streamlit as st
import pandas as pd
# 1. IMPORT BOTH CLASSIFICATION AND REGRESSION
import pycaret.classification as pyc_class
import pycaret.regression as pyc_reg

st.title("🛠️ Step 2: The Refinery")

if st.session_state.get('df') is not None:
    df = st.session_state['df']
    
    # --- 1. TARGET SELECTION (With the Red/Green Highlight) ---
    current_target = st.session_state.get('target', "-- Select Column --")
    is_empty = current_target == "-- Select Column --"
    border_color = "#FF4B4B" if is_empty else "#28A745"
    bg_color = "#FFF5F5" if is_empty else "#F6FFF8"
    
    st.markdown(f"""
        <style>
            div[data-testid="stVerticalBlockBorderWrapper"]:has(.st-key-target_container) {{
                background-color: {bg_color} !important;
                border-left: 10px solid {border_color} !important;
                transition: all 0.4s ease-in-out;
            }}
        </style>
    """, unsafe_allow_html=True)

    with st.container(border=True, key="target_container"):
        st.subheader("🎯 Essential: Choose Your Target")
        target_options = ["-- Select Column --"] + list(df.columns)
        default_idx = target_options.index(current_target) if current_target in target_options else 0
        target = st.selectbox("Select Target Column", options=target_options, index=default_idx, label_visibility="collapsed")
        st.session_state['target'] = target
        
        # 2. ADD ML TASK SELECTOR
        if target != "-- Select Column --":
            st.divider()
            st.write("#### 🧠 Machine Learning Task")
            ml_task = st.radio(
                "What are you trying to predict?", 
                ["Classification (Categories, e.g., Yes/No, Red/Blue)", "Regression (Continuous Numbers, e.g., Price, Age)"],
                help="Classification is for predicting categories. Regression is for predicting continuous numbers."
            )
            # Save the clean task name to session state for the Forge and Predict pages
            st.session_state['ml_task'] = 'classification' if 'Classification' in ml_task else 'regression'

    if target == "-- Select Column --":
        st.warning("⚠️ Action Required: Please select a target column above.")
        st.stop()

    # --- 2. ADVANCED SETTINGS ---
    st.write("### ⚙️ Engine Room: Advanced Preprocessing")

    with st.expander("🛡️ Data Stability & Outliers", expanded=True):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            do_normalize = st.checkbox("Normalize Data", value=True, help="Scales numbers to a 0-1 range. Essential for most AI.")
            norm_method = st.selectbox("Scaling Method", ["zscore", "minmax", "robust"], index=0)
        with col_c2:
            remove_outliers = st.checkbox("Handle Outliers", help="Finds and removes extreme anomalies that skew results.")
            outlier_threshold = st.slider("Outlier Sensitivity", 0.01, 0.10, 0.05)

    with st.expander("🎯 Precision Feature Selection"):
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            remove_multi = st.checkbox("Drop Multicollinearity", value=True, help="Removes redundant columns that are too similar.")
            multi_threshold = st.slider("Correlation Limit", 0.5, 0.95, 0.9)
        with col_s2:
            do_selection = st.checkbox("Smart Feature Selection", value=False)
            selection_threshold = st.slider("Keep Top Features (%)", 10, 100, 80) / 100

    # --- 3. EXECUTION ---
    if st.button("🚀 Run Refinery Pipeline"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        with st.status("Refining data...", expanded=True) as status:
            status_text.write(f"📊 Initializing {st.session_state['ml_task'].title()} Pipeline...")
            
            # 3. DYNAMICALLY CHOOSE THE PYCARET MODULE
            if st.session_state['ml_task'] == 'classification':
                pc_setup = pyc_class.setup
                pc_get_config = pyc_class.get_config
            else:
                pc_setup = pyc_reg.setup
                pc_get_config = pyc_reg.get_config
            
            # THE CORE SETUP
            pc_setup(
                data=df, 
                target=target,
                normalize=do_normalize,
                normalize_method=norm_method,
                remove_outliers=remove_outliers,
                outliers_threshold=outlier_threshold,
                remove_multicollinearity=remove_multi,
                multicollinearity_threshold=multi_threshold,
                feature_selection=do_selection,
                n_features_to_select=selection_threshold, 
                session_id=123,
                preprocess=True,
                html=False,
                verbose=False
            )
            
            progress_bar.progress(80)
            status_text.write("✨ Finalizing transformations...")
            
            # Use the dynamic get_config function
            X_transformed = pc_get_config('dataset_transformed')
            st.session_state['transformed_df'] = X_transformed
            
            progress_bar.progress(100)
            status.update(label="✅ Refinery Complete!", state="complete", expanded=True)
            
            st.write("### 💎 Engineered Dataset Preview")
            st.dataframe(X_transformed.head(10).reset_index(drop=True))
            status_text.empty()

        # st.write("### 💎 Engineered Dataset Preview")
        # st.dataframe(X_transformed.head(10).reset_index(drop=True))

else:
    st.warning("⚠️ Please upload a dataset in the Exploration page first!")