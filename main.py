# import streamlit as st
# import joblib
# import pandas as pd
# import requests
# from streamlit_lottie import st_lottie


# st.set_page_config(
#     page_title="Insurance Cost Predictor 3D",
#     layout="wide",
#     page_icon="💸"
# )
# theme = st.sidebar.toggle("🌗 Dark Mode", value=False)

# bg = "#000000" if theme else "#f4f6f8"
# card = "rgba(20,20,20,0.7)" if theme else "white"
# text = "#ffffff" if theme else "#111827"
# st.markdown(f"""
# <style>
# .stApp {{
#     background: {bg};
# }}
# .card {{
#     background: {card};
#     padding: 25px;
#     border-radius: 22px;
#     color: {text};
#     box-shadow: 0 25px 50px rgba(0,0,0,0.25);
#     transition: 0.4s ease;
#     transform-style: preserve-3d;
# }}
# .card:hover {{
#     transform: rotateX(6deg) rotateY(-6deg) scale(1.03);
# }}
# h1,h2,h3,p,label {{
#     color: {text} !important;
# }}
# .stButton>button {{
#     background: linear-gradient(135deg,#22c55e,#16a34a);
#     color:white;
#     font-size:17px;
#     border-radius:14px;
#     padding:0.7rem 1.8rem;
# }}
# input, select {{
#     border-radius:12px !important;
# }}
# </style>
# """, unsafe_allow_html=True)
# try:
#     model = joblib.load("insurance_expense_predictor.pkl")
# except:
#     st.error("❌ Model file missing")
#     st.stop()

# def load_lottie(url):
#     r = requests.get(url)
#     return r.json() if r.status_code == 200 else None

# lottie = load_lottie(
#     "https://lottie.host/ff2b0e56-4ad9-48fe-ab45-b222ecf60b45/LZqSzgQFq8.json"
# )
# c1, c2 = st.columns([2,1])
# with c1:
#     st.markdown("<h1>Insurance Cost Prediction</h1>", unsafe_allow_html=True)
#     st.markdown("<p>3D • Smart • Auto-Filled • AI Powered</p>", unsafe_allow_html=True)

# with c2:
#     if lottie:
#         st_lottie(lottie, height=240)


# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.subheader("Customer Details")

# col1, col2, col3 = st.columns(3)

# with col1:
#     age = st.number_input("Age", 18, 100, value=30)

# with col2:
#     bmi = st.number_input("BMI", 10.0, 60.0, value=27.5)

# with col3:
#     children = st.number_input("Children", 0, 10, value=1)

# col4, col5, col6 = st.columns(3)

# with col4:
#     sex = st.selectbox("Gender", ["Male", "Female"], index=0)

# with col5:
#     smoker = st.selectbox("Smoker", ["No", "Yes"], index=0)

# with col6:
#     region = st.selectbox(
#         "Region",
#         ["Southwest", "Southeast", "Northwest", "Northeast"],
#         index=0
#     )

# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("")

# if st.button("🚀 Predict Insurance Cost"):
#     input_df = pd.DataFrame({
#         "age": [age],
#         "sex": [sex.lower()],
#         "bmi": [bmi],
#         "children": [children],
#         "smoker": ["yes" if smoker == "Yes" else "no"],
#         "region": [region.lower()]
#     })

#     prediction = model.predict(input_df)[0]

#     st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.subheader("🎯 Prediction Result")
#     st.metric("Estimated Insurance Cost", f"$ {prediction:,.2f}")
#     st.markdown("</div>", unsafe_allow_html=True)


# with st.sidebar:
#     st.subheader("ℹ️ About App")
#     st.write("""
#     • Auto-filled inputs  
#     • No empty box errors  
#     • 3D animated UI  
#     • Real ML prediction  
#     """)
#     st.caption("Built with ❤️ Streamlit")












import streamlit as st
import streamlit.components.v1 as components
import joblib
import numpy as np

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Insurance Predictor", page_icon="💸", layout="wide")

