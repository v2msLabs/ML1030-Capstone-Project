import pandas as pd
import time
import argparse
from sklearn.model_selection import learning_curve, train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump
from . import common as c
import matplotlib.pyplot as plt
import seaborn as sns
import os

"""Argument parser.
Returns:
  Dictionary of arguments.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_file',
        type=str,
        required=True,
        help='Full input path to clean (pre-processed) data in *csv format. Example: ./clean_data/clean.csv ')
    parser.add_argument(
        '--output_dir',
        type=str,
        required=True,
        help='The output path where the script saves the trained model and other artifacts. Example: ./model')
    args, _ = parser.parse_known_args()
    return args


"""
Trains simulator model
"""

def main():
    print("Started simulator model training...")
    start = time.time()
    args = get_args()
    mf = os.path.join(args.output_dir,"simulator.model")
    sf = os.path.join(args.output_dir,"simulator.stats.txt")
    imf = os.path.join(args.output_dir,"simulator_confusion_matrix.png")
    imlf = os.path.join(args.output_dir,"simulator_learning_curves.png")
    c.create_dir(mf)

    df = pd.read_csv(args.input_file)
    columns,label = c.get_columns_label(c.simulator_model)
    data = df[columns]
    credit_score = df[label]
    # split to train/test 70/30
    train, test, train_class, test_class = train_test_split(data, credit_score, test_size=0.3)
    # upsample both training sets
    train, train_class = SMOTE().fit_resample(train, train_class)
    # the parameters of the classifier were identified by the rf_tuning module
    model = RandomForestClassifier(n_estimators=200, min_samples_split=5,bootstrap=False,max_features='sqrt')
    # fit the model
    _ = model.fit(train, train_class)
    # calculate stats
    rfp = model.predict(test)
    rfr = classification_report(test_class, rfp)
    rfcm = confusion_matrix(test_class, rfp)
    dump(model, mf)

    with open(sf, 'w') as f:
        print("Simulator  model score: {:.4}".format(model.score(test, test_class)),file=f)
        print(rfr, file=f)

    sns.heatmap(pd.DataFrame(rfcm), annot=True, fmt="d", cmap='Set2')
    plt.savefig(imf)
    plt.close('all')
    # chart model learning curves
    train_sizes, train_scores, validation_scores = learning_curve(estimator=model, X=train, y=train_class, cv=3)
    train_scores_mean = train_scores.mean(axis=1)
    validation_scores_mean = validation_scores.mean(axis=1)
    _ = plt.plot(train_sizes, train_scores_mean, 'o-', label='Training error')
    _ = plt.plot(train_sizes, validation_scores_mean, 'o-', label='Validation error')

    _ = plt.ylabel('Error', fontsize=14)
    _ = plt.xlabel('Training set size', fontsize=14)
    _ = plt.legend()
    _ = plt.ylim(1.5, 0)
    plt.savefig(imlf)

    print("Finished. Elapsed time(sec): {0}".format(time.time() - start))


if __name__ == '__main__':
    main()
