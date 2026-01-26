# Abhay's Project Portfolio

Welcome to my curated portfolio showcasing hands-on projects in **Machine Learning** and **Big Data Engineering**. Each folder contains production-ready work designed to demonstrate technical depth, practical impact, and deployment readiness.

---

## 📂 Contents
- **ML/** — Interactive machine learning projects focused on model building, evaluation, and deployment.  
- **BigData/** — Scalable pipelines and analytics using Spark, Hive, and HDFS.  
- **Dashboards/** — Tableau and Streamlit dashboards for visualization and reporting.  

---

## 🎯 Featured Project: Credit Card Default Risk Prediction
A Streamlit-based web app that predicts credit card default risk using a trained Random Forest model.

### 🔑 Highlights
- Clean UI with sidebar inputs  
- Scaled prediction pipeline using MinMaxScaler  
- Model and feature alignment for robust inference  
- MLflow for experiment tracking (`mlflow ui` to view locally)  
- Public cloud deployment for recruiter access  

### 📁 Files
- `app.py` — Streamlit app code  
- `models/` — Saved `.joblib` files: model, scaler, feature list  
- `requirements.txt` — Python dependencies  
- `README.md` — Project overview  

---

## 📦 Model Files
Due to GitHub’s 100 MB file size limit, large trained models are excluded from this repository.

🔗 [Download credit_default_rf_balanced.joblib](https://drive.google.com/file/d/1NDQ9PRvCbXXL-n99xhcyD5i3_z5auSJY/view?usp=drive_link)

---

## 🛠 Tech Stack
- **Languages & Libraries:** Python, pandas, scikit-learn, MLflow, numpy, matplotlib  
- **Frameworks:** Streamlit for interactive apps  
- **Big Data Tools:** Spark, Hive, HDFS, Airflow  
- **Visualization:** Tableau  

---

## 🚀 Deployment
All ML apps are cloud-hosted and publicly accessible.

### ▶ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
