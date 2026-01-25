# Abhay's Project Portfolio

Welcome to my curated portfolio showcasing hands-on projects in **Machine Learning** and **Big Data Engineering**. Each folder contains production-ready work designed to demonstrate technical depth, practical impact, and deployment readiness.

---

## 🔍 Contents

### 📁 ML/
Interactive machine learning projects focused on model building, evaluation, and deployment.

**Featured App:**  
[Credit Card Default Risk Prediction](https://your-streamlit-app-link.streamlit.app)  
A Streamlit-based web app that predicts credit card default risk using a trained Random Forest model. Includes:

- Clean UI with sidebar inputs
- Scaled prediction pipeline using `MinMaxScaler`
- Model and feature alignment for robust inference
- Public cloud deployment for recruiter access

**Files:**
- `app.py` — Streamlit app code  
- `models/` — Saved `.joblib` files: model, scaler, feature list  
- `requirements.txt` — Python dependencies  
- `README.md` — Project overview
- “This project uses MLflow for experiment tracking. Run mlflow ui locally to view experiments.”

---


## 🚀 Deployment
All ML apps are cloud-hosted and publicly accessible.  
To run locally:
```bash
streamlit run app.py