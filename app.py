import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("diabetes_predictor.pkl")  
scaler=joblib.load("scaler.pkl") 
st.set_page_config(page_title="🩺 Diabetes Predictor", page_icon="💉", layout="centered")

st.title("🩺 Diabetes Prediction App")
st.markdown("Enter patient health details to predict the **Diabetes Outcome** (0 = No, 1 = Yes)")

with st.form("diabetes_form"):
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input("🤰 Pregnancies", 0, 20, 2)
        Glucose = st.number_input("🩸 Glucose Level", 0, 300, 120)
        BloodPressure = st.number_input("🫀 Blood Pressure", 0, 200, 70)
        SkinThickness = st.number_input("📏 Skin Thickness", 0, 99, 20)

    with col2:
        Insulin = st.number_input("💉 Insulin Level", 0, 900, 85)
        BMI = st.number_input("⚖️ BMI", 0.0, 70.0, 26.5)
        DiabetesPedigreeFunction = st.number_input("🧬 Diabetes Pedigree Function", 0.0, 5.0, 0.5)
        Age = st.number_input("🎂 Age", 1, 120, 33)

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    input_df = pd.DataFrame([input_data])
    input_data = scaler.transform(input_df)       

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    
    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.error(f"🩺 Result: **DIABETES POSITIVE** ")
    else:
        st.success(f"💚 Result: **NO DIABETES** ")
    st.write("Probability of Diabetes:",round(prob,4))


st.markdown("---------")
st.caption("Developed by Atchaya • Diabetes Predictor 💡")
