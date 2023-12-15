from flask import Flask, render_template, request

from prediction import predict
from flask import jsonify

import pandas as pd


app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/")
def home():
    return render_template('index.html')


def check_input(dataframe):
	"""
	This function is used to check whether 
	input is integer or not
	Parameter
	----------
		dataframe : dataframe()
	Returns
	---------
		Returns True if all values is numerical else False 
	"""
	length_numerical_cols = len(list(dataframe.select_dtypes(
		exclude = 'object').columns))
	length_columns = dataframe.shape[1]

	if length_numerical_cols == length_columns:
		print("True")
		return True
	else:
		print(length_numerical_cols, length_columns)
		return False
	

@app.route('/recognisediabetic', methods=['GET', 'POST'])
def recognise_diesease():
	"""
	This function helps to predict diabetics with 
	input parameter
	Parameter
	---------
		Glucose
		BloodPressure
		SkinThickness
		Insulin
		BMI
		DiabetesPedigreeFunction
		Age
	Returns 
	--------
		Prediction from model
	"""
	Glucose = float(request.form.get("Glucose"))
	Pregnancies = float(request.form.get("Pregnancies"))
	BloodPressure = float(request.form.get("BloodPressure"))
	SkinThickness = float(request.form.get("SkinThickness"))
	Insulin = float(request.form.get("Insulin"))
	BMI = float(request.form.get("BMI"))
	DiabetesPedigreeFunction = float(request.form.\
		get("DiabetesPedigreeFunction"))
	Age = float(request.form.get("Age"))

	dict_test_data = {"Pregnancies" : Pregnancies,
                      "Glucose" : Glucose,
                      "BloodPressure" : BloodPressure,
                      "SkinThickness" : SkinThickness,
                      "Insulin" : Insulin,
                      "BMI" : BMI,
                      "DiabetesPedigreeFunction" : DiabetesPedigreeFunction,
                      "Age" : Age}

	data_input = pd.DataFrame(dict_test_data, 
    	index = [0])


	if check_input(data_input):
		prediction = predict(data_input)
		return render_template('index.html', 
			prediction = str(prediction))
	else:
		return render_template('index.html', 
			prediction = str("only numbers are Input"))


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True,threaded=True)


