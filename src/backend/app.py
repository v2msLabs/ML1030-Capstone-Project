#!/usr/local/bin/python3

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask import render_template
from flask_cors import CORS
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import joblib
from joblib import dump, load
import os
from time import time
import numpy as np
import sklearn

flask_app = Flask(__name__, static_url_path='')
CORS(flask_app)
#flask_app = Flask(__name__, static_url_path='', static_folder='backend/static', template_folder='backend/templates')
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Lending Prediction Tool", 
		  description = "Tools for Lender Simulation and Evaluation")
CORS(flask_app)

name_space = app.namespace('api', description='Simulator and Evaluator Lending support Tools')

simulatorModel = app.model('Simulator Model', 
				  {'input': fields.List(fields.Integer(required = True, 
														default = "1,1,4,3,3,1,2,6,5",
														description="Use this integer array of size 9 to test Simulator model", 
														help="Input Integer array cannot be blank or size less than 9."))})

evaluatorModel = app.model('Evaluator Model', 
				  {'input': fields.List(fields.Integer(required = True, 
														default = "1,1,4,3,3,1,2,6,5,4",
														description="Use this integer array of size 10 to test Evaluator model", 
														help="Input Integer array cannot be blank or size less than 10."))})



#model = {'input': fields.List(fields.int)}
#resource_fields = {'name': fields.String, 'first_names': fields.List(fields.String)}

#input:[1,1,4,3,3,1,2,6,5,4]
#POST /simulator-model 
#{"inputIntList":[1,2,3,4,5,6,7,8,9]}
#{"input":[1,1,4,3,3,1,2,6,5,4,4,1]}

#POST /simulator-model
# response /simulator-model
#{"category": 3}

@name_space.route("/simulator-model")
class SimulatorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument, Input needs to be Integer Array of Size 9', 500: 'Mapping Key Error' },
		params={ 'input': 'Integer array of size 9 for simulator model' })
	@app.expect(simulatorModel)
	def post(self):
		try:
			print("Entry simulator classifier")
			print("before joblib loading simulator classifier")
			simulatorClassifier = joblib.load('./models/simulator_rf_tuned_large.model')
			print("after joblib loading simulator classifier")
			formData = request.get_json()
			print("after reading input form data simulator classifier")
			data = [val for val in formData.values()]
			prediction = simulatorClassifier.predict(np.array(data).reshape(1, -1))
			print("after prediction simulator classifier")
			print(prediction[0])
			pred_str = prediction[0]
			pred_int = int(pred_str)
			return_value = {}
			return_value = {
				'category' : pred_int
			}
			print("Exit simulator classifier")
			return jsonify(return_value)
		except KeyError as e:
			print(e)
			app.abort(500, e.__doc__, status = "Server Error", statusCode = "500")
		except Exception as e:
			print(e)
			app.abort(400, e.__doc__, status = "Simulator Model Invalid Data", statusCode = "400")
			
@name_space.route("/evaluator-model")			
class EvaluatorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument, Input needs to be Integer Array of Size 10', 500: 'Mapping Key Error' },
		params={ 'input': 'Integer array of size 10 for Evaluator model' })
	@app.expect(evaluatorModel)
	def post(self):
		try:
			print("Entry evaluator classifier")
			print("before joblib loading evaluator classifier")
			evaluatorClassifier = joblib.load('./models/evaluator_rf_tuned_large.model')
			print("after joblib loading evaluator classifier")
			formData = request.get_json()
			print("after reading input form data evaluator classifier")
			data = [val for val in formData.values()]
			prediction = evaluatorClassifier.predict(np.array(data).reshape(1, -1))
			print("after prediction evaluator classifier")
			print(prediction[0])
			pred_str = prediction[0]
			#pred_str = "0"
			pred_int = int(pred_str)
			return_value = {}
			return_value = {
				'category' : pred_int
			}
			print("Exit evaluator classifier")
			return jsonify(return_value)
		except KeyError as e:
			print(e)
			app.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			print(e)
			app.abort(400, e.__doc__, status = "Evaluate Model Invalid Data", statusCode = "400")

if __name__=="__main__":
    flask_app.run(host='0.0.0.0', debug=True)
