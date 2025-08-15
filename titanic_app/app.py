import streamlit as st
import joblib
import numpy as np
import os
import plotly.graph_objects as go

# ----------------- Load Model -----------------
model_path = os.path.join(os.path.dirname(_file_), 'titanic_model.pkl')
model = joblib.load(model_path)

# ----------------- App Title -----------------
st.title("🚢 Titanic Survival Prediction")
st.markdown("This app predicts whether a passenger would have survived the Titanic disaster based on their information.")

# ----------------- User Input Form -----------------
st.subheader("🔹 Enter Passenger Details")

pclass = st.selectbox(
    "Passenger Class", 
    [1, 2, 3], 
    format_func=lambda x: f"{x}st Class" if x == 1 else f"{x}nd Class" if x == 2 else f"{x}rd Class"
)
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0, step=1.0)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=30.0, step=1.0)
embarked = st.selectbox("Embarked", ["C = Cherbourg", "Q = Queenstown", "S = Southampton"])
sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)

# ----------------- Preprocess Inputs -----------------
sex = 1 if sex == "male" else 0
embarked_dict = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_dict[embarked[0]]  # Take first letter (C/Q/S)

features = np.array([[pclass, sex, age, fare, embarked, sibsp, parch]])

# ----------------- Prediction -----------------
if st.button("Predict"):
    prob = model.predict_proba(features)[0]  # Probabilities [Not Survived, Survived]
    prediction = model.predict(features)[0]

    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.success(f"😊🚢 Survived with probability {prob[1]*100:.2f}%")
    else:
        st.error(f"😢🪦 Did Not Survive (Survival chance {prob[1]*100:.2f}%)")

    # ----------------- Gauge Chart -----------------
    st.subheader("📈 Survival Probability Gauge")
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=prob[1]*100,
        delta={'reference': 50, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green" if prediction == 1 else "red"},
            'steps': [
                {'range': [0, 50], 'color': "#ffcccc"},
                {'range': [50, 100], 'color': "#ccffcc"}
            ],
            'threshold': {
                'line': {'color': "blue", 'width': 4},
                'thickness': 0.75,
                'value': prob[1]*100
            }
        },
        title={'text': "Survival Probability (%)"}
    ))

    st.plotly_chart(fig, use_container_width=True)