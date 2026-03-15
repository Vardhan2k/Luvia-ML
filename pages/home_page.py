import streamlit as st

# --- HERO SECTION ---
st.write("## Welcome to Luvia ML")
st.write("##### Your End-to-End, No-Code Machine Learning Pipeline.")

st.markdown("""
Luvia ML is designed to take you from raw data to production-ready predictions in minutes, not months. 
Whether you are predicting customer churn, housing prices, or medical diagnoses, follow the four steps below to forge your intelligence.
""")

st.divider()

# --- THE 4 STEPS (GRID LAYOUT) ---
st.write("### 🗺️ The Pipeline Journey")

# Row 1
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.write("### 🔍 Step 1: The Oracle")
        st.write("**Exploratory Data Analysis (EDA)**")
        st.write("Upload your raw CSV data. The Oracle will automatically generate a comprehensive, interactive report detailing missing values, correlations, and distributions.")
        st.write("") # Spacer
        st.page_link("pages/exploration.py", label="Go to The Oracle", icon=":material/analytics:")

with col2:
    with st.container(border=True):
        st.write("### 🛠️ Step 2: The Refinery")
        st.write("**Feature Engineering & Preprocessing**")
        st.write("Select your target variable. Normalize data, handle missing outliers, fix multicollinearity, and mathematically prepare your dataset for the AI algorithms.")
        st.write("")
        st.page_link("pages/refinery.py", label="Go to The Refinery", icon=":material/architecture:")

st.write("") # Spacer between rows

# Row 2
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.write("### 🚀 Step 3: The Forge")
        st.write("**Model Training & Leaderboard**")
        st.write("Ignite the training engine. Luvia will evaluate multiple algorithms simultaneously, rank them by accuracy or R-squared, and fine-tune the ultimate winner.")
        st.write("")
        st.page_link("pages/forge.py", label="Go to The Forge", icon=":material/model_training:")

with col4:
    with st.container(border=True):
        st.write("### 🔮 Step 4: The Lens")
        st.write("**Inference & Predictions**")
        st.write("Upload fresh, unseen data and apply your freshly forged `.pkl` model. Generate instant predictions and download the results as a ready-to-use CSV.")
        st.write("")
        st.page_link("pages/predict.py", label="Go to The Lens", icon=":material/online_prediction:")

st.divider()

# --- FOOTER ---
st.caption("🔒 **Privacy First:** Luvia ML processes all data directly in your current session. No data is stored or sent to external servers after you close this tab.")