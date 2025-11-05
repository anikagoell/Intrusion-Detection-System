<h1 align="center">🛡️ Intrusion Detection System (IDS)</h1>
<h3 align="center">A Machine Learning Based Network Threat Detection Project</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/ML-RandomForest-green"/>
  <img src="https://img.shields.io/badge/Status-Completed-success"/>
</p>

---

## 📘 Project Overview

This project is an **Intrusion Detection System (IDS)** built using **Machine Learning**.  
It analyzes network traffic data and classifies each connection as either **Normal** or **Attack**.  
The model was trained on the **KDD Cup 99 / NSL-KDD** dataset — a well-known benchmark for intrusion detection research.

The web interface is developed with **Streamlit**, providing an easy way to upload CSV files and visualize detection results in real time.

---

## 🧠 Objective

To develop a system capable of:
- Detecting malicious network activity using machine learning.
- Classifying network traffic into normal or attack patterns.
- Providing an intuitive web interface for testing and demonstration.

---

## ⚙️ Key Features

✅ **End-to-End Machine Learning Pipeline**  
- Data preprocessing (encoding & scaling).  
- Model training with Random Forest Classifier.  
- Model evaluation with accuracy and confusion matrix.  

✅ **Interactive Web App**  
- Built with Streamlit.  
- Allows file uploads for real-time detection.  
- Displays predictions and connection statistics dynamically.

✅ **Attractive Dark UI**  
- Styled using custom CSS for a professional dashboard look.  
- Metrics, tables, and alerts are visually highlighted for clarity.

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python |
| **Libraries** | pandas, scikit-learn, joblib, streamlit |
| **Model** | Random Forest Classifier |
| **Frontend** | Streamlit UI with custom CSS |
| **Dataset** | NSL-KDD (KDDTrain+.txt) |

---

## 🧪 How It Works

1. **Data Preprocessing**  
   - Encodes categorical features (`protocol_type`, `service`, `flag`) using LabelEncoders.  
   - Scales all numeric values using MinMaxScaler.  

2. **Model Training**  
   - A RandomForestClassifier learns from 41 network traffic features.  
   - The model achieves near-perfect accuracy on the NSL-KDD dataset.  

3. **Web Application**  
   - Users upload a `.csv` or `.txt` file.  
   - Data is preprocessed automatically using the saved encoders and scaler.  
   - The trained model predicts whether each connection is normal or an attack.  

---

## 🚀 How to Run the Project

### 🧩 Step 1 — Install Dependencies
```bash
pip install -r requirements.txt
