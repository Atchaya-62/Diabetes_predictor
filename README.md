🩺 __Diabetes Prediction App__

A simple and user-friendly web application that predicts whether a person is likely to have diabetes based on medical input parameters, using a Machine Learning classification model.

🚀 __Features__

Predicts diabetes likelihood using medical input values
Clean and intuitive Streamlit interface
Uses a trained ML model (diabetes_predictor.pkl)
Scaling handled using a saved scaler (scaler.pkl)
Fast, accurate, and deployment-ready

🧩 __Prerequisites (For Local Use)__

You need:
Python 3.7+
pip

⚙️ __Installation (Local Setup)__
1. Clone the repository
git clone https://github.com/Atchaya-62/Diabetes_predictor


2. Install dependencies
pip install -r requirements.txt


▶️ __Running Locally__
streamlit run app.py

Then open:
http://localhost:8501

🧠 __How It Works__

The app uses a machine learning classifier trained on the PIMA Diabetes dataset.

User inputs include:
Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age

Inputs are scaled through scaler.pkl.

Prediction result is shown as:

0 — Non-Diabetic

1 — Diabetic

📁 __Project Structure__
diabetes-prediction-app/
├── app.py                    
├── train_model.py            
├── diabetes_predictor.pkl    
├── scaler.pkl                
├── diabetes.csv              
├── requirements.txt          
└── README.md                 

🌟 __Future Improvements__

Add confidence score for predictions
Add charts & analytics (BMI distribution, glucose histograms, etc.)
Compare multiple algorithms (Random Forest, SVM, XGBoost)
Add user authentication
Improve UI with animations

🧭 __How to Use the App__

Step 1: Enter all medical parameters
<img width="990" height="802" alt="image" src="https://github.com/user-attachments/assets/882b5aaa-bb0c-4074-8649-81d1d486674f" />


Step 2: Click Predict
<img width="944" height="141" alt="image" src="https://github.com/user-attachments/assets/3cde0e95-b166-41ae-a911-6d898da09efc" />


Step 3: View your diabetes prediction result
<img width="972" height="256" alt="image" src="https://github.com/user-attachments/assets/80e2d295-5f69-49cd-98af-6e5da37f7eea" />

