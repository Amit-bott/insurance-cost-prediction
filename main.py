# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# from streamlit_lottie import st_lottie
# import requests
# import json

# # ----------------------------------------------------
# #  PAGE CONFIG + GLOBAL CSS
# # ----------------------------------------------------
# st.set_page_config(
#     page_title="Insurance Cost Predictor",
#     layout="centered",
#     page_icon="💰"
# )
# # ----------------------------------------------------
# #  DARK BLACK THEME + PREMIUM UI
# # ----------------------------------------------------
# dark_theme_css = """
# <style>
# /* Full black background */
# .stApp {
#     background: #000000 !important;
# }

# /* Glassmorphism components */
# .glass-card {
#     background: rgba(20, 20, 20, 0.55);
#     padding: 25px;
#     border-radius: 20px;
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 8px 30px rgba(0,0,0,0.6);
#     backdrop-filter: blur(14px);
# }

# /* Headings */
# h1, h2, h3, h4, h5, h6, p, label, span {
#     color: #e8e8e8 !important;
# }

# /* SideBar */
# [data-testid="stSidebar"] {
#     background-color: #0d0d0d !important;
#     border-right: 1px solid #222 !important;
# }

# /* Buttons */
# .stButton>button {
#     background: linear-gradient(135deg, #8E2DE2, #4A00E0);
#     color: white !important;
#     padding: 0.75rem 1.8rem;
#     border-radius: 14px;
#     border: none;
#     transition: 0.2s ease;
#     font-size: 17px;
# }
# .stButton>button:hover {
#     transform: scale(1.07);
#     background: linear-gradient(135deg, #4A00E0, #8E2DE2);
# }

# /* Input fields */
# input, select, textarea {
#     background-color: #111 !important;
#     color: white !important;
#     border-radius: 10px !important;
#     border: 1px solid #333 !important;
# }

# /* Tables */
# table {
#     color: white !important;
# }

# /* Metrics */
# .css-1xarl3l, .css-12w0qpk {
#     background: rgba(255,255,255,0.12) !important;
#     border-radius: 12px !important;
#     color: #fff !important;
# }
# </style>
# """
# st.markdown(dark_theme_css, unsafe_allow_html=True)


# # ----------------------------------------------------
# # LOAD THE ML MODEL
# # ----------------------------------------------------
# try:
#     loaded_model = joblib.load('insurance_expense_predictor.pkl')
#     model_loaded = True
# except:
#     try:
#         loaded_model = joblib.load('insurance_model.pkl')
#         model_loaded = True
#     except:
#         model_loaded = False
#         st.error("❌ Model file not found. Please ensure the model file exists.")

# # ----------------------------------------------------
# # LOTTIE ANIMATION FROM URL (No file needed)
# # ----------------------------------------------------
# # ----------------------------------------------------
# # LOTTIE ANIMATION (WORKING FIX)
# def load_lottie_url(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# # WORKING INSURANCE LOTTIE URL
# lottie_animation = load_lottie_url(
#     "https://lottie.host/ff2b0e56-4ad9-48fe-ab45-b222ecf60b45/LZqSzgQFq8.json"
# )

# if lottie_animation:
#     st_lottie(lottie_animation, height=260, key="header")
# else:
#     st.write("⚠️ Animation unavailable, but app still works.")

# # Title Section
# # st.markdown("<h1 style='text-align:center; color:white;'>🔮 Insurance Cost Prediction</h1>", unsafe_allow_html=True)
# # st.markdown("<p style='text-align:center; color:#e0e0e0;'>Modern AI-powered prediction with premium UI</p>", unsafe_allow_html=True)

# st.markdown("<h1 style='text-align:center;'>🔮 Insurance Cost Prediction</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; color:#999;'>AI-powered premium prediction dashboard</p>", unsafe_allow_html=True)

# # ----------------------------------------------------
# # INPUT FORM
# # ----------------------------------------------------
# st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
# st.subheader("📥 Enter Customer Details")

# col1, col2 = st.columns(2)

# with col1:
#     age = st.number_input('Age', min_value=18, max_value=100, value=30)
#     bmi = st.number_input('BMI', min_value=10.0, max_value=60.0, value=28.5, step=0.1)
#     children = st.number_input('Children', min_value=0, max_value=10, value=0)

# with col2:
#     sex = st.selectbox("Gender", ['Male', 'Female'])
#     smoker = st.selectbox('Smoker', ['No', 'Yes'])
#     region = st.selectbox('Region', ['Southwest', 'Southeast', 'Northwest', 'Northeast'])

# st.markdown("</div>", unsafe_allow_html=True)
# st.markdown("---")


