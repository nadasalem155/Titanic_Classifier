# Titanic Classifier 🚢

**Description:**  
This project implements a **binary classification model** using a **Random Forest Classifier** to predict whether a passenger on the Titanic survived or not.  

**Live App:**  
Access the deployed app here:  
🔗 [Titanic Classifier - Streamlit App](https://titanicclassifier-ejfv8enxhitqtcprbhwrhw.streamlit.app/)  

---

## Dataset 📊
The dataset is the **Titanic dataset from Kaggle**, containing passenger information such as:  
- **Age**  
- **Sex**  
- **Pclass** (ticket class: 1st, 2nd, 3rd)  
- **Fare**  
- **Embarked** (C = Cherbourg, Q = Queenstown, S = Southampton)  
- **SibSp** (number of siblings/spouses aboard)  
- **Parch** (number of parents/children aboard)  

**Objective:**  
Predict whether a passenger survived (**1**) or not (**0**) based on the available features.  

---

## Features 📝
- **PassengerId** → unique id (removed for modeling)  
- **Survived** → target column (0 = No, 1 = Yes)  
- **Pclass** → passenger class  
- **Sex** → male/female  
- **Age** → in years  
- **SibSp** → siblings/spouses aboard  
- **Parch** → parents/children aboard  
- **Fare** → ticket price  
- **Embarked** → port of embarkation (C, Q, S)  
- **Cabin** → removed due to missing values (~77%)  
- **Ticket** → removed  
- **Name** → removed  

---

## Model 🤖
- **Algorithm:** `RandomForestClassifier` from `sklearn.ensemble`  
- **Training:** on cleaned and preprocessed data  
- **Comparison:** Random Forest vs. Decision Tree  

---

## Evaluation 📈
**Metrics:**  
- Accuracy: 0.8371  
- Precision: 0.8333  
- Recall: 0.7246  
- F1 Score: 0.7752  

**Confusion Matrix:**

[[99 10] [19 50]]

**Cross-validation Scores:**

[0.7640, 0.8202, 0.8315, 0.7921, 0.8531]
Average Accuracy: 0.8122

**Insights:**  
- Female passengers had higher survival rate than males  
- 1st class passengers survived more than 2nd and 3rd class  
- Children (<16 years) had the highest survival rate  
- Passengers with family onboard or higher fare had better survival chances  
- Embarked location mattered: C > Q > S  

---

## Deployment 🚀
The model is deployed using **Streamlit**, allowing users to:  
- Input passenger details  
- Predict survival probability  
- Receive **interactive emoji feedback** (😊 Survived / 😢 Did Not Survive)  

---

## presentation 📄
You can view the full project presentation here:  
🔗 [Titanic Classifier presentation ](Titanic_Classifier-presentation.pdf)  

*(Replace `#` with the link to your PDF/Word report.)*

---

## Files Included 📂
- `titanic_random_forest.ipynb` → Full notebook with preprocessing, training, and evaluation  
- `README.md` → Project overview and details  
- `titanic_model.pkl` → Trained Random Forest model  
- `app.py` → Streamlit deployment script  

---

## Requirements ⚡
Python
pandas
numpy
scikit-learn
matplotlib
streamlit
joblib



-----------------

## Conclusion 🏁

Random Forest outperformed a single Decision Tree in terms of accuracy

Combining predictions from multiple trees reduced overfitting and improved generalization

The project demonstrates a complete ML pipeline:
EDA → Cleaning → Feature Engineering → Modeling → Evaluation → Deployment

Provides clear insights about factors affecting survival on the Titanic
