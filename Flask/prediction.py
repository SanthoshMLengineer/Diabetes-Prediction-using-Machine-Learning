from os.path import abspath

import pickle

import numpy as np

# Constants
num_outcome = {0:"Non-Diabetic",
			   1:"Diabetic"
			   }

outcome_display = {"Diabetic":"You have diabetic please visit Hospital",
				   "Non-Diabetic":"You have no Diabetic"
				   }
#model = pickle.load(open("F:\\Personal Projects\\Diabetics Prediction\\Python Scripts\\Data Files\\gradient_boost_model.pkl",'rb'))
#print(model)

def load_model():
	"""
	This function helps to load model
	Parameter
	---------
		None
	Returns
	-------
		model = object
			loaded model
	"""
	try:
		model = pickle.load(open(".//..//Data Files//Random_forest.pkl",'rb'))
		return model
	except Exception as e:
		raise e

def predict(dataframe):
	"""
	This function helps to do prediction
	Parameter
	--------
		list_features : list()
			list of features
	Returns
	-------
		Prediction : str
			Outcome from model
	"""
	model = load_model()
	if model:
		result = model.predict(dataframe)
		return outcome_display[num_outcome[result[0]]]
	else:
		return "Error in loading model"