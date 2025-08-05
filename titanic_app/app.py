import streamlit as st 
import joblib 
import numpy as np 
import os

# Load the trained model using absolute path
model_path = os.path.join(os.path.dirname(__file__), 'titanic_model.pkl')
model = joblib.load(model_path)

st.title("Titanic Survival Prediction")
st.write("Hello, Titanic App is Running!")  

# Form input
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=0.0)
fare = st.number_input("Fare", min_value=0.0, max_value=0.0, value=0.0)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])
sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)

# Convert inputs
sex = 1 if sex == "male" else 0
embarked_dict = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_dict[embarked]

# Make prediction
features = np.array([[pclass, sex, age, fare, embarked, sibsp, parch]])
if st.button("Predict"):
    result = model.predict(features)
    st.success(f"Prediction: {'Survived' if result[0] == 1 else 'Did Not Survive'}")
