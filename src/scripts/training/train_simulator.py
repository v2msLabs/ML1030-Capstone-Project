import pandas as pd
import time
import argparse
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from joblib import dump

"""Argument parser.
Returns:
  Dictionary of arguments.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_path',
        type=str,
        required=True,
        help='Full input path to cleaned (pre-processed) data in *csv format. Example: ./clean_data/clean.csv ')
    parser.add_argument(
        '--output_dir',
        type=str,
        required=True,
        help='Full output path where the script saves the trained model image. Example: ./model/simulator.model')
    args, _ = parser.parse_known_args()
    return args

def train(input_path):
    df = pd.read_csv(input_path)
    data = df[['24', '26', '22', '18', '20', '23', '19', '16', '36', '25']]
    credit_score = df['credit_score_category']
    # split to train/test 70/30
    train, test, train_class, test_class = train_test_split(data, credit_score, test_size=0.3)
    # upsample both training sets
    train, train_class = SMOTE().fit_resample(train, train_class)
    model = RandomForestClassifier(n_estimators=200, min_samples_split=20)
    _ = model.fit(train, train_class)
    rfp = model.predict(test)
    print("Simulator  model score: {:.4}".format(model.score(test, test_class)))
    rfr = classification_report(test_class, rfp)
    print(rfr)
    return model


if __name__ == '__main__':
    start = time.time()
    args = get_args()
    model = train(args.input_path)
    f = "{}clean_data.csv".format(args.output_dir)
    dump(model,args.output_path)
    print("The model has been saved in {}".format(args.output_path))
    print("Finished. Elapsed time(sec): {0}".format(time.time() - start))