# 🎓 Student Grade Class Prediction App

A Machine Learning web application that predicts a student's grade class based on academic and personal factors. Built using Scikit-learn and deployed with Streamlit for real-time predictions.

---

## 🚀 Live Demo
👉 (Add your deployed Streamlit link here)

---

## 📌 Features
- 🎯 Predicts student grade class (A–E)
- ⚡ Real-time prediction with interactive UI
- 🧠 Machine Learning model using Naive Bayes & KNN
- 🔄 Pipeline integration for preprocessing + prediction
- 📊 Clean and user-friendly Streamlit interface
- ✅ Handles feature consistency during deployment

---

## 🛠️ Tech Stack
- **Python**
- **Scikit-learn**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Joblib**

---

## 📊 Model Details
- **Algorithm Used:**
  - Gaussian Naive Bayes
  - K-Nearest Neighbors (KNN)

- **Pipeline:**
  - Data preprocessing (scaling/encoding)
  - Model training
  - Combined using Scikit-learn Pipeline

---

## 📥 Input Features
The model takes the following inputs:

- Age  
- Gender  
- Ethnicity  
- Parental Education  
- Study Time Weekly  
- Absences  
- Tutoring  
- Parental Support  
- Extracurricular Activities  
- Sports  
- Music  
- Volunteering  
- GPA  

---

## 📈 Output
- Predicted **Grade Class**:
  - Grade A (Excellent)
  - Grade B (Very Good)
  - Grade C (Good)
  - Grade D (Pass)
  - Grade E (Fail/Retake)

---

## 🖥️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/student-grade-app.git

# Navigate to project folder
cd student-grade-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
