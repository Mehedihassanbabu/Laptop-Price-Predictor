import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)

# ------------------ LOAD DATA ------------------
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

# ------------------ HEADER ------------------
st.markdown("<h1 style='text-align: center;'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Enter laptop specifications to estimate price</p>", unsafe_allow_html=True)

st.markdown("---")

# ------------------ LAYOUT ------------------
col1, col2 = st.columns(2)

# ---------- LEFT SIDE ----------
with col1:
    st.subheader("🔧 Basic Specifications")

    company = st.selectbox('Brand', df['Company'].unique())
    type_name = st.selectbox('Type', df['TypeName'].unique())

    ram = st.selectbox('RAM (GB)', [2,4,6,8,12,16,24,32,64])
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5)

    touchscreen = st.selectbox('Touchscreen', ['No','Yes'])
    ips = st.selectbox('IPS Display', ['No','Yes'])

# ---------- RIGHT SIDE ----------
with col2:
    st.subheader("⚙️ Technical Specifications")

    screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.0)

    resolution = st.selectbox(
        'Screen Resolution',
        ['1920x1080','1366x768','1600x900','3840x2160',
         '3200x1800','2880x1800','2560x1600',
         '2560x1440','2304x1440']
    )

    cpu = st.selectbox('CPU', df['Cpu brand'].unique())
    hdd = st.selectbox('HDD (GB)', [0,128,256,512,1024,2048])
    ssd = st.selectbox('SSD (GB)', [0,8,128,256,512,1024])
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())
    os = st.selectbox('Operating System', df['os'].unique())

# ------------------ PREDICTION BUTTON ------------------
st.markdown("---")

center_col = st.columns([1,2,1])
with center_col[1]:
    predict_btn = st.button("🚀 Predict Price", use_container_width=True)

# ------------------ PREDICTION ------------------


if predict_btn:

    # convert categorical
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / screen_size

    # dataframe create
    input_df = pd.DataFrame(
        [[company, type_name, ram, weight, touchscreen_val, ips_val,
          ppi, cpu, hdd, ssd, gpu, os]],
        columns=[
            "Company","TypeName","Ram","Weight","Touchscreen","Ips",
            "ppi","Cpu brand","HDD","SSD","Gpu brand","os"
        ]
    )

    try:
        prediction = pipe.predict(input_df)[0]
        price = np.exp(prediction)

        # -------- CENTER RESULT --------
        result_col = st.columns([1,2,1])
        with result_col[1]:
            st.markdown("### Estimated Price")
            st.success(f"Tk {int(price):,}")

    except Exception as e:
        result_col = st.columns([1,2,1])
        with result_col[1]:
            st.error(f"❌ {e}")