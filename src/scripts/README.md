# KASI Insight ML Scripts

## Prerequisites

To successfully run KASI Insight ML scripts please make sure that you have python v 3.7 or newer installed. Also make sure the `setuptools` package is installed. To install the package run `pip install -U setuptools`


## KASI Insight Script Installation

* Using command prompt tool navigate to the `..\src` folder of the project. For Windows use `cmd` in admin mode.
* Execute `pip install ./scripts`
* Verify that the *kasi* module is installed executing `pip list`. Find the package name in the list.


## Data Processor

This script normalizes raw survey data. The result of the script is an *.csv file that contains clean categorised data. 

To execute the script run `kasi_process --input_dir [path_to_raw_data] --output_file [path_with_filename_to_store_clean_data]`

To get more info about the script run `kasi_process -h`

Example: `kasi_process --input_dir C:/data/raw --output_file C:/data/processed/clean_data.csv`

## Hyper-parameter Tuning

**NOTE!** This is an optional script
The hyper parameter tuning script is searching the best parameters for a given algorithm and model.

At the moment of writing the following algorithm have been considered:

* Random Forest
* Support Vector Machine
* Gradient Boosting Classifier

To execute the script run `kasi_tune --algoritm [algorithm] --model [siulator/evaluator] --input_file [path_to_clean_data_file] --output_dir [path_to_the_output_directory]`

Example: `kasi_tune --algorithm rf --model simulator --input_file ../clean/clean_data.csv --output_dir ./tuning`
 

## Model Training

The model training script trains either simulator or evaluator model employing one of the following algorithms:

* Random Forest (rf)
* Support Vector Machine (svm)
* Gradient Boosting Classifier (gb)

The script can either apply parameters found during the algorithm tuning exercise (default behaviour).
Or it can use default algorithm settings (the --default parameter should be set to *True*)

To execute the script run `kasi_train --algoritm [algorithm] --model [siulator/evaluator] --input_file [path_to_clean_data_file] --output_dir [path_to_the_output_directory] --default`

Example: `kasi_train --algorithm rf --model simulator --input_file ../clean/clean_data.csv --output_dir ./training`

The script generates a number of artifacts, namely:

* model image as a file with the extension *.model
* model stats as a text file (extension *.txt)
* confusion matrix image (*.png file)
* learning curves image (*.png file)

The generated file have the following naming convention:

`[model]_[algorithm]_[params]_[purpose].extension`

Where

- model: `simultor` or `evaluator`
- algorithm: `rf`, `gb` or `svm`
- params: `tuned` or `default`
- purpose (optional): `curves`, `stats`, `matrx`
- extension: `txt`, `model`, `png`

Example: *evaluator_svm_tuned_stats.txt*