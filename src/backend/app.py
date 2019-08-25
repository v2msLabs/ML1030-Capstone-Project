from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
import json
import joblib
from joblib import dump, load
import os
from time import time
import numpy as np

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Lending Prediction Tool", 
		  description = "Tools for Lender Simulation and Evaluation")


#input:[1,1,4,3,3,1,2,6,5,4]
#POST /simulator-model 
#{"inputIntList":[1,2,3,4,5,6,7,8,9,10]}
#{"input":[1,1,4,3,3,1,2,6,5,4,4,1]}

#POST /simulator-model
# response /simulator-model
#{"category": 3}

@app.route("/api/simulator-model")
class SimulatorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
	#@app.expect(model1)		
	def post(self):
		try:
			simulatorClassifier = joblib.load("./models/rf_simulator.model")
			formData = request.get_json()
			print(formData)
			data = [val for val in formData.values()]
			print(data)
			prediction = simulatorClassifier.predict(np.array(data).reshape(1, -1))
			print(prediction[0])
			pred_str = prediction[0]
			pred_int = int(pred_str)
			return_value = {}
			return_value = {
				'category' : pred_int
			}
			return jsonify(return_value)
		except KeyError as e:
			app.abort(500, e.__doc__, status = "Server Error", statusCode = "500")
		except Exception as e:
			print(e)
			app.abort(400, e.__doc__, status = "Simulator Model Invalid Data", statusCode = "400")
			
			
@app.route("/api/evaluator-model")
class EvaluatorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
	#@app.expect(model2)		
	def post(self):
		try:
			evaluatorClassifier = joblib.load('./models/gb_lender.model')
			formData = request.get_json()
			print(formData)
			data = [val for val in formData.values()]
			print(data)
			prediction = evaluatorClassifier.predict(np.array(data).reshape(1, -1))
			print(prediction[0])
			pred_str = prediction[0]
			pred_int = int(pred_str)
			return_value = {}
			return_value = {
				'category' : pred_int
			}
			return jsonify(return_value)
		except KeyError as e:
			app.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			app.abort(400, e.__doc__, status = "Evaluate Model Invalid Data", statusCode = "400")
