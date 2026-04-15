# 💻 Laptop Price Prediction Web App

A Machine Learning web application that predicts laptop prices based on specifications using a trained regression model and Streamlit UI.

---

## 🚀 Project Overview

This project uses a **Stacking Regressor model** trained on a laptop dataset to predict the price of a laptop based on features like:

* Brand (Company)
* Type (Gaming, Notebook, etc.)
* RAM
* Weight
* Touchscreen
* IPS Display
* PPI (Pixel Density)
* CPU Brand
* GPU Brand
* Storage (HDD / SSD)
* Operating System

The model is deployed using **Streamlit** for an interactive web interface.

---

## 🧠 Machine Learning Details

* Algorithm: Stacking Regressor
* Preprocessing: OneHotEncoding + Feature Engineering
* Target: Log(Price) (converted back using exponential)
* Model File: `pipe.pkl`

---

## ⚙️ Installation & Setup

### 1. Clone repository

```bash
git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor
```

### 2. Create environment

```bash
conda create -n laptop-env python=3.10
conda activate laptop-env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run application

```bash
streamlit run app.py
```

---

## 🎯 Features

* Clean UI using Streamlit
* Real-time prediction
* ML pipeline integration
* Feature-based input system
* Production-ready structure

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit

---

## 📌 Future Improvements

* Model accuracy improvement
* Advanced UI design
* Cloud deployment (Streamlit Cloud / Render)
* API version using Flask/FastAPI

---

## 👨‍💻 Author

Built with ❤️ by Mehedi Hassan