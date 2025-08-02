# titanic_classifier1

This project implements a binary classification model using a Random Forest Classifier to predict whether a passenger on the Titanic survived or not.

## Dataset

The dataset used is the Titanic dataset from Kaggle.

It includes information about Titanic passengers such as:

- Age  
- Sex  
- Pclass (ticket class)  
- Fare  
- Embarked location  
- SibSp (number of siblings/spouses aboard)  
- Parch (number of parents/children aboard)

## Objective

To build a machine learning model that predicts whether a passenger survived (1) or not (0) based on available features.

## Model

- Algorithm used: RandomForestClassifier from sklearn.ensemble
- Trained on cleaned and preprocessed data
- Compared performance with a simple Decision Tree Classifier

## Evaluation

The model is evaluated using the following metrics:

- Accuracy  
- Confusion Matrix  
- Precision  
- Recall  
- F1 Score  
- Cross-validation

### Example Output

Confusion Matrix: [[93 16] [16 53]]

Accuracy : 0.8202
Precision: 0.7681
Recall   : 0.7681
F1 Score : 0.7681

### Cross-validation Scores

[0.8034, 0.8258, 0.8202, 0.7753, 0.8136]
Average Accuracy: 0.8077

## Files Included

- titanic_random_forest.ipynb: Jupyter Notebook with full code, preprocessing, training, and evaluation  
- README.md: Project overview and details

## Conclusion

The Random Forest model performed better than a single Decision Tree in terms of accuracy. This is because it combines predictions from multiple trees, reducing overfitting and improving generalization.

