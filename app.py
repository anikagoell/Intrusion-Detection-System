import streamlit as st
import pandas as pd
import joblib

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Intrusion Detection System",
    page_icon="🛡️",
    layout="wide"
)

# --- CUSTOM CSS FOR STYLE ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        background-image: linear-gradient(to bottom right, #0f172a, #1e293b);
        color: white;
    }
    h1, h2, h3, h4 {
        color: #38bdf8;
        text-align: center;
    }
    .stFileUploader {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #334155;
    }
    .dataframe {
        background-color: #1e293b;
        color: #e2e8f0;
    }
    /* Make metric text visible */
    [data-testid="stMetricValue"] {
        color: white !important;
    }
    [data-testid="stMetricLabel"] {
        color: #38bdf8 !important;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>🔍 Intrusion Detection System (IDS)</h1>", unsafe_allow_html=True)
st.markdown("<h3>🧠 Machine Learning-based Network Threat Detection</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- FILE UPLOAD SECTION (Main Page) ---
st.markdown("### 📂 Upload Network Data File (CSV or TXT)")
uploaded_file = st.file_uploader("Choose your network traffic file:", type=["csv", "txt"])

# --- LOAD MODEL COMPONENTS ---
model = joblib.load("ids_model.pkl")
scaler = joblib.load("scaler.pkl")
protocol_encoder = joblib.load("protocol_encoder.pkl")
service_encoder = joblib.load("service_encoder.pkl")
flag_encoder = joblib.load("flag_encoder.pkl")

# --- COLUMN LIST ---
columns = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
    'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
    'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login',
    'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
    'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
    'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
    'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate'
]

# --- MAIN LOGIC ---
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.markdown("### 🧾 Uploaded Data Preview")
    st.dataframe(data.head())

    # Encode + scale
    data['protocol_type'] = protocol_encoder.transform(data['protocol_type'])
    data['service'] = service_encoder.transform(data['service'])
    data['flag'] = flag_encoder.transform(data['flag'])
    data_scaled = scaler.transform(data[columns])

    # Predict
    preds = model.predict(data_scaled)
    data['Prediction'] = ["✅ Normal" if p == 0 else "🚨 Attack" for p in preds]

    # Display results
    st.markdown("### 🔍 Detection Results")
    st.dataframe(data[['Prediction']])

    # Count metrics
    normal = list(data['Prediction']).count("✅ Normal")
    attack = list(data['Prediction']).count("🚨 Attack")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🟢 Normal Connections", normal)
    with col2:
        st.metric("🔴 Attacks Detected", attack)
else:
    st.info("📁 Please upload a CSV or TXT file to begin intrusion detection.")