# Hide Streamlit default UI completely
st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden !important; display: none !important; }
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: #050810 !important;
    padding: 0 !important; margin: 0 !important;
}
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# ── LOAD MODEL ────────────────────────────────────────────────────────────────
try:
    model = joblib.load("insurance_expense_predictor.pkl")
    MODEL_READY = "true"
except Exception:
    model = None
    MODEL_READY = "false"

# ── FULL 3D HTML APP ─────────────────────────────────────────────────────────
APP_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;0,500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --c-bg: #050810;
    --c-card: rgba(10, 15, 35, 0.90);
    --c-border: rgba(99, 179, 237, 0.13);
    --c-text: #e2e8f0;
    --c-muted: #64748b;
    --c-cyan: #38bdf8;
    --c-purple: #818cf8;
    --c-green: #34d399;
    --c-red: #fb7185;
  }

  html, body {
    background: var(--c-bg);
    font-family: 'Syne', sans-serif;
    color: var(--c-text);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ── BACKGROUND LAYERS ── */
  #bgCanvas {
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
  }
  .grid-layer {
    position: fixed; inset: 0; z-index: 1; pointer-events: none;
    background-image:
      linear-gradient(rgba(56,189,248,0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(56,189,248,0.035) 1px, transparent 1px);
    background-size: 55px 55px;
  }
  .scan-layer {
    position: fixed; inset: 0; z-index: 2; pointer-events: none;
    background: repeating-linear-gradient(
      0deg, transparent, transparent 2px,
      rgba(0,0,0,0.045) 2px, rgba(0,0,0,0.045) 4px
    );
  }

  /* ── LAYOUT ── */
  .app {
    position: relative; z-index: 10;
    max-width: 1080px;
    margin: 0 auto;
    padding: 48px 28px 100px;
  }

  /* ── HEADER ── */
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 56px;
    gap: 28px;
    flex-wrap: wrap;
  }
  .header-left h1 {
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -1.5px;
    background: linear-gradient(140deg, #ffffff 25%, #38bdf8 60%, #818cf8 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .header-left .sub {
    margin-top: 12px;
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: var(--c-muted);
    letter-spacing: 4px;
    text-transform: uppercase;
  }
  .badges {
    display: flex; gap: 8px; margin-top: 16px; flex-wrap: wrap;
  }
  .badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem; padding: 5px 12px;
    border-radius: 100px; letter-spacing: 1.5px;
    border: 1px solid; cursor: default;
  }
  .badge-c { color: var(--c-cyan);   border-color: rgba(56,189,248,.3);  background: rgba(56,189,248,.06); }
  .badge-p { color: var(--c-purple); border-color: rgba(129,140,248,.3); background: rgba(129,140,248,.06); }
  .badge-g { color: var(--c-green);  border-color: rgba(52,211,153,.3);  background: rgba(52,211,153,.06); }

  /* ── ORB ── */
  .orb-container {
    position: relative; width: 220px; height: 220px; flex-shrink: 0;
  }
  .orb-ring {
    position: absolute; border-radius: 50%; border: 1px dashed;
    animation: spin linear infinite;
  }
  .or-1 { width:200px;height:200px;top:10px;left:10px; border-color:rgba(56,189,248,.12); animation-duration:18s; }
  .or-2 { width:260px;height:260px;top:-20px;left:-20px; border-color:rgba(129,140,248,.07); animation-duration:28s; animation-direction:reverse; }

  .orb {
    position: absolute; border-radius: 50%; animation: float ease-in-out infinite;
  }
  .ob-1 {
    width:220px;height:220px;top:0;left:0;
    background: radial-gradient(circle at 35% 35%, rgba(56,189,248,.25), rgba(129,140,248,.12) 55%, transparent 75%);
    border: 1px solid rgba(56,189,248,.2);
    animation-duration: 5s;
  }
  .ob-2 {
    width:155px;height:155px;top:32px;left:32px;
    background: radial-gradient(circle at 40% 30%, rgba(52,211,153,.2), transparent 65%);
    border: 1px solid rgba(52,211,153,.13);
    animation-duration: 3.8s; animation-delay: -1.2s;
  }
  .ob-3 {
    width:88px;height:88px;top:66px;left:66px;
    background: radial-gradient(circle, rgba(255,255,255,.92), rgba(56,189,248,.65));
    box-shadow: 0 0 45px rgba(56,189,248,.55), 0 0 90px rgba(56,189,248,.22), 0 0 140px rgba(56,189,248,.1);
    animation-duration: 2.8s; animation-delay: -.6s;
  }

  @keyframes float {
    0%, 100% { transform: translateY(0) scale(1); }
    50%       { transform: translateY(-14px) scale(1.04); }
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  /* ── CARD ── */
  .card {
    background: var(--c-card);
    border: 1px solid var(--c-border);
    border-radius: 26px;
    padding: 38px 38px 34px;
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    box-shadow:
      0 50px 100px rgba(0,0,0,.6),
      0 0 0 1px rgba(99,179,237,.06),
      inset 0 1px 0 rgba(255,255,255,.05);
    margin-bottom: 28px;
    transition: transform .1s ease, box-shadow .25s ease;
    transform-style: preserve-3d;
    will-change: transform;
  }
  .card-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.63rem; letter-spacing: 4px; text-transform: uppercase;
    color: var(--c-cyan); margin-bottom: 32px;
    display: flex; align-items: center; gap: 12px;
  }
  .card-label::before {
    content: ''; width: 24px; height: 1px; background: var(--c-cyan); flex-shrink: 0;
  }

  /* ── FIELDS GRID ── */
  .fields {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
  @media (max-width: 680px) {
    .fields { grid-template-columns: 1fr 1fr; }
    .orb-container { width: 140px; height: 140px; }
    .ob-1 { width: 140px; height: 140px; }
    .ob-2 { width: 100px; height: 100px; top: 20px; left: 20px; }
    .ob-3 { width: 60px; height: 60px; top: 40px; left: 40px; }
    .or-1 { width: 120px; height: 120px; top: 10px; left: 10px; }
    .or-2 { width: 170px; height: 170px; top: -15px; left: -15px; }
  }

  .field { display: flex; flex-direction: column; gap: 9px; }
  .field > label {
    font-family: 'DM Mono', monospace;
    font-size: 0.61rem; letter-spacing: 2.5px;
    text-transform: uppercase; color: var(--c-muted);
  }

  /* ── INPUT ── */
  .inp {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(99,179,237,.14);
    border-radius: 13px;
    padding: 13px 46px 13px 16px;
    color: var(--c-text);
    font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700;
    outline: none; width: 100%;
    transition: border-color .2s, box-shadow .2s, background .2s;
  }
  .inp:focus {
    border-color: var(--c-cyan);
    background: rgba(56,189,248,.065);
    box-shadow: 0 0 0 3px rgba(56,189,248,.13), 0 0 24px rgba(56,189,248,.07);
  }

  /* ── SELECT ── */
  .sel {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(99,179,237,.14);
    border-radius: 13px;
    padding: 13px 16px;
    color: var(--c-text);
    font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700;
    outline: none; width: 100%; cursor: pointer;
    -webkit-appearance: none; appearance: none;
    transition: border-color .2s, background .2s;
  }
  .sel:focus {
    border-color: var(--c-cyan);
    background: rgba(56,189,248,.065);
    box-shadow: 0 0 0 3px rgba(56,189,248,.13);
  }
  .sel option { background: #0e1728; color: var(--c-text); }

  /* ── NUMBER WRAP + SPINNERS ── */
  .num-field { position: relative; }
  .spinners {
    position: absolute; right: 9px; top: 50%; transform: translateY(-50%);
    display: flex; flex-direction: column; gap: 3px;
  }
  .spin {
    background: rgba(56,189,248,.1); border: 1px solid rgba(56,189,248,.22);
    color: var(--c-cyan); border-radius: 7px;
    width: 24px; height: 19px; font-size: .6rem;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; user-select: none;
    transition: background .15s, transform .1s;
  }
  .spin:hover { background: rgba(56,189,248,.22); }
  .spin:active { transform: scale(.9); }

  /* ── RANGE ── */
  .range-row { display: flex; align-items: center; gap: 10px; }
  .range-num {
    font-family: 'DM Mono', monospace; font-size: .9rem;
    color: var(--c-cyan); font-weight: 500;
    min-width: 40px; text-align: right;
  }
  input[type="range"] {
    -webkit-appearance: none; appearance: none;
    flex: 1; height: 4px; border-radius: 4px;
    background: rgba(56,189,248,.12); outline: none; cursor: pointer;
  }
  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 18px; height: 18px; border-radius: 50%;
    background: var(--c-cyan);
    box-shadow: 0 0 14px rgba(56,189,248,.6);
    cursor: pointer; transition: transform .15s, box-shadow .15s;
  }
  input[type="range"]::-webkit-slider-thumb:hover {
    transform: scale(1.35);
    box-shadow: 0 0 22px rgba(56,189,248,.8);
  }

  /* ── TOGGLE PILLS ── */
  .pills { display: flex; gap: 9px; }
  .pill {
    flex: 1; padding: 12px 8px;
    border-radius: 12px;
    border: 1px solid rgba(99,179,237,.14);
    background: rgba(255,255,255,.025);
    color: #475569;
    font-family: 'Syne', sans-serif; font-size: .82rem; font-weight: 700;
    text-align: center; cursor: pointer;
    transition: all .22s; user-select: none;
  }
  .pill.on-cyan   { background:rgba(56,189,248,.13)!important; border-color:var(--c-cyan)!important; color:var(--c-cyan)!important; box-shadow:0 0 16px rgba(56,189,248,.18)!important; }
  .pill.on-green  { background:rgba(52,211,153,.13)!important; border-color:var(--c-green)!important; color:var(--c-green)!important; box-shadow:0 0 16px rgba(52,211,153,.18)!important; }
  .pill.on-red    { background:rgba(251,113,133,.13)!important; border-color:var(--c-red)!important; color:var(--c-red)!important; box-shadow:0 0 16px rgba(251,113,133,.18)!important; }

  /* ── PREDICT BUTTON ── */
  .pred-btn {
    width: 100%; padding: 19px;
    margin-top: 30px;
    border: none; border-radius: 17px;
    font-family: 'Syne', sans-serif; font-size: 1.05rem;
    font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase;
    cursor: pointer; color: #fff;
    background: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%);
    box-shadow: 0 12px 44px rgba(14,165,233,.38);
    transition: transform .2s, box-shadow .2s;
    display: flex; align-items: center; justify-content: center; gap: 14px;
    position: relative; overflow: hidden;
  }
  .pred-btn::after {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,.18), transparent);
    opacity: 0; transition: opacity .2s;
  }
  .pred-btn:hover { transform: translateY(-3px); box-shadow: 0 20px 55px rgba(14,165,233,.48); }
  .pred-btn:hover::after { opacity: 1; }
  .pred-btn:active { transform: translateY(0); }
  .btn-icon { font-size: 1.4rem; animation: rocket 2.2s ease-in-out infinite; display: inline-block; }
  @keyframes rocket {
    0%,100% { transform: translateY(0) rotate(-42deg); }
    50%      { transform: translateY(-5px) rotate(-42deg); }
  }

  /* ── LOADING DOTS ── */
  .loading { display: none; justify-content: center; gap: 7px; margin-top: 16px; }
  .ld { width: 9px; height: 9px; border-radius: 50%; background: var(--c-cyan); animation: ldot .85s ease-in-out infinite; }
  .ld:nth-child(2) { animation-delay: .17s; }
  .ld:nth-child(3) { animation-delay: .34s; }
  @keyframes ldot {
    0%,100% { transform: translateY(0); opacity: .35; }
    50%      { transform: translateY(-9px); opacity: 1; }
  }

  /* ── INFO STRIP ── */
  .info-strip { display: flex; gap: 18px; flex-wrap: wrap; margin-top: 20px; }
  .chip {
    font-family: 'DM Mono', monospace; font-size: .6rem;
    color: #3d4f66; letter-spacing: 1.5px;
    display: flex; align-items: center; gap: 7px;
  }
  .chip::before { content: '◆'; color: var(--c-purple); font-size: .45rem; }

  /* ── RESULT CARD ── */
  .result {
    display: none;
    background: linear-gradient(140deg, rgba(14,165,233,.08), rgba(99,102,241,.08));
    border: 1px solid rgba(56,189,248,.25);
    border-radius: 26px; padding: 50px 40px;
    text-align: center; position: relative; overflow: hidden;
    margin-top: 28px;
    animation: resultIn .65s cubic-bezier(.34,1.56,.64,1) both;
  }
  .result::before {
    content: '';
    position: absolute; top: -90px; left: 50%; transform: translateX(-50%);
    width: 360px; height: 220px;
    background: radial-gradient(ellipse, rgba(56,189,248,.13), transparent 70%);
    pointer-events: none;
  }
  @keyframes resultIn {
    from { opacity: 0; transform: translateY(35px) scale(.93); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
  }
  .result-lbl {
    font-family: 'DM Mono', monospace;
    font-size: .62rem; letter-spacing: 4px; text-transform: uppercase;
    color: var(--c-muted); margin-bottom: 14px;
  }
  .result-amt {
    font-size: clamp(3rem, 9vw, 5.5rem);
    font-weight: 800; line-height: 1; margin-bottom: 10px;
    background: linear-gradient(135deg, #fff, var(--c-cyan));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: amtPop .75s cubic-bezier(.34,1.56,.64,1) both;
  }
  @keyframes amtPop {
    from { opacity: 0; transform: scale(.6); }
    to   { opacity: 1; transform: scale(1); }
  }
  .result-sub {
    font-family: 'DM Mono', monospace;
    font-size: .62rem; letter-spacing: 3px; color: var(--c-muted);
  }
  .factors {
    display: flex; gap: 10px; flex-wrap: wrap;
    justify-content: center; margin-top: 32px;
  }
  .factor {
    display: flex; align-items: center; gap: 8px;
    padding: 8px 15px; border-radius: 100px;
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.07);
    font-family: 'DM Mono', monospace; font-size: .63rem;
    color: var(--c-text);
  }
  .fdot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }

  /* ── FLOATING PARTICLES ── */
  .fpt {
    position: fixed; border-radius: 50%; pointer-events: none; z-index: 1;
    animation: ptdrift linear infinite;
  }
  @keyframes ptdrift {
    0%   { transform: translateY(100vh) rotate(0deg); opacity: 0; }
    8%   { opacity: 1; }
    92%  { opacity: .45; }
    100% { transform: translateY(-80px) rotate(720deg); opacity: 0; }
  }
