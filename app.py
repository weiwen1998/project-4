from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
import os
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

app = Flask(__name__)
app = Flask(__name__, static_folder="templates")

# Import filepaths for model, scale, and encoding dictionary
filename = 'machine_learning/models/finalized_model.sav'
filename_standard ='machine_learning/models/standard_scaler.sav'
replacement_dict = 'machine_learning/models/dict_all.obj'

# Create function that will be used to encode, scale, and predict heart disease
# Only using 8 params
def predict_heart_disease(sex, age_category, gen_health, stroke, diabetic, kidney_disease, smoking, alcohol):
    dict_all_loaded = pickle.load(open(replacement_dict, 'rb'))

    # Create list of categorical columns based on the 8 params
    cat_columns = ["Sex", "AgeCategory", 
               "GenHealth", "Stroke", 
               "Diabetic", "KidneyDisease", 
               "Smoking", "AlcoholDrinking"]

    # put all parameters into dataframe
    df = pd.DataFrame({"Sex": sex,
                    "AgeCategory": age_category,
                    "GenHealth": gen_health,
                    "Stroke":stroke,
                    "Diabetic":diabetic,
                    "KidneyDisease":kidney_disease,
                    "Smoking":smoking,
                    "AlcoholDrinking":alcohol}, index=[0])

    for col in cat_columns:
        df[col].replace(dict_all_loaded[col], inplace=True)

    loaded_model = pickle.load(open(filename, 'rb'))

    result = loaded_model.predict(df)

    if result[0] == 0:
        return "No heart disease risk"
    else:
        return "Heart disease risk"



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictor", methods = ["GET","POST"])
def predictor():
    if request.method == "POST":
        sex = request.form['sex']
        age_category = request.form['age-category']
        gen_health = request.form["gen-health"]
        stroke = request.form['stroke']
        diabetic = request.form['diabetic']
        kidney_disease = request.form['kidney-disease']
        smoking = request.form['smoking']
        alcohol = request.form['alcohol']

        prediction = predict_heart_disease(sex, age_category, gen_health, stroke, diabetic, kidney_disease, smoking, alcohol)

        return render_template('predictor.html', result = prediction)

    else:
        return render_template("predictor.html")
    
@app.route("/tableau")
def tableau():
    return render_template("tableau_draft.html")

@app.route("/first_story")
def first_story():
    return render_template("tableau_second_draft.html")

if __name__ == "__main__":
    app.run(debug=True)

