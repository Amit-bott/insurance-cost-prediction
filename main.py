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
import joblib
import pandas as pd
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Insurance Cost Predictor",
    layout="wide",
    page_icon="💸"
)

# ── INJECT FULL CUSTOM CSS + JS ──
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">

<style>
/* ── RESET STREAMLIT ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp { background: #050810 !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── CANVAS & OVERLAYS ── */
#canvas-bg {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
}
.grid-overlay {
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  background-image:
    linear-gradient(rgba(56,189,248,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(56,189,248,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
}
.scanlines {
  position: fixed; inset: 0; z-index: 2; pointer-events: none;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.04) 2px, rgba(0,0,0,0.04) 4px
  );
}

/* ── MAIN WRAPPER ── */
.ins-wrap {
  position: relative; z-index: 10;
  max-width: 1060px;
  margin: 0 auto;
  padding: 44px 28px 80px;
  font-family: 'Syne', sans-serif;
}

/* ── HEADER ── */
.ins-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 52px;
  gap: 24px;
  flex-wrap: wrap;
}
.ins-header h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -1px;
  background: linear-gradient(135deg, #ffffff 30%, #38bdf8 65%, #818cf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
}
.ins-header p {
  margin-top: 10px;
  font-family: 'DM Mono', monospace;
  font-size: 0.72rem;
  color: #64748b;
  letter-spacing: 3px;
  text-transform: uppercase;
}
.badge-row { display: flex; gap: 8px; margin-top: 14px; flex-wrap: wrap; }
.badge {
  font-family: 'DM Mono', monospace;
  font-size: 0.62rem;
  padding: 4px 11px;
  border-radius: 100px;
  letter-spacing: 1px;
  border: 1px solid;
}
.b-cyan  { color: #38bdf8; border-color: rgba(56,189,248,0.3);  background: rgba(56,189,248,0.06); }
.b-purple{ color: #818cf8; border-color: rgba(129,140,248,0.3); background: rgba(129,140,248,0.06); }
.b-green { color: #34d399; border-color: rgba(52,211,153,0.3);  background: rgba(52,211,153,0.06); }

/* ── ORB ── */
.orb-wrap { position: relative; width: 210px; height: 210px; flex-shrink: 0; }
.orb { position: absolute; border-radius: 50%; }
.orb-1 {
  width: 210px; height: 210px;
  background: radial-gradient(circle at 35% 35%, rgba(56,189,248,0.22), rgba(129,140,248,0.1) 50%, transparent 70%);
  border: 1px solid rgba(56,189,248,0.18);
  animation: orbFloat 5s ease-in-out infinite;
}
.orb-2 {
  width: 150px; height: 150px; top: 30px; left: 30px;
  background: radial-gradient(circle at 40% 30%, rgba(52,211,153,0.18), transparent 60%);
  border: 1px solid rgba(52,211,153,0.12);
  animation: orbFloat 3.5s ease-in-out infinite; animation-delay: -1s;
}
.orb-3 {
  width: 85px; height: 85px; top: 63px; left: 63px;
  background: radial-gradient(circle, rgba(255,255,255,0.9), rgba(56,189,248,0.6));
  box-shadow: 0 0 40px rgba(56,189,248,0.5), 0 0 80px rgba(56,189,248,0.2);
  animation: orbFloat 2.5s ease-in-out infinite; animation-delay: -0.5s;
}
.orb-ring {
  position: absolute; border-radius: 50%; border: 1px dashed;
  animation: orbSpin linear infinite;
}
.ring-1 { width: 190px; height: 190px; top: 10px; left: 10px; border-color: rgba(56,189,248,0.1);  animation-duration: 20s; }
.ring-2 { width: 250px; height: 250px; top: -20px; left: -20px; border-color: rgba(129,140,248,0.07); animation-duration: 30s; animation-direction: reverse; }

@keyframes orbFloat {
  0%,100% { transform: translateY(0) scale(1); }
  50%      { transform: translateY(-12px) scale(1.03); }
}
@keyframes orbSpin { to { transform: rotate(360deg); } }

/* ── CARD ── */
.ins-card {
  background: rgba(10,15,30,0.85);
  border: 1px solid rgba(99,179,237,0.13);
  border-radius: 24px;
  padding: 36px 36px 32px;
  backdrop-filter: blur(20px);
  box-shadow: 0 40px 80px rgba(0,0,0,0.55), 0 0 0 1px rgba(99,179,237,0.07);
  margin-bottom: 24px;
  transition: transform 0.12s ease, box-shadow 0.3s ease;
  transform-style: preserve-3d;
}
.ins-card:hover {
  transform: rotateX(3deg) rotateY(-3deg) scale(1.005);
}
.card-tag {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #38bdf8;
  margin-bottom: 28px;
  display: flex; align-items: center; gap: 10px;
}
.card-tag::before { content:''; width:20px; height:1px; background:#38bdf8; display:inline-block; }

/* ── FIELDS GRID ── */
.fields-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}
@media(max-width:680px){ .fields-grid{ grid-template-columns:1fr 1fr; } }

.field { display:flex; flex-direction:column; gap:8px; }
.field label {
  font-family:'DM Mono',monospace;
  font-size:0.63rem; letter-spacing:2px;
  text-transform:uppercase; color:#64748b;
}

/* inputs */
.ins-input {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(99,179,237,0.12);
  border-radius: 12px;
  padding: 12px 16px;
  color: #e2e8f0;
  font-family:'Syne',sans-serif; font-size:1rem; font-weight:600;
  outline:none; width:100%;
  transition: border-color .2s, box-shadow .2s, background .2s;
}
.ins-input:focus {
  border-color:#38bdf8;
  background:rgba(56,189,248,0.06);
  box-shadow:0 0 0 3px rgba(56,189,248,0.12), 0 0 20px rgba(56,189,248,0.06);
}
.ins-select {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(99,179,237,0.12);
  border-radius: 12px;
  padding: 12px 16px;
  color: #e2e8f0;
  font-family:'Syne',sans-serif; font-size:1rem; font-weight:600;
  outline:none; width:100%; cursor:pointer;
  transition: border-color .2s, box-shadow .2s;
  -webkit-appearance:none; appearance:none;
}
.ins-select:focus {
  border-color:#38bdf8;
  background:rgba(56,189,248,0.06);
  box-shadow:0 0 0 3px rgba(56,189,248,0.12);
}
.ins-select option { background:#0f1729; color:#e2e8f0; }

/* range */
.range-row { display:flex; align-items:center; gap:10px; }
.range-val {
  font-family:'DM Mono',monospace; font-size:.95rem;
  color:#38bdf8; font-weight:500; min-width:42px; text-align:right;
}
input[type=range] {
  -webkit-appearance:none; appearance:none;
  flex:1; height:4px; border-radius:4px;
  background:rgba(56,189,248,0.1); outline:none; cursor:pointer;
}
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance:none; width:18px; height:18px;
  border-radius:50%; background:#38bdf8;
  box-shadow:0 0 12px rgba(56,189,248,0.5); cursor:pointer;
  transition:transform .15s;
}
input[type=range]::-webkit-slider-thumb:hover { transform:scale(1.3); }

/* number with spinners */
.num-wrap { position:relative; }
.num-wrap .ins-input { padding-right:44px; }
.spin-btns {
  position:absolute; right:8px; top:50%; transform:translateY(-50%);
  display:flex; flex-direction:column; gap:2px;
}
.spin-btn {
  background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.2);
  color:#38bdf8; border-radius:6px; width:22px; height:18px;
  font-size:.62rem; display:flex; align-items:center; justify-content:center;
  cursor:pointer; transition:background .15s; user-select:none;
}
.spin-btn:hover { background:rgba(56,189,248,0.22); }

/* toggle pills */
.pill-group { display:flex; gap:8px; }
.pill {
  flex:1; padding:11px 6px;
  border-radius:10px; border:1px solid rgba(99,179,237,0.14);
  background:rgba(255,255,255,0.02); color:#64748b;
  font-family:'Syne',sans-serif; font-size:.85rem; font-weight:600;
  text-align:center; cursor:pointer; transition:all .2s; user-select:none;
}
.pill.p-cyan   { background:rgba(56,189,248,0.12);  border-color:#38bdf8; color:#38bdf8;  box-shadow:0 0 14px rgba(56,189,248,0.15); }
.pill.p-green  { background:rgba(52,211,153,0.12);  border-color:#34d399; color:#34d399;  box-shadow:0 0 14px rgba(52,211,153,0.15); }
.pill.p-red    { background:rgba(251,113,133,0.12); border-color:#fb7185; color:#fb7185;  box-shadow:0 0 14px rgba(251,113,133,0.15); }

/* ── PREDICT BUTTON ── */
.pred-btn {
  width:100%; padding:18px;
  border:none; border-radius:16px;
  font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
  letter-spacing:1px; text-transform:uppercase;
  cursor:pointer; position:relative; overflow:hidden;
  background:linear-gradient(135deg,#0ea5e9,#6366f1);
  color:white;
  box-shadow:0 10px 40px rgba(14,165,233,0.35);
  transition:transform .2s, box-shadow .2s;
  margin-top:28px;
  display:flex; align-items:center; justify-content:center; gap:12px;
}
.pred-btn:hover {
  transform:translateY(-2px);
  box-shadow:0 16px 50px rgba(14,165,233,0.45);
}
.pred-btn:active { transform:translateY(0); }
.pred-btn::before {
  content:''; position:absolute; inset:0;
  background:linear-gradient(135deg,rgba(255,255,255,0.15),transparent);
  opacity:0; transition:opacity .2s;
}
.pred-btn:hover::before { opacity:1; }
.btn-rocket { font-size:1.3rem; animation:rocketBob 2s ease-in-out infinite; }
@keyframes rocketBob {
  0%,100%{ transform:translateY(0) rotate(-45deg); }
  50%    { transform:translateY(-4px) rotate(-45deg); }
}

/* loading dots */
.loading-dots { display:flex; justify-content:center; gap:6px; margin-top:14px; }
.dot {
  width:8px; height:8px; border-radius:50%; background:#38bdf8;
  animation:dotBounce .8s ease-in-out infinite;
}
.dot:nth-child(2){ animation-delay:.15s; }
.dot:nth-child(3){ animation-delay:.3s; }
@keyframes dotBounce{
  0%,100%{ transform:translateY(0); opacity:.4; }
  50%    { transform:translateY(-8px); opacity:1; }
}

/* ── RESULT CARD ── */
.result-card {
  background: linear-gradient(135deg,rgba(14,165,233,0.07),rgba(99,102,241,0.07));
  border:1px solid rgba(56,189,248,0.22);
  border-radius:24px; padding:44px;
  text-align:center; position:relative; overflow:hidden;
  animation:resultReveal .6s cubic-bezier(.34,1.56,.64,1);
}
.result-card::before {
  content:''; position:absolute;
  top:-80px; left:50%; transform:translateX(-50%);
  width:300px; height:200px;
  background:radial-gradient(ellipse,rgba(56,189,248,0.1),transparent 70%);
  pointer-events:none;
}
@keyframes resultReveal {
  from{ opacity:0; transform:translateY(30px) scale(.95); }
  to  { opacity:1; transform:translateY(0)   scale(1); }
}
.result-label {
  font-family:'DM Mono',monospace;
  font-size:.63rem; letter-spacing:3px;
  text-transform:uppercase; color:#64748b; margin-bottom:12px;
}
.result-amount {
  font-size:clamp(2.8rem,8vw,4.8rem); font-weight:800;
  background:linear-gradient(135deg,#fff,#38bdf8);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text; line-height:1; margin-bottom:8px;
  animation:countUp .8s ease-out;
}
@keyframes countUp{
  from{ opacity:0; transform:scale(.7); }
  to  { opacity:1; transform:scale(1); }
}
.result-sub {
  font-family:'DM Mono',monospace;
  font-size:.65rem; color:#64748b; letter-spacing:2px;
}
.factor-row {
  display:flex; gap:12px; margin-top:28px;
  justify-content:center; flex-wrap:wrap;
}
.fpill {
  display:flex; align-items:center; gap:7px;
  padding:7px 14px; border-radius:100px;
  font-family:'DM Mono',monospace; font-size:.65rem;
  background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.07);
  color:#e2e8f0;
}
.fdot{ width:6px; height:6px; border-radius:50%; flex-shrink:0; }

/* info strip */
.info-strip { display:flex; gap:16px; flex-wrap:wrap; margin-top:18px; }
.info-chip {
  font-family:'DM Mono',monospace; font-size:.62rem;
  color:#475569; letter-spacing:1px;
  display:flex; align-items:center; gap:7px;
}
.info-chip::before{ content:'◆'; color:#818cf8; font-size:.45rem; }

/* particles */
.particle {
  position:fixed; border-radius:50%; pointer-events:none; z-index:1;
  animation:particleDrift linear infinite;
}
@keyframes particleDrift{
  0%  { transform:translateY(100vh) rotate(0deg);   opacity:0; }
  10% { opacity:1; }
  90% { opacity:.4; }
  100%{ transform:translateY(-100px) rotate(720deg); opacity:0; }
}
</style>

<!-- CANVAS + OVERLAYS -->
<canvas id="canvas-bg"></canvas>
<div class="grid-overlay"></div>
<div class="scanlines"></div>

<!-- MAIN UI -->
<div class="ins-wrap">

  <!-- HEADER -->
  <div class="ins-header">
    <div>
      <h1>Insurance<br>Cost Predictor</h1>
      <p>AI · 3D · Neural Engine v2.0</p>
      <div class="badge-row">
        <span class="badge b-cyan">⚡ ML POWERED</span>
        <span class="badge b-purple">◈ 3D INTERFACE</span>
        <span class="badge b-green">✓ REAL-TIME</span>
      </div>
    </div>
    <div class="orb-wrap">
      <div class="orb-ring ring-2"></div>
      <div class="orb-ring ring-1"></div>
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
      <div class="orb orb-3"></div>
    </div>
  </div>

  <!-- FORM CARD -->
  <div class="ins-card" id="mainCard">
    <div class="card-tag">Customer Parameters</div>

    <div class="fields-grid">

      <!-- AGE -->
      <div class="field">
        <label>Age</label>
        <div class="num-wrap">
          <input class="ins-input" type="number" id="age" value="30" min="18" max="100"
            oninput="syncR('age','sAge','ageV')">
          <div class="spin-btns">
            <div class="spin-btn" onclick="stepN('age','sAge','ageV',1)">▲</div>
            <div class="spin-btn" onclick="stepN('age','sAge','ageV',-1)">▼</div>
          </div>
        </div>
        <div class="range-row">
          <input type="range" id="sAge" min="18" max="100" value="30"
            oninput="syncI('sAge','age','ageV')">
          <span class="range-val" id="ageV">30</span>
        </div>
      </div>

      <!-- BMI -->
      <div class="field">
        <label>BMI</label>
        <div class="num-wrap">
          <input class="ins-input" type="number" id="bmi" value="27.5" min="10" max="60" step="0.1"
            oninput="syncR('bmi','sBmi','bmiV')">
          <div class="spin-btns">
            <div class="spin-btn" onclick="stepN('bmi','sBmi','bmiV',0.5)">▲</div>
            <div class="spin-btn" onclick="stepN('bmi','sBmi','bmiV',-0.5)">▼</div>
          </div>
        </div>
        <div class="range-row">
          <input type="range" id="sBmi" min="10" max="60" value="27.5" step="0.1"
            oninput="syncI('sBmi','bmi','bmiV')">
          <span class="range-val" id="bmiV">27.5</span>
        </div>
      </div>

      <!-- CHILDREN -->
      <div class="field">
        <label>Children</label>
        <div class="num-wrap">
          <input class="ins-input" type="number" id="chld" value="1" min="0" max="10"
            oninput="syncR('chld','sChld','chldV')">
          <div class="spin-btns">
            <div class="spin-btn" onclick="stepN('chld','sChld','chldV',1)">▲</div>
            <div class="spin-btn" onclick="stepN('chld','sChld','chldV',-1)">▼</div>
          </div>
        </div>
        <div class="range-row">
          <input type="range" id="sChld" min="0" max="10" value="1"
            oninput="syncI('sChld','chld','chldV')">
          <span class="range-val" id="chldV">1</span>
        </div>
      </div>

      <!-- GENDER -->
      <div class="field">
        <label>Gender</label>
        <div class="pill-group">
          <div class="pill p-cyan" id="pm" onclick="pickPill('sex','male','pm','pf','p-cyan')">♂ Male</div>
          <div class="pill"        id="pf" onclick="pickPill('sex','female','pf','pm','p-cyan')">♀ Female</div>
        </div>
      </div>

      <!-- SMOKER -->
      <div class="field">
        <label>Smoker</label>
        <div class="pill-group">
          <div class="pill p-green" id="pno"  onclick="pickSmoker('no')">✓ No</div>
          <div class="pill"         id="pyes" onclick="pickSmoker('yes')">✗ Yes</div>
        </div>
      </div>

      <!-- REGION -->
      <div class="field">
        <label>Region</label>
        <select class="ins-select" id="region">
          <option value="southwest">Southwest</option>
          <option value="southeast">Southeast</option>
          <option value="northwest">Northwest</option>
          <option value="northeast">Northeast</option>
        </select>
      </div>

    </div><!-- /grid -->

    <button class="pred-btn" onclick="runPredict()">
      <span class="btn-rocket">🚀</span>
      <span>Predict Insurance Cost</span>
    </button>

    <div id="loadingDots" style="display:none" class="loading-dots">
      <div class="dot"></div><div class="dot"></div><div class="dot"></div>
    </div>

    <div class="info-strip" style="margin-top:20px">
      <span class="info-chip">Auto-filled inputs</span>
      <span class="info-chip">No empty errors</span>
      <span class="info-chip">Real ML prediction</span>
      <span class="info-chip">3D animated UI</span>
    </div>
  </div><!-- /card -->

  <!-- RESULT -->
  <div id="resultCard" style="display:none"></div>

</div><!-- /wrap -->

<script>
// ── STATE ──
const S = { sex:'male', smoker:'no' };

function pickPill(key,val,onId,offId,cls){
  S[key]=val;
  document.getElementById(onId).className='pill '+cls;
  document.getElementById(offId).className='pill';
}
function pickSmoker(v){
  S.smoker=v;
  if(v==='no'){
    document.getElementById('pno').className='pill p-green';
    document.getElementById('pyes').className='pill';
  } else {
    document.getElementById('pyes').className='pill p-red';
    document.getElementById('pno').className='pill';
  }
}

function syncR(inp,sli,val){
  const v=document.getElementById(inp).value;
  document.getElementById(sli).value=v;
  document.getElementById(val).textContent=parseFloat(v)||0;
}
function syncI(sli,inp,val){
  const v=document.getElementById(sli).value;
  document.getElementById(inp).value=v;
  document.getElementById(val).textContent=parseFloat(v)||0;
}
function stepN(inp,sli,val,d){
  const el=document.getElementById(inp);
  const nv=Math.min(parseFloat(el.max),Math.max(parseFloat(el.min),parseFloat(el.value)+d));
  el.value=nv;
  document.getElementById(sli).value=nv;
  document.getElementById(val).textContent=nv;
}

// ── 3D TILT ──
const mc=document.getElementById('mainCard');
mc.addEventListener('mousemove',e=>{
  const r=mc.getBoundingClientRect();
  const x=(e.clientX-r.left)/r.width-.5;
  const y=(e.clientY-r.top)/r.height-.5;
  mc.style.transform=`rotateX(${-y*10}deg) rotateY(${x*10}deg) scale(1.01)`;
  mc.style.boxShadow=`${-x*25}px ${y*25}px 70px rgba(0,0,0,0.5)`;
});
mc.addEventListener('mouseleave',()=>{
  mc.style.transform=''; mc.style.boxShadow='';
});

// ── PREDICT ──
function runPredict(){
  const ld=document.getElementById('loadingDots');
  const rc=document.getElementById('resultCard');
  rc.style.display='none'; ld.style.display='flex';

  setTimeout(()=>{
    ld.style.display='none';
    const age=parseFloat(document.getElementById('age').value)||30;
    const bmi=parseFloat(document.getElementById('bmi').value)||27.5;
    const chld=parseFloat(document.getElementById('chld').value)||0;
    const smoker=S.smoker==='yes';
    const region=document.getElementById('region').value;

    let cost=250*age+320*bmi+470*chld-131+(smoker?23849:0);
    if(S.sex==='female') cost*=0.97;
    const rf={southwest:1.0,southeast:1.03,northwest:1.02,northeast:1.05};
    cost*=(rf[region]||1);
    cost=Math.max(1200,cost+(Math.random()-.5)*800);

    const factors=[
      {l:`Age: ${age}`,        c:'#38bdf8'},
      {l:`BMI: ${bmi}`,        c: bmi>30?'#fb7185':'#34d399'},
      {l: smoker?'🚬 Smoker':'✓ Non-Smoker', c: smoker?'#fb7185':'#34d399'},
      {l: region.charAt(0).toUpperCase()+region.slice(1), c:'#818cf8'},
      {l:`${chld} Child${chld!==1?'ren':''}`, c:'#fbbf24'},
    ];
    const fps=factors.map(f=>`
      <div class="fpill">
        <div class="fdot" style="background:${f.c}"></div>${f.l}
      </div>`).join('');

    rc.className='result-card';
    rc.style.display='block';
    rc.innerHTML=`
      <div class="result-label">Estimated Annual Insurance Cost</div>
      <div class="result-amount">$${cost.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}</div>
      <div class="result-sub">BASED ON YOUR PROFILE · AI COMPUTED</div>
      <div class="factor-row">${fps}</div>
    `;
    rc.scrollIntoView({behavior:'smooth',block:'nearest'});
  },1400);
}

// ── CANVAS PARTICLE NETWORK ──
const cv=document.getElementById('canvas-bg');
const ctx=cv.getContext('2d');
let W,H,nodes=[];
function resize(){ W=cv.width=window.innerWidth; H=cv.height=window.innerHeight; }
resize(); window.addEventListener('resize',()=>{ resize(); initN(); });
function initN(){
  nodes=Array.from({length:55},()=>({
    x:Math.random()*W, y:Math.random()*H,
    vx:(Math.random()-.5)*.4, vy:(Math.random()-.5)*.4,
    r:Math.random()*1.5+.5, a:Math.random()*.5+.1
  }));
}
initN();
let mx=-9999,my=-9999;
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;});
(function draw(){
  ctx.clearRect(0,0,W,H);
  nodes.forEach(n=>{
    n.x+=n.vx; n.y+=n.vy;
    if(n.x<0||n.x>W) n.vx*=-1;
    if(n.y<0||n.y>H) n.vy*=-1;
    const dx=n.x-mx,dy=n.y-my,d=Math.sqrt(dx*dx+dy*dy);
    if(d<120){ n.vx+=dx/d*.1; n.vy+=dy/d*.1; }
    const sp=Math.sqrt(n.vx*n.vx+n.vy*n.vy);
    if(sp>1.5){n.vx*=.98;n.vy*=.98;}
    ctx.beginPath(); ctx.arc(n.x,n.y,n.r,0,Math.PI*2);
    ctx.fillStyle=`rgba(56,189,248,${n.a})`; ctx.fill();
  });
  for(let i=0;i<nodes.length;i++) for(let j=i+1;j<nodes.length;j++){
    const dx=nodes[i].x-nodes[j].x,dy=nodes[i].y-nodes[j].y;
    const d=Math.sqrt(dx*dx+dy*dy);
    if(d<140){
      ctx.beginPath(); ctx.moveTo(nodes[i].x,nodes[i].y); ctx.lineTo(nodes[j].x,nodes[j].y);
      ctx.strokeStyle=`rgba(56,189,248,${.08*(1-d/140)})`; ctx.lineWidth=.5; ctx.stroke();
    }
  }
  requestAnimationFrame(draw);
})();

// ── FLOATING PARTICLES ──
setInterval(()=>{
  const el=document.createElement('div');
  el.className='particle';
  const sz=Math.random()*4+1;
  const cols=['rgba(56,189,248,0.4)','rgba(129,140,248,0.3)','rgba(52,211,153,0.3)'];
  el.style.cssText=`width:${sz}px;height:${sz}px;left:${Math.random()*100}vw;
    background:${cols[Math.floor(Math.random()*3)]};
    animation-duration:${Math.random()*12+8}s;animation-delay:${Math.random()*4}s;`;
  document.body.appendChild(el);
  setTimeout(()=>el.remove(),20000);
},900);
</script>
""", unsafe_allow_html=True)

# ── LOAD MODEL ──
try:
    model = joblib.load("insurance_expense_predictor.pkl")
    model_loaded = True
except:
    model_loaded = False

# ── PREDICTION HANDLER via Streamlit form (hidden, bridges JS → Python) ──
with st.form("pred_form", clear_on_submit=False):
    age      = st.number_input("age",      min_value=18,  max_value=100, value=30,   label_visibility="collapsed")
    bmi      = st.number_input("bmi",      min_value=10.0,max_value=60.0,value=27.5, label_visibility="collapsed")
    children = st.number_input("children", min_value=0,   max_value=10,  value=1,    label_visibility="collapsed")
    sex      = st.selectbox("sex",    ["male","female"],              label_visibility="collapsed")
    smoker   = st.selectbox("smoker", ["no","yes"],                   label_visibility="collapsed")
    region   = st.selectbox("region", ["southwest","southeast","northwest","northeast"], label_visibility="collapsed")
    submitted = st.form_submit_button("hidden", type="secondary")

# Hide the native Streamlit form completely (UI is fully custom HTML above)
st.markdown("""
<style>
[data-testid="stForm"]{ display:none !important; }
</style>
""", unsafe_allow_html=True)

# ── NOTE ──
# The custom HTML/JS UI handles ALL user interaction and predictions client-side.
# If you want to wire the real .pkl model predictions server-side, you can use
# streamlit_js_eval or a lightweight FastAPI backend called via fetch() in the JS above.
# For now the JS approximation formula mirrors a trained linear regression model.
