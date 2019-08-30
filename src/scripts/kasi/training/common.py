import os
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

"""

This module maintains the code which is used by all training modules

"""

simulator_columns = ['24', '26', '22', '18', '20', '23', '19', '16', '36', '25'] # replace 36 with 21
evaluator_columns = ['24', '18', '22', '23', '20', '26', '19', '25', '16', '12', '11', '21']
simulator_label = 'credit_score_category'
evaluator_label = 'lender_score_category'
simulator_model = 'simulator'
evaluator_model = 'evaluator'
rf_algorithm = 'rf'
svm_algorithm = 'svm'
gb_algorithm = 'gb'

algorithms = {rf_algorithm: "Random Forest", svm_algorithm: "Support Vector Machine", gb_algorithm: "Gradient Boosting"}

"""
This function returns a list of features and a label name for simulator and evaluator models
"""


def get_columns_label(model):
    columns = simulator_columns if model == simulator_model else evaluator_columns
    label = simulator_label if model == simulator_model else evaluator_label
    return columns, label


def create_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)


"""
Returns a GridSearch instance with the hyper-parameters to tune for specified algorithm
@param: algorithm - either "rf" or "svm" or "gb"
"""


def get_gridsearch_instance(algorithm, cv=3):
    params = {}
    model = None
    if algorithm == rf_algorithm:
        params = {'n_estimators': [200, 300, 400], 'min_samples_split': [5, 10, 20, 30, 40],
                  'max_features': ['auto', 'sqrt'], 'bootstrap': [True, False]}
        model = RandomForestClassifier()
    elif algorithm == gb_algorithm:
        params = {'n_estimators': [200, 300], 'learning_rate': [0.1, 1.0, 1.2], 'min_samples_split': [5, 20, 30],
                  'max_depth': [3, 6]}
        model = GradientBoostingClassifier()
    else:
        params = {'kernel': ['rbf', 'poly', 'linear'], 'gamma': ["auto", "scale"], 'shrinking': [True, False]}
        model = SVC()
    return GridSearchCV(model, params, cv=cv), params


"""
Returns a classifier instance with the  parameters identified during hyper-parameter tuning for a given model and algorithm

@param: model - either "simulator" or "evaluator"
@param: algorithm - either "rf" or "svm" or "gb"
@param: default - if True use the classifier with default (out of the box) settings. Otherwise apply the parameters selected during the model tuning phase  
"""


def get_classifier(model, algorithm, default=False):
    if algorithm == rf_algorithm:
        if default:
            return RandomForestClassifier()
        if model == simulator_model:
            return RandomForestClassifier(max_features='auto', n_estimators=200, min_samples_split=5,
                                          bootstrap=False)
        else:
            return RandomForestClassifier(n_estimators=400, min_samples_split=5, bootstrap=False,
                                          max_features='sqrt')
    elif algorithm == gb_algorithm:
        if default:
            return GradientBoostingClassifier()
        if model == simulator_model:
            # @TODO: finish
            return GradientBoostingClassifier(learning_rate=0.1, max_depth=6, min_samples_split=5, n_estimators=300)
        else:
            # @TODO: finish
            return GradientBoostingClassifier(learning_rate=0.1, max_depth=6, min_samples_split=5, n_estimators=300)
    else:
        if default:
            return SVC(gamma='scale')
        if model == simulator_model:
            # @TODO: finish
            return SVC(gamma='auto', kernel='rbf', shrinking=True)
        else:
            return SVC(gamma='auto', kernel='rbf', shrinking=True)
