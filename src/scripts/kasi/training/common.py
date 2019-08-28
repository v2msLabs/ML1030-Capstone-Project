import os
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
"""

This module maintains the code which is used by all training modules

"""

simulator_columns = ['24', '26', '22', '18', '20', '23', '19', '16', '36', '25']
evaluator_columns = ['24', '18', '22', '23', '20', '26', '19', '25', '16', '12', '11', '21']
simulator_label = 'credit_score_category'
evaluator_label = 'lender_score_category'
simulator_model = 'simulator'
evaluator_model = 'evaluator'
rf_algorithm = 'rf'
svm_algorithm = 'svm'
gb_algorithm = 'gb'

algorithms = {rf_algorithm: "Random Forest", svm_algorithm: "Support Vector Machine", gb_algorithm: "Gradient Boosting"}


def get_columns_label(model):
    columns = simulator_columns if model == simulator_model else evaluator_columns
    label = simulator_label if model == simulator_model else evaluator_label
    return columns, label


def create_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def get_gridsearch_instance(algorithm,cv=3):
    params = {}
    model = None
    if algorithm == rf_algorithm:
        params = {'n_estimators': [200, 300, 400], 'min_samples_split': [5, 10, 20, 30, 40],
                'max_features': ['auto', 'sqrt'], 'bootstrap': [True, False]}
        model = RandomForestClassifier()
    elif algorithm == gb_algorithm:
        params =  {'n_estimators': [200, 300], 'learning_rate': [0.1, 1.0, 1.2], 'min_samples_split': [5, 20, 30],
                'max_depth': [3, 6]}
        model = GradientBoostingClassifier()
    else:
        params = {}
        model = SVC()
        # finish for svm
    return GridSearchCV(model, params, cv=cv),params
