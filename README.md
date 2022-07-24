# Heart Condition Checker
The app created with Python to predict person's heart health condition based on well-trained machine learning model ().

## Table of Contents
1. [General info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)


## General info
In this project, logistic regression was used to predict person's heart health condition expressed as a dichotomous variable (heart disease: yes/no). The model was trained on approximately 70,000 data from an annual telephone survey of the health of U.S. residents from the year 2020. The dataset is publicly available at the following link: https://www.cdc.gov/brfss/annual_data/annual_2020.html. The data is originally stored in SAS format. The original dataset contains approx. 400,000 rows and over 200 variables. The data conversion and cleaning process is described in another repository: https://github.com/kamilpytlak/data-analyses/tree/main/heart-disease-prediction. This project contains:
* the app - the application construct is located in the `app.py` file. This file uses data from the `data` folder and saved (previously trained) ML models from the `model` folder.

The logistic regression model was found to be satisfactorily accurate (accuracy approx. 80%).

## Technologies

### Visualisation

* Tableau
* HTML / CSS

### Backend

* Flask (API)

### Machine Learning

* Sklearn (Logistic Regression / Random Forest)
* Imbalanced Learn (Because dataset is severely imbalanced)

## Model Analysis

Since we wanted to classify whether someone had heart disease or not (classification), we used Logistic Regression and Random Forest Classification. We had to use Random Undersampling to balnce our data (we had more samples of people without heart disease than people with).

Overall, logistic regression had a higher accuracy than random forest. However, Random Forest had a higher recall (.79 compared to Logistic regression's .70). This means that Random Forest predicted more of the samples with heart disease, but Logistic Regression had higher overall accuracy.

## Feature Importance

Both models said the most important categories are:

* Age
* Stroke History
* Diabetic
* Gender
* Smoking

## Dashboard

Link to Tableau - Nicholas & Ramana 
