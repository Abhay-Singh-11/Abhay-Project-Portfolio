import streamlit as st
import pandas as pd
import joblib
import gdown
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Credit Default Risk Prediction",
    layout="centered"
)

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "credit_default_rf_balanced.joblib"
FEATURES_PATH = BASE_DIR / "features.joblib"

# -----------------------------
# GOOGLE DRIVE CONFIG (MODEL)
# -----------------------------
FILE_ID = "1NDQ9PRvCbXXL-n99xhcyD5i3_z5auSJY"  # your drive file id
URL = f"https://drive.google.com/uc?id={FILE_ID}"

# -----------------------------
# DOWNLOAD MODEL IF NOT PRESENT
# -----------------------------
if not MODEL_PATH.exists():
    with st.spinner("Downloading ML model (one-time)... Please wait..."):
        gdown.download(URL, str(MODEL_PATH), quiet=False)

# -----------------------------
# LOAD MODEL & FEATURES
# -----------------------------
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("❌ Failed to load model file.")
    st.stop()

try:
    feature_names = joblib.load(FEATURES_PATH)
except Exception as e:
    st.error("❌ features.joblib not found. Make sure it is committed to GitHub.")
    st.stop()

# -----------------------------
# TITLE
# -----------------------------
st.title("💳 Credit Card Default Risk Prediction")

st.write(
    "This application predicts the **risk of credit card default** based on "
    "customer credit history and payment behavior."
)

# -----------------------------
# MAPPINGS
# -----------------------------
education_map = {
    0: "Unknown",
    1: "Graduate School",
    2: "University",
    3: "High School",
    4: "Others"
}

marriage_map = {
    0: "Unknown",
    1: "Married",
    2: "Single",
    3: "Others"
}

# -----------------------------
# SIDEBAR INPUTS
# -----------------------------
st.sidebar.header("Customer Information")

LIMIT_BAL = st.sidebar.number_input("Credit Limit (LIMIT_BAL)", 0.0, 1_500_000.0, 20000.0, step=1000.0)
AGE = st.sidebar.number_input("Age", 18, 100, 30)

SEX = st.sidebar.selectbox(
    "Sex",
    options=[1, 2],
    format_func=lambda x: "Male (1)" if x == 1 else "Female (2)"
)

EDUCATION = st.sidebar.selectbox(
    "Education Level",
    options=list(education_map.keys()),
    format_func=lambda x: education_map[x]
)

MARRIAGE = st.sidebar.selectbox(
    "Marriage Status",
    options=list(marriage_map.keys()),
    format_func=lambda x: marriage_map[x]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Repayment Status")

PAY_0 = st.sidebar.number_input("PAY_0", -2, 8, 0)
PAY_2 = st.sidebar.number_input("PAY_2", -2, 8, 0)
PAY_3 = st.sidebar.number_input("PAY_3", -2, 8, 0)
PAY_4 = st.sidebar.number_input("PAY_4", -2, 8, 0)
PAY_5 = st.sidebar.number_input("PAY_5", -2, 8, 0)
PAY_6 = st.sidebar.number_input("PAY_6", -2, 8, 0)

st.sidebar.markdown("---")
st.sidebar.subheader("Bill Amounts")

BILL_AMT1 = st.sidebar.number_input("BILL_AMT1", -1_000_000.0, 2_000_000.0, 0.0, step=1000.0)
BILL_AMT2 = st.sidebar.number_input("BILL_AMT2", -1_000_000.0, 2_000_000.0, 0.0, step=1000.0)
BILL_AMT3 = st.sidebar.number_input("BILL_AMT3", -1_000_000.0, 2_000_000.0, 0.0, step=1000.0)
BILL_AMT4 = st.sidebar.number_input("BILL_AMT4", -1_000_000.0, 2_000_000.0, 0.0, step=1000.0)
BILL_AMT5 = st.sidebar.number_input("BILL_AMT5", -1_000_000.0, 2_000_000.0, 0.0, step=1000.0)
BILL_AMT6 = st.sidebar.number_input("BILL_AMT6", -1_000_000.0, 2_000_000.0, 0.0, step=1000.0)

st.sidebar.markdown("---")
st.sidebar.subheader("Payment Amounts")

PAY_AMT1 = st.sidebar.number_input("PAY_AMT1", 0.0, 2_500_000.0, 0.0, step=1000.0)
PAY_AMT2 = st.sidebar.number_input("PAY_AMT2", 0.0, 2_500_000.0, 0.0, step=1000.0)
PAY_AMT3 = st.sidebar.number_input("PAY_AMT3", 0.0, 2_500_000.0, 0.0, step=1000.0)
PAY_AMT4 = st.sidebar.number_input("PAY_AMT4", 0.0, 2_500_000.0, 0.0, step=1000.0)
PAY_AMT5 = st.sidebar.number_input("PAY_AMT5", 0.0, 2_500_000.0, 0.0, step=1000.0)
PAY_AMT6 = st.sidebar.number_input("PAY_AMT6", 0.0, 2_500_000.0, 0.0, step=1000.0)

# -----------------------------
# BUILD INPUT DATAFRAME
# -----------------------------
input_df = pd.DataFrame({
    "LIMIT_BAL": [LIMIT_BAL],
    "AGE": [AGE],
    "EDUCATION": [EDUCATION],
    "MARRIAGE": [MARRIAGE],
    "PAY_0": [PAY_0],
    "PAY_2": [PAY_2],
    "PAY_3": [PAY_3],
    "PAY_4": [PAY_4],
    "PAY_5": [PAY_5],
    "PAY_6": [PAY_6],
    "BILL_AMT1": [BILL_AMT1],
    "BILL_AMT2": [BILL_AMT2],
    "BILL_AMT3": [BILL_AMT3],
    "BILL_AMT4": [BILL_AMT4],
    "BILL_AMT5": [BILL_AMT5],
    "BILL_AMT6": [BILL_AMT6],
    "PAY_AMT1": [PAY_AMT1],
    "PAY_AMT2": [PAY_AMT2],
    "PAY_AMT3": [PAY_AMT3],
    "PAY_AMT4": [PAY_AMT4],
    "PAY_AMT5": [PAY_AMT5],
    "PAY_AMT6": [PAY_AMT6],
    "SE_MA": [SEX]
})

# Align with training features
input_df = input_df[feature_names]

# Preview
preview_df = input_df.copy()
preview_df["EDUCATION"] = preview_df["EDUCATION"].replace({5: 0, 6: 0}).map(education_map)
preview_df["MARRIAGE"] = preview_df["MARRIAGE"].map(marriage_map)
preview_df["SE_MA"] = preview_df["SE_MA"].map({1: "Male", 2: "Female"})

st.write("### Input Data (Preview)")
st.dataframe(preview_df)

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("Predict Default Risk"):

    proba = model.predict_proba(input_df)[0, 1]

    st.subheader("Prediction Result")

    if proba < 0.30:
        st.success(f"✅ Low Risk of Default (Probability: {proba:.2%})")
    elif proba < 0.50:
        st.warning(f"⚠️ Medium Risk of Default (Probability: {proba:.2%})")
    else:
        st.error(f"🚨 High Risk of Default (Probability: {proba:.2%})")

    st.markdown(
        """
        **Risk Interpretation**
        - **Low Risk:** Customer is unlikely to default based on historical behavior.
        - **Medium Risk:** Customer shows moderate signs of repayment risk.
        - **High Risk:** Customer exhibits strong indicators of potential default.
        """
    )
