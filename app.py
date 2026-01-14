import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

st.set_page_config(page_title="Prediksi UMKM PRO", layout="centered")
st.title("🏪 Aplikasi Prediksi UMKM PRO")

MODEL_FILE = "model_umkm.pkl"

# =====================
# UPLOAD DATA
# =====================
uploaded_file = st.file_uploader("Upload file CSV UMKM", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("data_umkm.csv")
    st.info("Menggunakan data contoh UMKM")

st.subheader("📊 Data")
st.write(data)

# =====================
# PILIH KOLOM
# =====================
st.subheader("⚙️ Pilih Kolom Input & Target")

columns = data.columns.tolist()

x_cols = st.multiselect(
    "Pilih beberapa kolom Input (X)",
    columns,
    default=columns[:-1]
)

y_col = st.selectbox("Kolom Target (Y)", columns, index=len(columns)-1)

if len(x_cols) == 0:
    st.warning("Pilih minimal 1 kolom input")
    st.stop()

X = data[x_cols]
y = data[y_col]

# =====================
# SPLIT DATA
# =====================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================
# TRAIN / LOAD MODEL
# =====================
if os.path.exists(MODEL_FILE):
    model = joblib.load(MODEL_FILE)
    st.info("Model di-load dari file")
else:
    model = RandomForestRegressor(n_estimators=300, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_FILE)
    st.success("Model baru dilatih & disimpan")

# =====================
# AKURASI
# =====================
y_pred_test = model.predict(X_test)
akurasi = r2_score(y_test, y_pred_test)
st.success(f"Akurasi Model (R2 Score): {akurasi:.2f}")

# =====================
# INPUT MANUAL
# =====================
st.subheader("🔮 Prediksi Manual")

input_values = []

for col in x_cols:
    val = st.number_input(
        f"Masukkan {col}",
        float(data[col].min()),
        float(data[col].max())
    )
    input_values.append(val)

prediksi = model.predict([input_values])

st.write(f"### Hasil Prediksi {y_col}: **{int(prediksi[0])}**")
