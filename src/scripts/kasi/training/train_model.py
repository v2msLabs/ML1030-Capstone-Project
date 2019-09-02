import pandas as pd
import time
import argparse
from sklearn.model_selection import learning_curve, train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump
from . import common as c
import matplotlib.pyplot as plt
import seaborn as sns
import os

"""

    This module performs training of the simulator and evaluator models.

"""

"""Argument parser.
Returns:
  Dictionary of arguments.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--algorithm',
        type=str,
        required=True,
        help='What algorithm to apply to train the model. Acceptable values: {0}. Example: rf'.format(c.algorithms))
    parser.add_argument(
        '--model',
        type=str,
        required=True,
        help='Which model to train. Acceptable values: simulator, evaluator. Example: simulator')
    parser.add_argument(
        '--input_file',
        type=str,
        required=True,
        help='Full input path to clean (pre-processed) data in *csv format. Example: ./clean_data/clean.csv')
    parser.add_argument(
        '--output_dir',
        type=str,
        required=True,
        help='Output path. This is where the script saves the model image and the accompanying artifacts. Example: ./models')
    parser.add_argument(
        '--default',
        type=bool,
        default=False,
        help='Train the model with the default parameters (optional). This feature is mainly used during the research phase. Example: True')
    parser.add_argument(
        '--feature_size',
        type=str,
        default="large",
        help='Specify the feature size to train the model (optional). Acceptable values: small, base , large (default). This fature is mainly used during the research phase.Example: large')
    args, _ = parser.parse_known_args()
    return args


"""
Main entry point of the script that starts the model training process
"""


def main():
    start = time.time()
    args = get_args()
    default = "default" if args.default else "tuned"
    mf = os.path.join(args.output_dir, "{0}_{1}_{2}_{3}.model".format(args.model, args.algorithm, default, args.feature_size))
    sf = os.path.join(args.output_dir, "{0}_{1}_{2}_{3}_stats.txt".format(args.model, args.algorithm, default, args.feature_size))
    imf = os.path.join(args.output_dir, "{0}_{1}_{2}_{3}_matrix.png".format(args.model, args.algorithm, default, args.feature_size))
    imlf = os.path.join(args.output_dir, "{0}_{1}_{2}_{3}_curves.png".format(args.model, args.algorithm, default, args.feature_size))
    c.create_dir(mf)

    print("Started {0} training employing {1} algorithm".format(args.model, c.algorithms[args.algorithm]))
    df = pd.read_csv(args.input_file)
    columns, label = c.get_columns_label(args.model,args.feature_size)
    data = df[columns]
    labels = df[label]
    # split to train/test 70/30
    train, test, train_class, test_class = train_test_split(data, labels, test_size=0.3)
    # upsample both training sets
    train, train_class = SMOTE().fit_resample(train, train_class)
    # the parameters of the classifier were identified by the rf_tuning module
    model = c.get_classifier(args.model, args.algorithm, args.default)
    # fit the model
    _ = model.fit(train, train_class)
    # calculate stats
    predictions = model.predict(test)
    report = classification_report(test_class, predictions)
    matrix = confusion_matrix(test_class, predictions)
    dump(model, mf)

    with open(sf, 'w') as f:
        print('Features:\n', file=f)
        print(columns, file=f)
        print('Parameters in use:\n', file=f)
        print(model.get_params(), file=f)
        print(
            "{} model with {} algorithm score: {:.4}".format(args.model, c.algorithms[args.algorithm],
                                                             model.score(test, test_class)),
            file=f)
        print(report, file=f)

    sns.heatmap(pd.DataFrame(matrix), annot=True, fmt="d", cmap='Set2')
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
