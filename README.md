
**Predicting Breast Cancer in a patient**

**Abstract:**

Breast cancer represents one of the diseases that make a high number of deaths every
year. It is the most common type of all cancers and the main cause of women's deaths
worldwide. Classification and data mining methods are an effective way to classify data.
Especially in the medical field, where those methods are widely used in diagnosis and
analysis to make decisions.

**Problem Statement:**

Given the details of cell nuclei taken from breast mass, predict whether or not a patient
has breast cancer using the Ensembling Techniques. Perform necessary exploratory
data analysis before building the model and evaluate the model based on performance
metrics other than model accuracy.

**Dataset Information:**

The dataset consists of several predictor variables and one target variable, Diagnosis.
The target variable has values 'Benign' and 'Malignant', where 'Benign' means that the
cells are not harmful or there is no cancer and 'Malignant' means that the patient has
cancer and the cells have a harmful effect


<img width="675" alt="home page image" src="https://github.com/user-attachments/assets/cb5c0a40-d8fe-4c2d-a0f6-f628f87bf515">


**Breast Cancer Prediction using SVM Classifier**


This project aims to predict breast cancer in patients using Support Vector Machine (SVM) classifier with the scikit-learn library. The steps involved include data pre-processing, training the SVM classifier, assessing the model's correctness, and tuning hyperparameters for improved performance.


**Introduction**

Breast cancer is one of the most common cancers among women worldwide. Early detection and accurate prediction of breast cancer can significantly improve patient outcomes. In this project, we use machine learning techniques to predict whether a patient has breast cancer based on various features.

**Dependencies**

Python 3

pandas

numpy

scikit-learn

**Data Pre-processing**

Data pre-processing involves handling missing values, scaling features, encoding categorical variables, and splitting the dataset into training and testing sets. It ensures that the data is in a suitable format for training the SVM classifier.

**Feature Selection**
Implementing Univariate Feature Selection technique to select TOP 5 Features.

<img width="290" alt="image" src="https://github.com/user-attachments/assets/1b146f94-bfe5-47fd-8158-83e17f3a6016">


**Training SVM Classifier**

We train an SVM classifier using the scikit-learn library to predict breast cancer in patients. SVM is a powerful algorithm suitable for binary classification tasks like this. We use the training data to fit the SVM model and make predictions on unseen testing data.

**Model Evaluation**

We assess the correctness of the SVM classifier by evaluating its performance using various metrics such as accuracy, precision, sensitivity (recall), specificity. These metrics provide insights into the efficiency and effectiveness of the classifier.

<img width="498" alt="image" src="https://github.com/user-attachments/assets/3526f443-352e-47e4-b018-5899a784910f">

**Streamlit Web Page**

<img width="746" alt="User input image" src="https://github.com/user-attachments/assets/04249b4b-a573-4505-852d-ffda4af5ad27">