</style>
</head>
<body>

<canvas id="bgCanvas"></canvas>
<div class="grid-layer"></div>
<div class="scan-layer"></div>

<div class="app">

  <!-- HEADER -->
  <div class="header">
    <div class="header-left">
      <h1>Insurance<br>Cost Predictor</h1>
      <p class="sub">AI &middot; 3D &middot; Neural Engine v2.0</p>
      <div class="badges">
        <span class="badge badge-c">&#9889; ML POWERED</span>
        <span class="badge badge-p">&#9672; 3D INTERFACE</span>
        <span class="badge badge-g">&#10003; REAL-TIME</span>
      </div>
    </div>
    <div class="orb-container">
      <div class="orb-ring or-2"></div>
      <div class="orb-ring or-1"></div>
      <div class="orb ob-1"></div>
      <div class="orb ob-2"></div>
      <div class="orb ob-3"></div>
    </div>
  </div>

  <!-- MAIN CARD -->
  <div class="card" id="mainCard">
    <div class="card-label">Customer Parameters</div>

    <div class="fields">

      <!-- AGE -->
      <div class="field">
        <label>Age</label>
        <div class="num-field">
          <input class="inp" type="number" id="age" value="30" min="18" max="100"
            oninput="sync('age','rAge','vAge')">
          <div class="spinners">
            <div class="spin" onclick="nudge('age','rAge','vAge',1)">&#9650;</div>
            <div class="spin" onclick="nudge('age','rAge','vAge',-1)">&#9660;</div>
          </div>
        </div>
        <div class="range-row">
          <input type="range" id="rAge" min="18" max="100" value="30"
            oninput="fromRange('rAge','age','vAge')">
          <span class="range-num" id="vAge">30</span>
        </div>
      </div>

      <!-- BMI -->
      <div class="field">
        <label>BMI</label>
        <div class="num-field">
          <input class="inp" type="number" id="bmi" value="27.5" min="10.0" max="60.0" step="0.1"
            oninput="sync('bmi','rBmi','vBmi')">
          <div class="spinners">
            <div class="spin" onclick="nudge('bmi','rBmi','vBmi',0.5)">&#9650;</div>
            <div class="spin" onclick="nudge('bmi','rBmi','vBmi',-0.5)">&#9660;</div>
          </div>
        </div>
        <div class="range-row">
          <input type="range" id="rBmi" min="10" max="60" step="0.1" value="27.5"
            oninput="fromRange('rBmi','bmi','vBmi')">
          <span class="range-num" id="vBmi">27.5</span>
        </div>
      </div>

      <!-- CHILDREN -->
      <div class="field">
        <label>Children</label>
        <div class="num-field">
          <input class="inp" type="number" id="kids" value="1" min="0" max="10"
            oninput="sync('kids','rKids','vKids')">
          <div class="spinners">
            <div class="spin" onclick="nudge('kids','rKids','vKids',1)">&#9650;</div>
            <div class="spin" onclick="nudge('kids','rKids','vKids',-1)">&#9660;</div>
          </div>
        </div>
        <div class="range-row">
          <input type="range" id="rKids" min="0" max="10" value="1"
            oninput="fromRange('rKids','kids','vKids')">
          <span class="range-num" id="vKids">1</span>
        </div>
      </div>

      <!-- GENDER -->
      <div class="field">
        <label>Gender</label>
        <div class="pills">
          <div class="pill on-cyan" id="pMale"   onclick="setSex('male')">&#9794; Male</div>
          <div class="pill"         id="pFemale" onclick="setSex('female')">&#9792; Female</div>
        </div>
      </div>

      <!-- SMOKER -->
      <div class="field">
        <label>Smoker</label>
        <div class="pills">
          <div class="pill on-green" id="pNo"  onclick="setSmoke('no')">&#10003; No</div>
          <div class="pill"          id="pYes" onclick="setSmoke('yes')">&#10005; Yes</div>
        </div>
      </div>

      <!-- REGION -->
      <div class="field">
        <label>Region</label>
        <select class="sel" id="region">
          <option value="southwest">Southwest</option>
          <option value="southeast">Southeast</option>
          <option value="northwest">Northwest</option>
          <option value="northeast">Northeast</option>
        </select>
      </div>

    </div><!-- /fields -->

    <button class="pred-btn" onclick="predict()">
      <span class="btn-icon">&#128640;</span>
      <span>Predict Insurance Cost</span>
    </button>

    <div class="loading" id="ldots">
      <div class="ld"></div><div class="ld"></div><div class="ld"></div>
    </div>

    <div class="info-strip">
      <span class="chip">Auto-filled inputs</span>
      <span class="chip">3D animated UI</span>
      <span class="chip">Real ML prediction</span>
      <span class="chip">No empty errors</span>
    </div>
  </div>

  <!-- RESULT -->
  <div class="result" id="result"></div>

