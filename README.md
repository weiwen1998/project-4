# Heart Condition Checker
The app created with Python to predict person's heart health condition based on well-trained machine learning model ().

## Table of Contents
1. [General info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)


## General info
In this project, logistic regression was used to predict person's heart health condition expressed as a dichotomous variable (heart disease: yes/no). The model was trained on approximately 70,000 data from an annual telephone survey of the health of U.S. residents from the year 2020. The dataset is publicly available at the following link: https://www.cdc.gov/brfss/annual_data/annual_2020.html. The data is originally stored in SAS format. The original dataset contains approx. 400,000 rows and over 200 variables. 

## Technologies

### Visualisation

* Tableau
<img width="955" alt="Tableau " src="https://user-images.githubusercontent.com/96853408/180678154-1724551a-ccb6-4e8c-9f53-8de1e921b22e.png">
<img width="379" alt="Tableau - Factors of Heart Disease " src="https://user-images.githubusercontent.com/96853408/180678177-7a1d4512-5b3d-4323-90f5-4c435eb6f674.png">

* HTML / CSS
<img width="471" alt="HTML " src="https://user-images.githubusercontent.com/96853408/180678201-e2c789e4-8cba-4a35-a791-3b7ff64feec8.png">


### Backend

* Flask (API)
![image](https://user-images.githubusercontent.com/96853408/180737260-bb729ef0-62bc-48d9-b37c-52bd2d003346.png)




### Machine Learning

* Sklearn (Logistic Regression / Random Forest)
![Sklearn - models ](https://user-images.githubusercontent.com/96853408/180677787-871e58e1-2393-456f-bbb3-cfe684ff37e8.png)

* Imbalanced Learn (Because dataset is severely imbalanced)
<img width="604" alt="Machine Learning - Imbalance " src="https://user-images.githubusercontent.com/96853408/180677807-e28d2887-edb9-476a-ab7a-ca3e602e1e40.png">


## Model Analysis

Since we wanted to classify whether someone had heart disease or not (classification), we used Logistic Regression and Random Forest Classification. We had to use Random Undersampling to balnce our data (we had more samples of people without heart disease than people with).

Overall, Logistic Regression had a higher accuracy than random forest. However, Random Forest had a higher recall (.79 compared to Logistic regression's .70). 
<img width="539" alt="Logistic Regression " src="https://user-images.githubusercontent.com/96853408/180678128-1548debd-117f-4f62-9a21-d330f5e3edd4.png">

<img width="553" alt="Random Forest Model" src="https://user-images.githubusercontent.com/96853408/180678137-094c9bda-b624-4e90-acf0-18ec9fc5b263.png">


This means that Random Forest predicted more of the samples with heart disease, but Logistic Regression had higher overall accuracy.



## Categories of Importance

Results from both models are heavily depedent on the following categories. 

* Age
* Stroke History
* Diabetic
* Gender
* Smoking
* Kidney Disease 
* General Health 
* Alcohol Consumption

Logistic Regresion Model 

<img width="356" alt="Logistic Regression - Importance  " src="https://user-images.githubusercontent.com/96853408/180677930-cf7853ef-a421-436c-8a3d-77aaf7abf5b6.png">

Random Forest Model 

<img width="259" alt="Forest Model - Importance " src="https://user-images.githubusercontent.com/96853408/180677848-0791b9ea-eb6e-4d51-a28f-7970a8134f66.png">

## Dashboard

https://public.tableau.com/app/profile/nicholas4845/viz/Book1_16581366231650/FactorsofHeartDisease?publish=yes
https://public.tableau.com/app/profile/ramana7009/viz/FinalProject-HeartDieseasePrediction/TheStory?publish=yes

