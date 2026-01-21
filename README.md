# 📉 Prediksi Churn Pelanggan Menggunakan XGBoost

## 🧠 Deskripsi Proyek
Proyek ini merupakan **Tugas Besar Mata Kuliah Machine Learning** yang bertujuan untuk membangun
aplikasi **prediksi churn pelanggan (pelanggan berhenti berlangganan)** menggunakan pendekatan
**end-to-end Machine Learning**, mulai dari preprocessing data, pemodelan, evaluasi, hingga
deployment berbasis web menggunakan **Streamlit**.

Model utama yang digunakan adalah **XGBoost**, karena dataset churn umumnya bersifat
**imbalanced**, sehingga membutuhkan algoritma yang mampu menangani distribusi kelas tidak seimbang
dengan baik.

---

## 🎯 Tujuan Proyek
- Memprediksi kemungkinan pelanggan melakukan churn
- Membandingkan Logistic Regression (baseline) dan XGBoost (advanced)
- Menerapkan pipeline Machine Learning end-to-end
- Melakukan deployment model dalam bentuk aplikasi web interaktif

---

## 📊 Dataset
- **Nama Dataset**: Telco Customer Churn  
- **Sumber**: Kaggle  
  https://www.kaggle.com/datasets/blastchar/telco-customer-churn  
- **Jumlah Data**: ±7.000 baris  
- **Jumlah Fitur**: >20 fitur  
- **Target**: Churn (Yes / No)  
- **Karakteristik Data**: Imbalanced  

Dataset ini **bukan dataset “Hello World”** dan memenuhi seluruh ketentuan tugas besar.

---

## 🧪 Metodologi

### 1. Preprocessing Data
- Menghapus kolom tidak relevan (customerID)
- Menangani missing value pada TotalCharges
- Encoding label target (Churn)
- One-Hot Encoding fitur kategorikal
- Standard Scaling fitur numerik
- Menyimpan scaler dan feature names untuk deployment

### 2. Modeling
- Logistic Regression sebagai baseline model
- XGBoost sebagai model utama
- Penanganan data imbalanced menggunakan `scale_pos_weight`

### 3. Evaluasi Model
Metrik evaluasi yang digunakan:
- F1-Score
- ROC-AUC
- Confusion Matrix
- ROC Curve
- Feature Importance (XGBoost)

---

## 📈 Ringkasan Hasil Evaluasi

| Model                | F1-Score   | ROC-AUC   |
|---------------------|------------|-----------|
| Logistic Regression | Baik       | Baik      |
| XGBoost             | Lebih Baik | Lebih Baik |

Model **XGBoost** dipilih untuk deployment karena memberikan performa terbaik
pada data tidak seimbang.

---

## 🌐 Deployment Aplikasi
Aplikasi web dibangun menggunakan **Streamlit** dengan fitur:
- Form input data pelanggan
- Prediksi churn dan probabilitasnya
- Visualisasi probabilitas churn
- Penjelasan hasil prediksi
- Antarmuka berbahasa Indonesia
- Tampilan UI ramah pengguna

---

## 🗂️ Struktur Folder Proyek

```

churn_project/
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── notebooks/
│   └── churn_prediction.ipynb
├── models/
│   ├── xgb_model.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
├── app.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/username/churn-project.git
cd churn-project
````

### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

Aktivasi virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Menjalankan Notebook

```bash
jupyter notebook
```

Buka file:

```
notebooks/churn_prediction.ipynb
```

Lalu jalankan **Restart & Run All**.

### 5. Menjalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

Akses aplikasi melalui browser:

```
http://localhost:8501
```

---

## 🧾 Contoh Input Pengujian

* Tenure: 12 bulan
* Monthly Charges: 75
* Total Charges: 900
* Contract: Month-to-month

Biasanya menunjukkan **risiko churn tinggi**.

---

## 🎓 Identitas Pembuat

* **Nama**: Ardi Kamal Karima
* **NIM**: 301230023
* **Kelas**: 5C
* **Semester**: 5
* **Universitas**: Universitas Bale Bandung (UNIBBA)

---

## 📌 Catatan Akademik

Proyek ini dibuat untuk memenuhi **Tugas Besar Mata Kuliah Machine Learning**
dan telah memenuhi kriteria:

* Pipeline end-to-end
* Komparasi minimal dua algoritma
* Evaluasi tepat untuk data imbalanced
* Deployment berbasis web

---

## 📜 Lisensi

Proyek ini dibuat untuk **kepentingan akademik dan pembelajaran**.

````