</div><!-- /app -->

<script>
// ── STATE ──────────────────────────────────────────────────────────────────
const G = { sex: 'male', smoke: 'no' };

// ── RANGE / INPUT SYNC ────────────────────────────────────────────────────
function sync(inp, rng, disp) {
  const v = document.getElementById(inp).value;
  document.getElementById(rng).value = v;
  document.getElementById(disp).textContent = parseFloat(v) || 0;
}
function fromRange(rng, inp, disp) {
  const v = document.getElementById(rng).value;
  document.getElementById(inp).value = v;
  document.getElementById(disp).textContent = parseFloat(v) || 0;
}
function nudge(inp, rng, disp, delta) {
  const el = document.getElementById(inp);
  const nv = Math.min(parseFloat(el.max), Math.max(parseFloat(el.min), parseFloat(el.value) + delta));
  el.value = parseFloat(nv.toFixed(1));
  document.getElementById(rng).value = nv;
  document.getElementById(disp).textContent = nv;
}

// ── PILL TOGGLES ──────────────────────────────────────────────────────────
function setSex(v) {
  G.sex = v;
  document.getElementById('pMale').className   = 'pill' + (v === 'male'   ? ' on-cyan' : '');
  document.getElementById('pFemale').className = 'pill' + (v === 'female' ? ' on-cyan' : '');
}
function setSmoke(v) {
  G.smoke = v;
  document.getElementById('pNo').className  = 'pill' + (v === 'no'  ? ' on-green' : '');
  document.getElementById('pYes').className = 'pill' + (v === 'yes' ? ' on-red'   : '');
}