# # ----------------------------------------------------
# # PREDICTION
# # ----------------------------------------------------
# if st.button("🚀 Predict Insurance Cost"):
#     if not model_loaded:
#         st.error("❌ Model not loaded.")
#     else:
#         # Prepare DataFrame
#         input_data = pd.DataFrame({
#             'age': [age],
#             'sex': [sex.lower()],
#             'bmi': [bmi],
#             'children': [children],
#             'smoker': ['yes' if smoker == 'Yes' else 'no'],
#             'region': [region.lower()]
#         })

#         st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
#         st.write("### 📊 Input Summary")
#         st.table(input_data)
#         st.markdown("</div>", unsafe_allow_html=True)

#         # Prediction
#         try:
#             pred = loaded_model.predict(input_data)[0]

#             st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
#             st.subheader("🎯 Prediction Result")

#             st.metric("Estimated Annual Insurance Cost", f"${pred:,.2f}")

#             st.info(f"""
#             Based on the entered details, the predicted annual insurance cost is  
#             **${pred:,.2f}**  
#             """)

#             st.markdown("</div>", unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"❌ Error during prediction: {str(e)}")


# # ----------------------------------------------------
# # SIDEBAR
# # ----------------------------------------------------
# with st.sidebar:
#     st.markdown("<h2 style='color:white;'>ℹ️ About</h2>", unsafe_allow_html=True)
#     st.write("""
#     This app predicts annual insurance costs using a trained ML model.

#     **Factors considered:**
#     - Age  
#     - Gender  
#     - BMI  
#     - Smoking status  
#     - Region  
#     - Number of children  
#     """)

#     st.markdown("---")
#     st.caption("Built with ❤️ using Streamlit + Machine Learning")












import streamlit as st
import joblib
import pandas as pd
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Insurance Cost Predictor 3D",
    layout="wide",
    page_icon="💸"
)

# --------------------------------------------------
# THEME TOGGLE
# --------------------------------------------------
theme = st.sidebar.toggle("🌗 Dark Mode", value=False)

bg = "#000000" if theme else "#f4f6f8"
card = "rgba(20,20,20,0.7)" if theme else "white"
text = "#ffffff" if theme else "#111827"

# --------------------------------------------------
# 3D CSS
# --------------------------------------------------
st.markdown(f"""
<style>
.stApp {{
    background: {bg};
}}

.card {{
    background: {card};
    padding: 25px;
    border-radius: 22px;
    color: {text};
    box-shadow: 0 25px 50px rgba(0,0,0,0.25);
    transition: 0.4s ease;
    transform-style: preserve-3d;
}}
.card:hover {{
    transform: rotateX(6deg) rotateY(-6deg) scale(1.03);
}}

h1,h2,h3,p,label {{
    color: {text} !important;
}}

.stButton>button {{
    background: linear-gradient(135deg,#22c55e,#16a34a);
    color:white;
    font-size:17px;
    border-radius:14px;
    padding:0.7rem 1.8rem;
}}

input, select {{
    border-radius:12px !important;
}}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
try:
    model = joblib.load("insurance_expense_predictor.pkl")
except:
    st.error("❌ Model file missing")
    st.stop()

# --------------------------------------------------
# LOTTIE
# --------------------------------------------------
def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie = load_lottie(
    "https://lottie.host/ff2b0e56-4ad9-48fe-ab45-b222ecf60b45/LZqSzgQFq8.json"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
c1, c2 = st.columns([2,1])
with c1:
    st.markdown("<h1>Insurance Cost Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p>3D • Smart • Auto-Filled • AI Powered</p>", unsafe_allow_html=True)

with c2:
    if lottie:
        st_lottie(lottie, height=240)

# --------------------------------------------------
# INPUT CARD (NO EMPTY BOXES)
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 18, 100, value=30)

with col2:
    bmi = st.number_input("BMI", 10.0, 60.0, value=27.5)

with col3:
    children = st.number_input("Children", 0, 10, value=1)

col4, col5, col6 = st.columns(3)

with col4:
    sex = st.selectbox("Gender", ["Male", "Female"], index=0)

with col5:
    smoker = st.selectbox("Smoker", ["No", "Yes"], index=0)

with col6:
    region = st.selectbox(
        "Region",
        ["Southwest", "Southeast", "Northwest", "Northeast"],
        index=0
    )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("")

# --------------------------------------------------
# PREDICT
# --------------------------------------------------
if st.button("🚀 Predict Insurance Cost"):
    input_df = pd.DataFrame({
        "age": [age],
        "sex": [sex.lower()],
        "bmi": [bmi],
        "children": [children],
        "smoker": ["yes" if smoker == "Yes" else "no"],
        "region": [region.lower()]
    })

    prediction = model.predict(input_df)[0]

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎯 Prediction Result")
    st.metric("Estimated Insurance Cost", f"$ {prediction:,.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.subheader("ℹ️ About App")
    st.write("""
    • Auto-filled inputs  
    • No empty box errors  
    • 3D animated UI  
    • Real ML prediction  
    """)
    st.caption("Built with ❤️ Streamlit")
