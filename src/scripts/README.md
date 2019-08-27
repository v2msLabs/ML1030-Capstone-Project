#KASI Insight ML Scripts

## Prerequisites

To successfully run KASI Insight ML scripts make sure that you have python v 3.6 or newer installed.



## Data Processor

This script normalizes raw survey data. The result of the script is an *.csv file that contains clean categorised data. 

To run the script make sure your current directory is `../scripts`

To get more info about the script run `python -m scripts.processing.data_processor -h`

Example: `python -m scripts.processing.data_processor --input_path ../data/raw/* --output_path ../data/processed/clean_data.csv`


## Simulator Model Training

## Evaluator Model Training
