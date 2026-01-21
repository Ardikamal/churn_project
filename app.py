import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# =========================
# LOAD MODEL & PREPROCESS
# =========================
model = joblib.load("models/xgb_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Prediksi Churn Pelanggan",
    page_icon="📉",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("📉 Aplikasi Prediksi Churn Pelanggan")
st.markdown("""
Aplikasi ini digunakan untuk **memprediksi kemungkinan pelanggan berhenti berlangganan (churn)**  
menggunakan **Machine Learning (XGBoost)** dengan data pelanggan perusahaan telekomunikasi.
""")

st.markdown("---")

# =========================
# SIDEBAR – IDENTITAS
# =========================
st.sidebar.title("👤 Identitas Pembuat")
st.sidebar.markdown("""
**Nama** : Ardi Kamal Karima  
**NIM** : 301230023  
**Kelas** : 5C  
**Semester** : 5  
**Universitas** : Universitas Bale Bandung (UNIBBA)  

📚 *Tugas Besar Mata Kuliah Machine Learning*
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### ℹ️ Contoh Input
- Tenure: 12 bulan  
- Monthly Charges: 75  
- Total Charges: 900  
- Contract: Month-to-month  
➡️ Biasanya berpotensi **churn**
""")

# =========================
# INPUT USER
# =========================
st.subheader("🧾 Masukkan Data Pelanggan")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    senior = st.selectbox("Pelanggan Lansia", [0, 1])
    partner = st.selectbox("Memiliki Pasangan", ["Yes", "No"])
    dependents = st.selectbox("Memiliki Tanggungan", ["Yes", "No"])

with col2:
    phone = st.selectbox("Layanan Telepon", ["Yes", "No"])
    multiple = st.selectbox("Multi Line", ["Yes", "No", "No phone service"])
    internet = st.selectbox("Layanan Internet", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Jenis Kontrak", ["Month-to-month", "One year", "Two year"])

with col3:
    tenure = st.slider("Lama Berlangganan (bulan)", 0, 72, 12)
    monthly = st.number_input("Biaya Bulanan", 0.0)
    total = st.number_input("Total Biaya", 0.0)
    payment = st.selectbox("Metode Pembayaran", [
        "Electronic check",
        "Mailed check",
        "Credit card (automatic)",
        "Bank transfer (automatic)"
    ])

# =========================
# DATAFRAME INPUT
# =========================
raw_df = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "PhoneService": phone,
    "MultipleLines": multiple,
    "InternetService": internet,
    "Contract": contract,
    "tenure": tenure,
    "MonthlyCharges": monthly,
    "TotalCharges": total,
    "PaymentMethod": payment,
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "PaperlessBilling": "Yes"
}])

# =========================
# PREPROCESSING
# =========================
encoded_df = pd.get_dummies(raw_df)
encoded_df = encoded_df.reindex(columns=feature_names, fill_value=0)

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
encoded_df[num_cols] = scaler.transform(encoded_df[num_cols])

# =========================
# PREDIKSI
# =========================
st.markdown("---")

if st.button("🔍 Prediksi Churn"):
    prob = model.predict_proba(encoded_df)[0][1]
    pred = model.predict(encoded_df)[0]

    st.subheader("📊 Hasil Prediksi")

    if pred == 1:
        st.error("🚨 **PELANGGAN BERPOTENSI CHURN**")
    else:
        st.success("✅ **PELANGGAN TIDAK CHURN**")

    st.write(f"**Probabilitas Churn:** `{prob:.2%}`")

    # =========================
    # PENJELASAN HASIL
    # =========================
    st.markdown("""
    ### 🧠 Interpretasi Model
    - Nilai probabilitas mendekati **1 (100%)** menunjukkan risiko churn tinggi.
    - Faktor utama biasanya:
        - Kontrak bulanan
        - Biaya bulanan tinggi
        - Lama berlangganan rendah
    """)

    # =========================
    # GRAFIK PROBABILITAS
    # =========================
    st.subheader("📈 Visualisasi Probabilitas")

    fig, ax = plt.subplots()
    ax.bar(["Tidak Churn", "Churn"], [1 - prob, prob])
    ax.set_ylabel("Probabilitas")
    ax.set_title("Distribusi Probabilitas Prediksi")

    st.pyplot(fig)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("""
📌 Aplikasi ini dibuat sebagai **Tugas Besar Machine Learning**  
Program Studi Teknik Informatika – Universitas Bale Bandung (UNIBBA)  
© 2026 – Ardi Kamal Karima
""")
