# Sales Prediction Using Python

A machine learning project that predicts product sales based on advertising expenditure across **TV**, **Radio**, and **Newspaper** channels. Includes a Streamlit web application for real-time predictions.

---

## Project Overview

This project analyzes the **Advertising dataset** (200 records) to understand the relationship between advertising spend and product sales. Two regression models are trained and compared, with the best-performing model deployed in an interactive Streamlit app.

---

## Dataset

**File:** `Advertising.csv`

| Feature | Description |
|---|---|
| `TV` | TV advertising spend |
| `Radio` | Radio advertising spend |
| `Newspaper` | Newspaper advertising spend |
| `Sales` | Product sales (target variable) |

**Dataset Stats:**
- Records: 200
- Missing values: None
- Duplicate rows: None

**Correlation with Sales:**
| Feature | Correlation |
|---|---|
| TV | 0.78 (strongest) |
| Radio | 0.58 |
| Newspaper | 0.23 (weakest) |

---

## ML Pipeline

1. **Data Loading** — Load `Advertising.csv`, drop unnamed index column if present
2. **Data Cleaning** — Check for missing values and duplicates (none found)
3. **EDA** — Sales distribution histogram, scatter plots (Sales vs each feature), correlation heatmap
4. **Train-Test Split** — 80% train / 20% test (`random_state=42`)
5. **Model Training** — Linear Regression & Random Forest Regressor (200 estimators)
6. **Evaluation** — MAE, RMSE, R² Score
7. **Best Model Selection** — Lowest RMSE wins → saved as `sales_prediction_model.pkl`

---

## Model Results

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | 1.4608 | 1.7816 | 0.8994 |
| **Random Forest** | **0.6289** | **0.7577** | **0.9818** |

**Best Model:** Random Forest (200 estimators)

**Feature Importance (Random Forest):**
| Feature | Importance |
|---|---|
| TV | 62.5% |
| Radio | 36.2% |
| Newspaper | 1.3% |

---

## Project Structure

```
5.Sales_Prediction/
├── app.py                        # Streamlit web application
├── sales_prediction.ipynb        # EDA, model training & evaluation
├── sales_prediction_model.pkl    # Saved best model (Random Forest)
├── Advertising.csv               # Dataset
├── requirements.txt              # Python dependencies
└── images/
    └── Background.jpg            # App background image
```

---

## Streamlit App

The app allows users to enter advertising budgets for each channel and instantly get a predicted sales value.

**App Features:**
- Number inputs for TV, Radio, and Newspaper advertising spend
- Displays **Predicted Sales** and **Total Advertising Spend** as result cards
- Shows input summary as a dataframe
- Sidebar with project info and tech stack

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

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data loading & processing |
| NumPy | Numerical operations |
| Matplotlib / Seaborn | Data visualization |
| Scikit-learn | ML models & evaluation |
| Streamlit | Web application |

---

## Internship

This project was developed as part of the **Oasis Infobyte** Data Science Internship.
