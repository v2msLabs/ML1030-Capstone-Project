import pandas as pd
import re
import glob
import time
from . import dictionaries  as dc
from . import category_maps as maps
from ..training import common as c
import argparse

"""Argument parser.
Returns:
  Dictionary of arguments.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_dir',
        type=str,
        required=True,
        help='An input directory where the survey files in <<csv>> format are stored. Example: ./raw_data')
    parser.add_argument(
        '--output_file',
        type=str,
        required=True,
        help='A full path with a file name which will store the processed data in <<csv>> format. This file will be used to train the models. Example: ./clean/clean_data.csv')
    args, _ = parser.parse_known_args()
    return args


"""
Map a value to a category
"""


def categorize(val, map, default_category=0):
    if (pd.isna(val)):
        return default_category
    else:
        v = map.get(val)
        if v:
            return v
        else:
            return default_category


"""
 Ranks/ categorizes values using a dictionary of ranges
 Used ot rank the credit score, lending amounts, etc. 
"""


def rank(ranges, value, default_rank=0):
    i = 1
    ln = len(ranges)
    for k, v in ranges.items():
        l = len(v)
        if l == 1 and value <= v[0]:
            return k
        elif l > 1 and v[0] <= value <= v[1]:
            return k
        elif i == ln and l == 1 and value >= v[0]:
            return k
        i = i + 1
    return default_rank


""" 
Categorizes monetary values stored in  free text format 
"""


def categorize_amount(val, country, default_category=2):
    if pd.isna(country):
        raise Exception('Country parameter is mandatory')
    amounts = [int(i) for i in re.findall('\d+', str(val).replace(",", ""))]
    ranges = dc.amount_per_country[country]
    l = len(amounts)
    if (l == 0):  # the lowest range
        return default_category
    else:
        c1 = rank(ranges, amounts[0])
        if l > 1:
            return max(c1, rank(ranges, amounts[1]), default_category)
        else:
            return c1


"""
Cleans one observation (row)
"""


def process_row(row):
    try:
        row[2] = categorize(row[2], maps.map_col2, default_category=2)
        row[3] = categorize(row[3], maps.map_col3_5, default_category=2)
        row[4] = categorize(row[4], maps.map_col4, default_category=2)
        row[5] = categorize(row[5], maps.map_col3_5, default_category=2)
        row[6] = categorize(row[6], maps.map_col6_7_8, default_category=2)
        row[7] = categorize(row[7], maps.map_col6_7_8, default_category=2)
        row[8] = categorize(row[8], maps.map_col6_7_8, default_category=2)
        row[9] = categorize(row[9], maps.map_col9, default_category=2)
        row[10] = categorize(row[10], maps.map_col10, default_category=2)
        row[11] = categorize(row[11], maps.map_col11, default_category=4)
        row[12] = categorize(row[12], maps.map_col12, default_category=4)
        row[13] = categorize(row[13], maps.map_col13, default_category=3)
        row[14] = categorize(row[14], map=maps.map_col14)
        row[16] = categorize(row[16], map=maps.map_col16)
        row[18] = categorize(row[18], map=maps.map_col18, default_category=2)
        row[19] = categorize_amount(row[19], country=row[16])
        row[20] = categorize(row[20], map=maps.map_col20, default_category=2)
        row[21] = categorize(row[21], map=maps.map_col21, default_category=2)
        row[22] = categorize(row[22], map=maps.map_col22_23_24, default_category=3)
        row[23] = categorize(row[23], map=maps.map_col22_23_24, default_category=3)
        row[24] = categorize(row[24], map=maps.map_col22_23_24, default_category=3)
        row[25] = categorize(row[25], maps.map_col25, default_category=3)
        row[26] = categorize(row[26], maps.map_col26, default_category=2)
        row[27] = categorize(row[27], maps.map_col27_28_34_35, default_category=1)
        row[28] = categorize(row[28], maps.map_col27_28_34_35, default_category=1)
        row[29] = categorize(row[29], map=maps.map_col29, default_category=2)
        row[30] = categorize(row[30], maps.map_col30_31_32, default_category=2)
        row[31] = categorize(row[31], maps.map_col30_31_32, default_category=2)
        row[32] = categorize(row[32], maps.map_col30_31_32, default_category=2)
        row[33] = categorize(row[33], maps.map_col33)
        row[34] = categorize(row[34], maps.map_col27_28_34_35, default_category=1)
        row[35] = categorize(row[35], maps.map_col27_28_34_35, default_category=1)
        row[36] = categorize(row[36], maps.map_col36, default_category=8)
        row[37] = categorize_amount(row[37], country=row[16])
        # formula ingredients
        # credit score
        # risk
        recipient_w = dc.cs_recipient_weights[row[20]]
        interest_w = dc.cs_interest_weights[row[22]]
        collateral_w = dc.cs_collateral_weights[row[23]]
        # liquidity
        frequency_w = dc.cs_frequency_weights[row[18]]
        duration_w = dc.cs_duration_weights[row[21]]
        amount_w = dc.cs_amount_weights[row[19]]
        # collection
        collection_w = dc.cs_collection_weights[row[24]]
        # usage
        usage_w = dc.cs_usage_weights[row[26]]
        row["credit_score"] = round((recipient_w + interest_w + collateral_w + frequency_w +
                                     duration_w + amount_w + collection_w + usage_w) * 1000)
        row["credit_score_category"] = rank(dc.credit_ranking, row["credit_score"], default_rank=2)
        # lender score
        # risk
        recipient_w = dc.ls_recipient_weights[row[20]]
        interest_w = dc.ls_interest_weights[row[22]]
        collateral_w = dc.ls_collateral_weights[row[23]]
        # liquidity
        frequency_w = dc.ls_frequency_weights[row[18]]
        duration_w = dc.ls_duration_weights[row[21]]
        amount_w = dc.ls_amount_weights[row[19]]
        # collection
        collection_w = dc.ls_collection_weights[row[24]]
        # usage
        usage_w = dc.ls_usage_weights[row[26]]
        row["lender_score"] = round((recipient_w + interest_w + collateral_w + frequency_w +
                                     duration_w + amount_w + collection_w + usage_w) * 1000)
        row["lender_score_category"] = rank(dc.credit_ranking, row["lender_score"], default_rank=2)
        return row
    except:
        ## do nothing
        return None


"""
  Processes input data converting alphanumeric/ numeric values to numeric categories
"""


def run(input_path):
    paths = glob.glob("{0}/*.csv".format(input_path))
    if pd.isna(len(paths) == 0):
        print('No input files found for processing')
        return
    print("Processing the following files: {}".format(paths))
    df = pd.concat([pd.read_csv(f, names=range(0, 38), header=0, low_memory=False) for f in paths],
                   ignore_index=True)
    df = df.drop([15, 17], axis=1)  # drop Neighborhood name and Race/Ethnicity
    return df.apply(lambda row: process_row(row), axis=1)


"""
Main entry point
"""


def main():
    start = time.time()
    args = get_args()
    df = run(args.input_dir)
    c.create_dir(args.output_file)
    # remove dirty rows
    clean = df[df[0].notnull()]
    int_col = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26,
               27, 28, 29, 30, 31, 32, 33, 34, 35, 36, "credit_score", "credit_score_category",
               "lender_score", "lender_score_category"]
    final = clean.copy()
    final[int_col] = clean[int_col].astype(int)
    final.to_csv(index=False, path_or_buf=args.output_file)
    print("The processed data has been saved in {}".format(args.output_file))
    print("Finished. Elapsed time(sec): {0}".format(time.time() - start))


if __name__ == '__main__':
    main()
