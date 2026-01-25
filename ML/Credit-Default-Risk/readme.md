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
## Model Files

Due to GitHub’s 100 MB file size limit, large trained models are excluded from this repository.

🔗 Download the Random Forest model used in the Credit Default Risk project:  
[Download credit_default_rf_balanced.joblib](https://drive.google.com/file/d/1NDQ9PRvCbXXL-n99xhcyD5i3_z5auSJY/view?usp=sharing))

## 🚀 Deployment
All ML apps are cloud-hosted and publicly accessible.  
To run locally:
```bash
streamlit run app.py
