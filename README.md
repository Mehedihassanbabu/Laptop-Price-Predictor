# 💻 Laptop Price Predictor Web App

A Machine Learning web application that predicts laptop prices based on user input specifications using a trained regression model.

---

## 🚀 Project Overview

This project predicts the price of a laptop based on various features such as:

- Brand (Company)
- Type (Gaming, Notebook, etc.)
- RAM
- Weight
- Touchscreen
- IPS Display
- Screen Size & Resolution
- CPU Brand
- GPU Brand
- Storage (HDD / SSD)
- Operating System

The model is deployed using **Streamlit** with a clean and interactive user interface.

---

## 🧠 Machine Learning Details

- **Algorithm:** Stacking Regressor  
- **Preprocessing:** OneHotEncoding + Feature Engineering  
- **Feature Engineering:** PPI calculated from screen resolution & screen size  
- **Target:** Log(Price) → Converted back using exponential  
- **Model File:** `pipe.pkl`

---

## 🖥️ UI Features

✔ Clean & modern Streamlit UI  
✔ Two-column layout for better user experience  
✔ Real-time price prediction  
✔ Centered result display  
✔ Error handling support  


## ⚙️ Installation & Setup

### Clone repository
git clone https://github.com/Mehedihassanbabu/Laptop-Price-Predictor.git

## Create environment
conda create -n laptop-env python=3.10
conda activate laptop-env

## Install dependencies
pip install -r requirements.txt

## Run application
streamlit run app.py

## 🛠 Tech Stack
Python
Pandas
NumPy
Scikit-learn
XGBoost
Streamlit

## 📌 Future Improvements

Model accuracy improvement
Advanced UI design
Cloud deployment (Streamlit Cloud / Render)
API version using Flask/FastAPI

## 👨‍💻 Author

**Mehedi Hassan**  
Aspiring Machine Learning Engineer 🚀  

🔗 GitHub: https://github.com/Mehedihassanbabu  
🔗 LinkedIn: https://www.linkedin.com/in/md-mehedi-hassan-ml/