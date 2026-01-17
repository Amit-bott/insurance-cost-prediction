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


theme = st.sidebar.toggle("🌗 Dark Mode", value=False)

bg = "#000000" if theme else "#f4f6f8"
card = "rgba(20,20,20,0.7)" if theme else "white"
text = "#ffffff" if theme else "#111827"


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


try:
    model = joblib.load("insurance_expense_predictor.pkl")
except:
    st.error("❌ Model file missing")
    st.stop()


def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie = load_lottie(
    "https://lottie.host/ff2b0e56-4ad9-48fe-ab45-b222ecf60b45/LZqSzgQFq8.json"
)


c1, c2 = st.columns([2,1])
with c1:
    st.markdown("<h1>Insurance Cost Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p>3D • Smart • Auto-Filled • AI Powered</p>", unsafe_allow_html=True)

with c2:
    if lottie:
        st_lottie(lottie, height=240)


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


with st.sidebar:
    st.subheader("ℹ️ About App")
    st.write("""
    • Auto-filled inputs  
    • No empty box errors  
    • 3D animated UI  
    • Real ML prediction  
    """)
    st.caption("Built with ❤️ Streamlit")
