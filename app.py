import streamlit as st
import pandas as pd
import pickle
import os
import base64


# PAGE CONFIGURATION
st.set_page_config(page_title="Sales Prediction System", page_icon=" ", layout="wide")


# BACKGROUND IMAGE
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image:
                    linear-gradient(rgba(3, 15, 35, 0.72), rgba(3, 15, 35, 0.82)),
                    url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Background image not found!")
set_background("images/background.jpg")


# CUSTOM CSS
st.markdown("""
<style>

.main-title {
    text-align: center;
    color: #FFFFFF;
    font-size: 42px;
    font-weight: bold;
    padding: 15px;
    text-shadow: 2px 2px 8px #000000;
}

.subtitle {
    text-align: center;
    color: #FFFFFF;
    font-size: 18px;
    margin-bottom: 30px;
}

h1, h2, h3 {
    color: #FFFFFF !important;
    font-weight: bold;
}

.stApp p {
    color: #FFFFFF;
}

.stNumberInput label {
    color: #FFFFFF !important;
    font-weight: bold !important;
}

.stNumberInput input {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border-radius: 8px;
}

div.stButton > button {
    background-color: #0784D1;
    color: #FFFFFF;
    border: none;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #00A6FF;
    color: #FFFFFF;
}

.result-card {
    background-color: #FFFFFF !important;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #6CCBFF;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.2);
    min-height: 115px;
}

.result-label {
    color: #000000 !important;
    font-size: 20px;
    font-weight: bold;
}

.result-value {
    color: #000000 !important;
    font-size: 35px;
    font-weight: bold;
    margin-top: 12px;
}

[data-testid="stSidebar"] {
    background-color: rgba(5, 25, 50, 0.96);
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

.footer {
    text-align: center;
    color: #FFFFFF;
    font-size: 14px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# LOAD MODEL
@st.cache_resource
def load_model():
    model_path = "sales_prediction_model.pkl"
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model
try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file not found! Please add sales_prediction_model.pkl")
    st.stop()
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# HEADER
st.markdown('<div class="main-title">SALES PREDICTION SYSTEM</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'Predict Product Sales Using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)
st.write("")


# SIDEBAR
st.sidebar.title("ABOUT PROJECT")
st.sidebar.write("This application predicts product sales based on advertising expenditure.")
st.sidebar.markdown("---")
st.sidebar.subheader("TECHNOLOGIES")
st.sidebar.write("Python")
st.sidebar.write("Pandas")
st.sidebar.write("NumPy")
st.sidebar.write("Scikit-learn")
st.sidebar.write("Streamlit")
st.sidebar.markdown("---")
st.sidebar.info("Enter advertising expenses and click Predict Sales.")


# INPUT SECTION
st.subheader("ENTER ADVERTISING DETAILS")
st.write("Enter advertising expenditure for each channel.")

col1, col2, col3 = st.columns(3)
with col1:
    tv = st.number_input("TV Advertising Spend", min_value=0.0, value=200.0, step=10.0)
with col2:
    radio = st.number_input("Radio Advertising Spend", min_value=0.0, value=40.0, step=5.0)
with col3:
    newspaper = st.number_input("Newspaper Advertising Spend", min_value=0.0, value=30.0, step=5.0)
st.write("")


# PREDICTION SECTION
if st.button("PREDICT SALES"):
    input_data = pd.DataFrame({"TV": [tv], "Radio": [radio], "Newspaper": [newspaper]})
    try:
        prediction = model.predict(input_data)[0]
        total_spend = tv + radio + newspaper
        st.success("Sales Prediction Completed Successfully!")
        st.subheader("PREDICTION RESULT")
        result_col1, result_col2 = st.columns(2)

        # PREDICTED SALES CARD
        with result_col1:
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">
                        Predicted Sales
                    </div>
                    <div class="result-value">
                        {prediction:.2f}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # TOTAL ADVERTISING SPEND CARD
        with result_col2:
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">
                        Total Advertising Spend
                    </div>
                    <div class="result-value">
                        {total_spend:.2f}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")
        st.subheader("ADVERTISING DETAILS")
        st.dataframe(input_data, use_container_width=True, hide_index=True)
        st.info("Prediction generated using your trained Machine Learning model.")
    except Exception as e:
        st.error(f"Prediction Error: {e}")


# FOOTER
st.markdown("---")
st.markdown(
    '<div class="footer">'
    'Sales Prediction Using Python | Machine Learning Project'
    '</div>',
    unsafe_allow_html=True
)