# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd

# # Load the trained model
# try:
#     # Try loading the model from the correct filename
#     loaded_model = joblib.load('insurance_expense_predictor.pkl')
#     model_loaded = True
# except:
#     # Fallback to the filename mentioned in your code
#     try:
#         loaded_model = joblib.load('insurance_model.pkl')
#         model_loaded = True
#     except:
#         model_loaded = False
#         st.error("❌ Model file not found. Please ensure 'insurance_expense_predictor.pkl' exists.")

# st.set_page_config(
#     page_title="Insurance Cost Predictor",
#     layout="centered"
# )

# st.title("🔮 Insurance Cost Prediction App")
# st.write("Enter customer details below to predict insurance charges.")

# if model_loaded:
#     st.success("✅ Model Loaded Successfully!")

# st.subheader("📥 Enter Customer Details")

# # Create input fields for all features
# col1, col2 = st.columns(2)

# with col1:
#     age = st.number_input('Age', min_value=18, max_value=100, value=30, step=1, help="Age of the customer")
#     bmi = st.number_input('BMI', min_value=10.0, max_value=60.0, value=28.5, step=0.1, format="%.1f", 
#                          help="Body Mass Index (weight in kg/(height in m)^2)")
#     children = st.number_input('Children', min_value=0, max_value=10, value=0, step=1, 
#                               help="Number of children/dependents")

# with col2:
#     sex = st.selectbox("Gender", options=['Male', 'Female'])
#     smoker = st.selectbox('Smoker', options=['No', 'Yes'])
#     region = st.selectbox('Region', options=['Southwest', 'Southeast', 'Northwest', 'Northeast'])

# # Additional information
# st.markdown("---")
# with st.expander("💡 Information about inputs"):
#     st.write("""
#     - **Age**: 18-100 years
#     - **BMI**: Typically 18.5-24.9 is healthy
#     - **Children**: Number of dependents covered by insurance
#     - **Smoker**: Has significant impact on insurance costs
#     - **Region**: Geographical region in the US
#     """)


# # Predict Button

# if st.button("🚀 Predict Insurance Cost", type="primary"):
#     if not model_loaded:
#         st.error("Model not loaded. Cannot make predictions.")
#     else:
#         # Create a DataFrame with the input data
#         # Note: The column names and order must match what the model was trained on
#         input_data = pd.DataFrame({
#             'age': [age],
#             'sex': [sex.lower()],  # Convert to lowercase to match training data
#             'bmi': [bmi],
#             'children': [children],
#             'smoker': ['yes' if smoker == 'Yes' else 'no'],  # Convert to yes/no
#             'region': [region.lower()]  # Convert to lowercase
#         })
        
#         st.write("### 📊 Input Summary")
#         st.table(input_data)
        
#         # Make prediction
#         try:
#             pred = loaded_model.predict(input_data)[0]
            
#             # Display prediction
#             st.markdown("---")
#             st.subheader("🎯 Prediction Results")
            
#             # Create a nice display
#             col_pred, col_icon = st.columns([3, 1])
#             with col_pred:
#                 st.metric(
#                     label="**Estimated Annual Insurance Cost**",
#                     value=f"${pred:,.2f}",
#                     delta=None
#                 )
            
#             with col_icon:
#                 st.write("")
#                 st.write("")
#                 st.write("💵")
            
#             # Add some context
#             st.info(f"""
#             Based on the provided information, the estimated annual insurance cost is **${pred:,.2f}**.
            
#             *This is a machine learning prediction and should be used as an estimate only.*
#             """)
            
#             # Show breakdown of factors
#             st.write("### 🔍 Factors Influencing Cost")
#             factors = {
#                 "Age": "Older customers typically have higher costs",
#                 "BMI": "Higher BMI increases health risk and cost",
#                 "Smoking": "Smokers pay significantly more (2-3x)",
#                 "Children": "More dependents increase cost",
#                 "Region": "Cost varies by geographical location"
#             }
            
#             for factor, impact in factors.items():
#                 st.write(f"• **{factor}**: {impact}")
                
#         except Exception as e:
#             st.error(f"Error making prediction: {str(e)}")
#             st.write("Please ensure all inputs are correctly formatted.")


# # Sidebar with additional info

# with st.sidebar:
#     st.title("ℹ️ About")
#     st.write("""
#     This app predicts insurance costs using a machine learning model trained on historical data.
    
#     The model considers:
#     - Demographic factors (age, gender)
#     - Health metrics (BMI)
#     - Lifestyle choices (smoking)
#     - Family information (children)
#     - Geographic region
    
#     **Model Performance:**
#     - R² Score: ~0.85-0.90
#     - Cross-validated for reliability
#     """)
    
#     st.markdown("---")
#     st.write("**📊 Sample Predictions:**")
#     st.write("""
#     - 30yo, Male, BMI 28.5, 0 children, Non-smoker, Southeast: ~$4,000
#     - 45yo, Female, BMI 32.1, 0 children, Non-smoker, Northwest: ~$8,000
#     - 60yo, Male, BMI 25.8, 1 child, Smoker, Southwest: ~$35,000
#     """)
    