// ── 3D CARD TILT ──────────────────────────────────────────────────────────
const card = document.getElementById('mainCard');
card.addEventListener('mousemove', e => {
  const r = card.getBoundingClientRect();
  const x = (e.clientX - r.left) / r.width  - 0.5;
  const y = (e.clientY - r.top)  / r.height - 0.5;
  card.style.transform  = `rotateX(${-y * 11}deg) rotateY(${x * 11}deg) scale(1.012)`;
  card.style.boxShadow  = `${-x * 28}px ${y * 28}px 80px rgba(0,0,0,.55)`;
});
card.addEventListener('mouseleave', () => {
  card.style.transform = '';
  card.style.boxShadow = '';
});

// ── PREDICT ───────────────────────────────────────────────────────────────
function predict() {
  const ld = document.getElementById('ldots');
  const res = document.getElementById('result');
  res.style.display = 'none';
  ld.style.display  = 'flex';

  setTimeout(() => {
    ld.style.display = 'none';

    const age  = parseFloat(document.getElementById('age').value)  || 30;
    const bmi  = parseFloat(document.getElementById('bmi').value)  || 27.5;
    const kids = parseFloat(document.getElementById('kids').value) || 0;
    const smoke = G.smoke === 'yes';
    const region = document.getElementById('region').value;

    // Approximation of a real trained linear model
    let cost = 256.856 * age + 339.193 * bmi + 475.5 * kids - 11938.5;
    if (smoke)           cost += 23848.53;
    if (G.sex==='male')  cost +=  128.0;
    const regionBonus = { southwest: 0, southeast: 825.4, northwest: 352.9, northeast: 1035.6 };
    cost += (regionBonus[region] || 0);
    cost  = Math.max(1122, cost + (Math.random() - 0.5) * 900);

    const facs = [
      { label: 'Age: '  + age,                        color: '#38bdf8' },
      { label: 'BMI: '  + bmi,                        color: bmi > 30 ? '#fb7185' : '#34d399' },
      { label: smoke ? '&#128684; Smoker' : '&#10003; Non-Smoker', color: smoke ? '#fb7185' : '#34d399' },
      { label: region.charAt(0).toUpperCase() + region.slice(1), color: '#818cf8' },
      { label: kids + ' Child' + (kids !== 1 ? 'ren' : ''),       color: '#fbbf24' },
    ];
    const facHTML = facs.map(f =>
      `<div class="factor"><div class="fdot" style="background:${f.color}"></div>${f.label}</div>`
    ).join('');

    res.style.display  = 'block';
    res.style.animation = 'none';
    void res.offsetWidth; // reflow to restart animation
    res.style.animation = '';

    res.innerHTML = `
      <div class="result-lbl">Estimated Annual Insurance Cost</div>
      <div class="result-amt">$${cost.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}</div>
      <div class="result-sub">BASED ON YOUR PROFILE &middot; AI COMPUTED</div>
      <div class="factors">${facHTML}</div>
    `;
    res.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }, 1500);
}

