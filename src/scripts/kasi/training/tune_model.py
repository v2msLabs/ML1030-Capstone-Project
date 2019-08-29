import argparse
import time
import pandas as pd
from imblearn.over_sampling import SMOTE
from . import common as c
import os

"""

    This module performs hyper-parameter tuning for the simulator and evaluator models.
    The module is not required for model re-training.

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
        help='Which algorithm to tune the hyper-parameters for. Acceptable values: {0}. Example: rf'.format(
            c.algorithms))
    parser.add_argument(
        '--model',
        type=str,
        required=True,
        help='Which model to tune the hyper-parameters for. Acceptable values: simulator, evaluator. Example: simulator')
    parser.add_argument(
        '--input_file',
        type=str,
        required=True,
        help='Full input path to clean (pre-processed) data in *csv format. Example: ./clean_data/clean.csv')
    parser.add_argument(
        '--output_dir',
        type=str,
        required=True,
        help='Output path. This is where the script saves the recommended hyper-parameters as a text file. Example: ./tuning')
    args, _ = parser.parse_known_args()
    return args


"""
Main entry point of the script that starts the tuning process
"""


def main():
    start = time.time()
    args = get_args()
    file = os.path.join(args.output_dir, "{0}_{1}_tuning.txt".format(args.model, args.algorithm))
    c.create_dir(file)
    print("Started {0} hyper-parameter tuning for {1}".format(c.algorithms[args.algorithm], args.model))
    gs, params = c.get_gridsearch_instance(args.algorithm)
    df = pd.read_csv(args.input_file)
    columns, label = c.get_columns_label(args.model)
    data = df[columns]
    credit_score = df[label]
    # upsample
    train, train_class = SMOTE().fit_resample(data, credit_score)
    with open(file, 'w') as f:
        print(params, file=f)
        print(label, file=f)
        print(columns, file=f)
        _ = gs.fit(train, train_class)
        print("Best {0} algorithm score: {1}".format(c.algorithms[args.algorithm], gs.best_score_), file=f)
        print("Best hyper-parameters:", file=f)
        bestParams = gs.best_estimator_.get_params()
        for paramName in sorted(params.keys()):
            print("\t%s: %r" % (paramName, bestParams[paramName]), file=f)
    print("The recommended hyper-parameters have been saved in {}".format(file))
    print("Finished. Elapsed time(sec): {0}".format(time.time() - start))


if __name__ == '__main__':
    main()
