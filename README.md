

# ⚖️ Court Case Backlog & Automated Case Scheduling System

An AI-powered system designed to reduce court case backlog by intelligently prioritizing cases, predicting delay risks, and automating hearing date scheduling.

---

## 📌 Problem Statement

Case scheduling in many district courts is manual, paper-based, and dependent on individual staff members. There is:

* No intelligent case prioritization
* No delay prediction system
* No adjournment monitoring
* No tracking of lawyer availability patterns
* No automated scheduling

This results in:

* Massive backlog
* Delayed justice
* Lack of transparency
* Inefficient court operations

---

## 🚀 Our Solution

We built an AI-driven automated scheduling system that:

* Calculates case priority score
* Predicts delay probability using Machine Learning
* Automatically assigns hearing dates
* Flags high-risk and long-pending cases
* Provides analytics dashboard for monitoring

---

## 🏗 System Architecture

```
Case Input
    ↓
Database Storage
    ↓
Priority Score Engine
    ↓
Delay Prediction Model (ML)
    ↓
Scheduling Engine
    ↓
Adjournment Monitoring
    ↓
Analytics Dashboard
```

---

## 🔑 Key Features

### 1️⃣ Case Priority Scoring System

Each case receives a weighted score based on:

* Case Age
* Urgency Level
* Adjournment Count
* Lawyer Attendance %
* Case Type

Priority Formula:

```
Priority Score =
(0.4 × Case_Age_Days) +
(0.3 × Urgency_Level × 100) +
(0.2 × Adjournments × 50) +
(0.1 × (100 − Lawyer_Attendance_%))
```

Cases are automatically ranked from highest to lowest priority.

---

### 2️⃣ AI-Based Delay Prediction

Machine Learning model predicts:

* Probability of case delay
* Risk level (Low / Medium / High)

Model Used:

* Logistic Regression

Features Used:

* Case Age
* Urgency Level
* Adjournments
* Lawyer Attendance %
* Judge Load

---

### 3️⃣ Automated Scheduling Engine

System:

* Checks judge availability
* Evaluates priority score
* Considers delay risk
* Assigns optimal hearing date

---

### 4️⃣ Adjournment Monitoring

* Tracks number of adjournments
* Flags cases with excessive adjournments
* Identifies frequent lawyer absence

---

### 5️⃣ Analytics Dashboard

Displays:

* Total cases
* High priority cases
* Delay risk distribution
* Case aging graph
* Judge workload analysis

---

## 🛠 Tech Stack

Frontend:

* Streamlit

Backend:

* Python

Machine Learning:

* Scikit-learn
* Pandas
* NumPy

Visualization:

* Matplotlib

---

## 📂 Project Structure

```
court_ai_project/
│
├── data.csv
├── generate_data.py
├── priority.py
├── model.py
├── app.py
└── README.md
```

---


---

## 📊 Expected Impact

* Faster case disposal
* Reduced backlog
* Data-driven judicial decisions
* Transparent scheduling
* Reduced unnecessary adjournments

---

## 🔮 Future Enhancements

* NLP-based FIR classification
* Reinforcement Learning for slot optimization
* SMS / Email notifications
* Lawyer reliability scoring
* Integration with court e-filing systems

---

## 👨‍💻 Hackathon Project

Built as part of a hackathon to modernize judicial scheduling using AI and automation.

---

## 📜 License

This project is for academic and hackathon demonstration purposes.