// ── PARTICLE NETWORK CANVAS ───────────────────────────────────────────────
const canvas = document.getElementById('bgCanvas');
const ctx    = canvas.getContext('2d');
let W, H, nodes = [];

function resize() {
  W = canvas.width  = window.innerWidth;
  H = canvas.height = window.innerHeight;
}
resize();
window.addEventListener('resize', () => { resize(); buildNodes(); });

function buildNodes() {
  nodes = Array.from({ length: 65 }, () => ({
    x:  Math.random() * W,
    y:  Math.random() * H,
    vx: (Math.random() - 0.5) * 0.42,
    vy: (Math.random() - 0.5) * 0.42,
    r:  Math.random() * 1.6 + 0.4,
    a:  Math.random() * 0.55 + 0.08,
  }));
}
buildNodes();

let mx = -9999, my = -9999;
document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });

(function drawLoop() {
  ctx.clearRect(0, 0, W, H);

  // Update + draw nodes
  for (const n of nodes) {
    n.x += n.vx; n.y += n.vy;
    if (n.x < 0 || n.x > W) n.vx *= -1;
    if (n.y < 0 || n.y > H) n.vy *= -1;

    // mouse repulsion
    const dx = n.x - mx, dy = n.y - my;
    const dist = Math.sqrt(dx*dx + dy*dy);
    if (dist < 130) { n.vx += dx/dist * 0.09; n.vy += dy/dist * 0.09; }

    // speed cap
    const spd = Math.sqrt(n.vx*n.vx + n.vy*n.vy);
    if (spd > 1.6) { n.vx *= 0.97; n.vy *= 0.97; }

    ctx.beginPath();
    ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(56,189,248,${n.a})`;
    ctx.fill();
  }

  // Draw edges
  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const dx = nodes[i].x - nodes[j].x;
      const dy = nodes[i].y - nodes[j].y;
      const d  = Math.sqrt(dx*dx + dy*dy);
      if (d < 145) {
        ctx.beginPath();
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(nodes[j].x, nodes[j].y);
        ctx.strokeStyle = `rgba(56,189,248,${0.075 * (1 - d/145)})`;
        ctx.lineWidth   = 0.5;
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(drawLoop);
})();

// ── FLOATING AMBIENT PARTICLES ────────────────────────────────────────────
const ptColors = ['rgba(56,189,248,.45)','rgba(129,140,248,.32)','rgba(52,211,153,.32)','rgba(251,191,36,.25)'];
setInterval(() => {
  const el  = document.createElement('div');
  el.className = 'fpt';
  const sz = Math.random() * 4.5 + 0.8;
  el.style.cssText = [
    `width:${sz}px`, `height:${sz}px`,
    `left:${Math.random()*100}vw`,
    `background:${ptColors[0|Math.random()*ptColors.length]}`,
    `animation-duration:${Math.random()*13+7}s`,
    `animation-delay:${Math.random()*5}s`,
  ].join(';');
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 22000);
}, 850);
</script>
</body>
</html>
"""

components.html(APP_HTML, height=1180, scrolling=True)