#     st.markdown("---")
#     st.write("**⚠️ Disclaimer:**")
#     st.caption("This tool provides estimates only. Actual insurance premiums may vary based on additional factors not included in this model.")


# # Footer

# st.markdown("---")
# st.caption("Built with Streamlit | Machine Learning Model: Random Forest/Gradient Boosting")





import streamlit as st
import joblib
import numpy as np
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import json

# ----------------------------------------------------
#  PAGE CONFIG + GLOBAL CSS
# ----------------------------------------------------
st.set_page_config(
    page_title="Insurance Cost Predictor",
    layout="centered",
    page_icon="💰"
)
# ----------------------------------------------------
#  DARK BLACK THEME + PREMIUM UI
# ----------------------------------------------------
dark_theme_css = """
<style>
/* Full black background */
.stApp {
    background: #000000 !important;
}

/* Glassmorphism components */
.glass-card {
    background: rgba(20, 20, 20, 0.55);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.6);
    backdrop-filter: blur(14px);
}

/* Headings */
h1, h2, h3, h4, h5, h6, p, label, span {
    color: #e8e8e8 !important;
}

/* SideBar */
[data-testid="stSidebar"] {
    background-color: #0d0d0d !important;
    border-right: 1px solid #222 !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #8E2DE2, #4A00E0);
    color: white !important;
    padding: 0.75rem 1.8rem;
    border-radius: 14px;
    border: none;
    transition: 0.2s ease;
    font-size: 17px;
}
.stButton>button:hover {
    transform: scale(1.07);
    background: linear-gradient(135deg, #4A00E0, #8E2DE2);
}

/* Input fields */
input, select, textarea {
    background-color: #111 !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #333 !important;
}

/* Tables */
table {
    color: white !important;
}

/* Metrics */
.css-1xarl3l, .css-12w0qpk {
    background: rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
    color: #fff !important;
}
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)


# ----------------------------------------------------
# LOAD THE ML MODEL
# ----------------------------------------------------
try:
    loaded_model = joblib.load('insurance_expense_predictor.pkl')
    model_loaded = True
except:
    try:
        loaded_model = joblib.load('insurance_model.pkl')
        model_loaded = True
    except:
        model_loaded = False
        st.error("❌ Model file not found. Please ensure the model file exists.")

# ----------------------------------------------------
# LOTTIE ANIMATION FROM URL (No file needed)
# ----------------------------------------------------
# ----------------------------------------------------
# LOTTIE ANIMATION (WORKING FIX)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# WORKING INSURANCE LOTTIE URL
lottie_animation = load_lottie_url(
    "https://lottie.host/ff2b0e56-4ad9-48fe-ab45-b222ecf60b45/LZqSzgQFq8.json"
)

if lottie_animation:
    st_lottie(lottie_animation, height=260, key="header")
else:
    st.write("⚠️ Animation unavailable, but app still works.")

# Title Section
# st.markdown("<h1 style='text-align:center; color:white;'>🔮 Insurance Cost Prediction</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; color:#e0e0e0;'>Modern AI-powered prediction with premium UI</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🔮 Insurance Cost Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#999;'>AI-powered premium prediction dashboard</p>", unsafe_allow_html=True)

# ----------------------------------------------------
# INPUT FORM
# ----------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.subheader("📥 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    bmi = st.number_input('BMI', min_value=10.0, max_value=60.0, value=28.5, step=0.1)
    children = st.number_input('Children', min_value=0, max_value=10, value=0)

with col2:
    sex = st.selectbox("Gender", ['Male', 'Female'])
    smoker = st.selectbox('Smoker', ['No', 'Yes'])
    region = st.selectbox('Region', ['Southwest', 'Southeast', 'Northwest', 'Northeast'])

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")


# ----------------------------------------------------
# PREDICTION
# ----------------------------------------------------
if st.button("🚀 Predict Insurance Cost"):
    if not model_loaded:
        st.error("❌ Model not loaded.")
    else:
        # Prepare DataFrame
        input_data = pd.DataFrame({
            'age': [age],
            'sex': [sex.lower()],
            'bmi': [bmi],
            'children': [children],
            'smoker': ['yes' if smoker == 'Yes' else 'no'],
            'region': [region.lower()]
        })

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 📊 Input Summary")
        st.table(input_data)
        st.markdown("</div>", unsafe_allow_html=True)

        # Prediction
        try:
            pred = loaded_model.predict(input_data)[0]

            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("🎯 Prediction Result")

            st.metric("Estimated Annual Insurance Cost", f"${pred:,.2f}")

            st.info(f"""
            Based on the entered details, the predicted annual insurance cost is  
            **${pred:,.2f}**  
            """)

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error during prediction: {str(e)}")


# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='color:white;'>ℹ️ About</h2>", unsafe_allow_html=True)
    st.write("""
    This app predicts annual insurance costs using a trained ML model.

    **Factors considered:**
    - Age  
    - Gender  
    - BMI  
    - Smoking status  
    - Region  
    - Number of children  
    """)

    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit + Machine Learning")
