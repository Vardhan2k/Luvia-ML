import streamlit as st
import pandas as pd
import pycaret.classification as pyc_class
import pycaret.regression as pyc_reg
import os

st.title("🔮 Step 4: The Lens")
st.write("Apply your forged models to new, unseen data to generate instant predictions.")

# --- 1. MODEL SOURCING ---
st.write("### 🧠 1. Load the Brain")
model_source = st.radio(
    "Where is your model coming from?", 
    ["Use Model from Forge (Current Session)", "Upload a .pkl Model File"],
    horizontal=True
)

loaded_model = None
task = None

if model_source == "Use Model from Forge (Current Session)":
    # Check if the Forge actually completed in this session
    if 'model_bytes' in st.session_state and 'ml_task' in st.session_state:
        task = st.session_state['ml_task']
        model_name = st.session_state.get('winner_name', 'Trained Model')
        st.success(f"✅ Loaded **{model_name}** ({task.title()}) directly from the Forge.")
        
        # PyCaret's load_model() requires a file path, so we temporarily write the bytes to disk
        with open("temp_forge_model.pkl", "wb") as f:
            f.write(st.session_state['model_bytes'])
            
        # Note: PyCaret automatically appends '.pkl' when loading, so we drop the extension here
        if task == 'classification':
            loaded_model = pyc_class.load_model("temp_forge_model")
        else:
            loaded_model = pyc_reg.load_model("temp_forge_model")
    else:
        st.warning("⚠️ The Forge is empty. Please train a model in Step 3 first, or choose to upload a file.")

else:
    # Manual Upload Logic
    uploaded_model = st.file_uploader("Upload your trained PyCaret model (.pkl)", type="pkl")
    task_radio = st.radio("What type of mathematical model is this?", ["Classification", "Regression"], horizontal=True)
    task = "classification" if "Classification" in task_radio else "regression"
    
    if uploaded_model:
        # Save uploaded file temporarily for PyCaret to read
        with open("temp_uploaded_model.pkl", "wb") as f:
            f.write(uploaded_model.getbuffer())
        
        try:
            with st.spinner("Waking up the model..."):
                if task == 'classification':
                    loaded_model = pyc_class.load_model("temp_uploaded_model")
                else:
                    loaded_model = pyc_reg.load_model("temp_uploaded_model")
            st.success("✅ Model loaded successfully!")
        except Exception as e:
            st.error(f"❌ Error loading model. Are you sure it's the correct task type? Details: {e}")


# --- 2. DATA INGESTION ---
st.divider()
st.write("### 📄 2. Upload Unseen Data")
uploaded_data = st.file_uploader("Upload a CSV file containing the data you want to predict", type="csv", help="This dataset must have the exact same columns as your training data, MINUS the target column.")

if uploaded_data and loaded_model is not None:
    new_data = pd.read_csv(uploaded_data)
    
    with st.expander("🔍 Preview New Data"):
        st.dataframe(new_data.head(10))
    
    # --- 3. INFERENCE ENGINE ---
    if st.button("🔮 Generate Predictions", type="primary", use_container_width=True):
        with st.spinner("Looking through The Lens..."):
            try:
                # Predict dynamically based on the task
                if task == 'classification':
                    predictions = pyc_class.predict_model(loaded_model, data=new_data)
                else:
                    predictions = pyc_reg.predict_model(loaded_model, data=new_data)
                    
                st.success("✨ Predictions generated successfully!")
                
                # PyCaret usually names the output column 'prediction_label' or 'Label'
                st.write("### 📊 Prediction Results")
                st.dataframe(predictions, use_container_width=True)
                
                # --- EXPORT ---
                st.divider()
                st.write("### 📦 Export Results")
                
                # Convert dataframe to CSV format for download
                csv_bytes = predictions.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Predictions (.csv)",
                    data=csv_bytes,
                    file_name="luvia_predictions.csv",
                    mime="text/csv",
                    type="primary"
                )
                
            except Exception as e:
                # The most common error here is missing columns
                st.error("❌ Prediction failed. This usually happens if your uploaded data is missing columns that the model was trained on.")
                with st.expander("Show Error Details"):
                    st.write(e)