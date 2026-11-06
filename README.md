# Sales Prediction Using Python

A machine learning project that predicts product sales based on advertising expenditure across TV, Radio, and Newspaper channels. Built with an interactive Streamlit web application for real-time predictions.

---

## Project Overview

This project analyzes the relationship between advertising spend and product sales using the classic **Advertising dataset** (200 records). Two regression models are trained and evaluated, with the best-performing model deployed in a Streamlit app.

---

## Dataset

**File:** `Advertising.csv`

| Feature | Description |
|---|---|
| `TV` | TV advertising spend |
| `Radio` | Radio advertising spend |
| `Newspaper` | Newspaper advertising spend |
| `Sales` | Product sales (target variable) |

- **Records:** 200
- **Missing values:** None
- **Duplicates:** None

**Correlation with Sales:**
- TV: 0.78 (strongest)
- Radio: 0.58
- Newspaper: 0.23 (weakest)

---

## Models

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | 1.4608 | 1.7816 | 0.8994 |
| **Random Forest** | **0.6289** | **0.7577** | **0.9818** |

**Best Model:** Random Forest (200 estimators) — saved as `sales_prediction_model.pkl`

**Feature Importance (Random Forest):**
- TV: 62.5%
- Radio: 36.2%
- Newspaper: 1.3%

---

## Project Structure

```
5.Sales_Prediction/
├── app.py                        # Streamlit web application
├── sales_prediction.ipynb        # EDA, model training & evaluation
├── sales_prediction_model.pkl    # Trained Random Forest model
├── Advertising.csv               # Dataset
├── requirements.txt              # Dependencies
└── images/
    └── Background.jpg            # App background image
```

---

## Setup, Run & Online Deploy

🌐 **Live Demo:** [https://5salesprediction-dx9nm3rni67cjw3ypvypzp.streamlit.app/](https://5salesprediction-dx9nm3rni67cjw3ypvypzp.streamlit.app/)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd 5.Sales_Prediction
```

### 2. Create a Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App Locally
```bash
streamlit run app.py
```

### 5. Deactivate Virtual Environment
```bash
deactivate
```

---

## Streamlit App

The app allows users to enter advertising budgets for each channel and get an instant sales prediction.

**Features:**
- Input fields for TV, Radio, and Newspaper spend
- Displays predicted sales and total advertising spend
- Shows input summary as a dataframe

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Streamlit

---

## Internship

This project was developed as part of the **Oasis Infobyte** Data Science Internship.
