
import streamlit as st
import pandas as pd
# 1. Import both modules
import pycaret.classification as pyc_class
import pycaret.regression as pyc_reg
import os

st.title("🚀 Step 3: The Forge")

if 'transformed_df' in st.session_state and 'ml_task' in st.session_state:
    
    # 2. DYNAMIC MODULE ROUTING
    task = st.session_state['ml_task']
    if task == 'classification':
        pc = pyc_class
        sort_metric = "Accuracy"
        st.caption("🧠 Engine tuned for: **Category Prediction (Classification)**")
    else:
        pc = pyc_reg
        sort_metric = "R2" # R-Squared is the standard accuracy metric for Regression
        st.caption("📈 Engine tuned for: **Number Prediction (Regression)**")
    
    # 3. Fetch available models using the dynamic module
    available_models_df = pc.models()
    model_ids = available_models_df.index.tolist()
    model_names = available_models_df['Name'].to_dict()

    # --- 🤖 MODEL SELECTION UI ---
    st.write("### 🤖 Model Selection")
    
    select_all = st.toggle("Select All Models", value=False, help="Enable to queue every available algorithm.")
    
    selected_models = st.multiselect(
        "Choose algorithms to evaluate:", 
        options=model_ids,
        default=model_ids if select_all else ['lr', 'dt', 'rf'],
        format_func=lambda x: f"{model_names.get(x, x)} ({x})"
    )

    # --- ⚙️ TUNING SETTINGS ---
    st.write("### ⚒️ Model Training Settings")
    with st.expander("⚙️ Advanced Tuning Settings"):
        do_tuning = st.toggle("Optimize Hyperparameters (Winner Only)", value=False)
        n_iter = st.slider("Tuning Iterations", 5, 50, 10)

    if not selected_models:
        st.warning("⚠️ Please select at least one model to ignite the Forge.")
        st.stop()

    # --- 🔥 IGNITION ---
    if st.button("🔥 Ignite the Forge", type="primary", width='stretch'):
        results = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        log_container = st.container(border=True)
        total_models = len(selected_models) 
        
        # START THE LOOP
        for i, m_id in enumerate(selected_models):
            percent = int(((i + 1) / total_models) * 100)
            readable_name = model_names.get(m_id, m_id)
            status_text.markdown(f"**Current Task:** Training `{readable_name}`... ({i+1}/{total_models})")
            
            try:
                # Train using dynamic module
                model = pc.create_model(m_id, cross_validation=True, verbose=False)
                score_df = pc.pull()
                
                if 'Mean' in score_df.index:
                    metrics = score_df.loc[['Mean']].copy()
                else:
                    metrics = score_df.iloc[-1:].copy()
                    
                metrics.insert(0, 'Model_ID', m_id)
                metrics.insert(1, 'Algorithm', readable_name)
                results.append(metrics)
                
                log_container.success(f"✅ `{readable_name}` completed.")
            except Exception as e:
                log_container.error(f"❌ Failed to train `{readable_name}`: {e}")
            
            progress_bar.progress(percent)

        if not results:
            st.error("All selected models failed to train.")
            st.stop()

        # --- 🏆 FINALIZING THE LEADERBOARD ---
        status_text.success("✨ All models forged! Compiling results...")
        
        # 4. Sort dynamically based on the task metric
        leaderboard = pd.concat(results).sort_values(by=sort_metric, ascending=False)
        leaderboard = leaderboard.reset_index(drop=True)
        leaderboard.index += 1
        st.session_state['leaderboard'] = leaderboard
        
        winner_id = leaderboard.iloc[0]['Model_ID']
        winner_name = leaderboard.iloc[0]['Algorithm']
        
        best_model = pc.create_model(winner_id, verbose=False)

        if do_tuning:
            with st.status(f"🎯 Fine-tuning {winner_name}...", expanded=True):
                best_model = pc.tune_model(best_model, n_iter=n_iter, choose_better=True)
                st.write("Optimization complete.")

        st.session_state['leaderboard'] = leaderboard
        st.session_state['winner_id'] = winner_id
        st.session_state['winner_name'] = winner_name
        
        # Save model using dynamic module
        pc.save_model(best_model, 'luvia_best_model')
        with open('luvia_best_model.pkl', 'rb') as f:
            st.session_state['model_bytes'] = f.read()
            
        st.session_state['forge_complete'] = True

    # ==========================================
    # --- 📊 DISPLAY RESULTS (OUTSIDE BUTTON) ---
    # ==========================================
    if st.session_state.get('forge_complete', False):
        st.write(f"### 🏆 Winner: **{st.session_state['winner_name']}**")
        
        st.write("#### Final Metrics")
        st.dataframe(st.session_state['leaderboard'], width="stretch")
        
        st.divider()
        st.write("### 📦 Export Model")
        st.download_button(
            label="📥 Download Production Model (.pkl)", 
            data=st.session_state['model_bytes'], 
            file_name=f"luvia_{st.session_state['winner_id']}_{task}_model.pkl",
            mime="application/octet-stream",
            type="primary"
        )

else:
    st.warning("⚠️ The Forge is cold. Please run the **Refinery** first to prepare your data!")