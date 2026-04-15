import streamlit as st
import pickle
import numpy as np
import pandas as pd
from pathlib import Path

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="wide")

# ------------------ PATH SETUP ------------------
BASE_DIR = Path(__file__).resolve().parent
PIPE_PATH = BASE_DIR / "pipe.pkl"
DF_PATH = BASE_DIR / "df.pkl"

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_model():
    try:
        with open(PIPE_PATH, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

@st.cache_data
def load_data():
    try:
        with open(DF_PATH, "rb") as f:
            data = pickle.load(f)
        return data
    except:
        return None

model = load_model()
df = load_data()

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙️ Configuration")
st.sidebar.info("Provide laptop specifications to predict price")

# ------------------ MAIN UI ------------------
st.title("💻 Laptop Price Predictor")
st.markdown("Predict laptop price using Machine Learning model")

col1, col2 = st.columns(2)

# ---------- INPUTS ----------
with col1:
    company = st.selectbox("Brand", df['Company'].unique() if df is not None else ["Dell", "HP", "Lenovo"])
    type_name = st.selectbox("Type", df['TypeName'].unique() if df is not None else ["Notebook", "Gaming"])
    ram = st.selectbox("RAM (GB)", [4, 8, 16, 32])
    weight = st.slider("Weight (kg)", 0.5, 4.0, 1.8)
    touchscreen = st.radio("Touchscreen", [0, 1])
    ips = st.radio("IPS Display", [0, 1])

with col2:
    ppi = st.slider("PPI", 50, 350, 141)
    cpu = st.selectbox("CPU", df['Cpu brand'].unique() if df is not None else ["Intel Core i5", "Intel Core i7"])
    hdd = st.slider("HDD (GB)", 0, 2000, 0)
    ssd = st.slider("SSD (GB)", 0, 2000, 256)
    gpu = st.selectbox("GPU", df['Gpu brand'].unique() if df is not None else ["Intel", "Nvidia"])
    os = st.selectbox("Operating System", df['os'].unique() if df is not None else ["Windows", "Mac"])

# ------------------ PREDICTION ------------------
if st.button("🚀 Predict Price"):
    if model is None:
        st.error("Model not loaded properly!")
    else:
        input_df = pd.DataFrame([[company, type_name, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
                                columns=["Company","TypeName","Ram","Weight","Touchscreen","Ips","ppi","Cpu brand","HDD","SSD","Gpu brand","os"])

        try:
            prediction = model.predict(input_df)[0]
            price = np.exp(prediction)

            st.success("Prediction Complete 🎉")
            st.metric("Estimated Price", f"৳ {price:,.2f}")
        except Exception as e:
            st.error(f"Prediction error: {e}")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")