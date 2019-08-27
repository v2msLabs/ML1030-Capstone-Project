import csv

#
# the latest survey dictionaries.
#
columns = {'0': "Timestamp",
           '1': "Location ID",
           '2': "Has it become more difficult or easier to find a job in your city?",
           '3': "Is this a good time for people to make a large purchase such as furniture or electrical appliances, given the economic climate?",
           '4': "Compared to the last 6 months, are you able to spend (more, the same or less) money on large purchases (furniture, electrical appliances) over the next 6 months?",
           '5': "Will you be able to meet your regular expenses over the next 6 months?",
           '6': "How do you expect your household’s income to change over the next 6 months?",
           '7': "How do you expect general economic conditions in your city to change over the next 6 months?",
           '8': "How do you expect general economic conditions in your country to change over the next 6 months?",
           '9': "Gender",
           '10': "Marital status",
           '11': "Age",
           '12': "What's your highest level of education?",
           '13': "Occupation",
           '14': "If you are a student, what level are you currently studying?",
           '15': "Race/Ethnicity",
           '16': "Country",
           '17': "What is the name of the neighborhood where you live?",
           '18': "Over the past 3 months, how many times have you lent someone money?",
           '19': "On average how much do you lend in general?",
           '20': "Who did you lend money to in the past 3 months?",
           '21': "When you lend money, when do you usually expect to get it repaid?",
           '22': "Do you include either interest or a lending fee when you lend?",
           '23': "Do you request guarantees when you lend?",
           '24': "Do you receive your money back in time?",
           '25': "Assuming that you have lent money at least ten times, how often would you get your money repaid?",
           '26': "What's the most common use of the money you lend?",
           '27': "Have you ever applied for a bank loan?",
           '28': "Are you a tontine / lending club member?",
           '29': "What is the most convenient way to get a loan?",
           '30': "To what extent do you agree with the following sentences [Access to credit is essential for me to achieve financial freedom]",
           '31': "To what extent do you agree with the following sentences [Credit is beneficial only if you have discipline]",
           '32': "To what extent do you agree with the following sentences [I would like to have more credit management training]",
           '33': "What type of loans are you currently paying of?",
           '34': "Do you have a credit score?",
           '35': "Do you have a credit card?",
           '36': "On average, how much of your total household monthly income do you spend paying off debt each month?",
           '37': "If you wanted to take a loan to start a business, how much would you need?"
           }
# Find Job in city
category_col2 = {0: 'Unknown', 1: 'Difficult', 2: 'Same', 3: 'Easier'}
#
category_col3_5 = {0: 'Unknown', 1: 'No', 2: 'Maybe', 3: 'Yes'}
# Spending on Large Purchases
category_col4 = {0: 'Unknown', 1: 'More', 2: 'Same', 3: 'Less'}
#
category_col6_7_8 = {0: 'Other', 1: 'Improve', 2: 'Stay the same', 3: 'Worsen'}
# gender
category_col9 = {0: "Unknown", 2: "Male", 1: "Female"}
# marital status
category_col10 = {0: "Unknown", 1: "Single", 2: "Married", 3: "Dating",
                  4: "Not married, but living with my partner",
                  5: "Separated, but not divorced", 6: "Divorced", 7: "Windowed"}
# age_groups
category_col11 = {0: "Unknown", 1: "Under 17", 2: "18-24", 3: "25-29", 4: "30-34", 5: "35-39", 6: "40-44",
                  7: "45-54", 8: "55-64", 9: "65+"}
# education
category_col12 = {0: "Other", 1: "No formal schooling", 2: "High school, no diploma", 3: "High school diploma",
                  4: "Trade/technical/vocational training", 5: "Bachelor’s degree",
                  6: "Master's degree", 7: "Doctorate degree",
                  9: "Currently studying", 10: "Professional Qualification e.g. CIMA"}
# occupation
category_col13 = {0: "Unknown/Other", 1: "Student", 2: "Salaried employee", 3: "Commission-based employee",
                  4: "Business owner", 5: "Unemployed", 6: "Not looking for employment",
                  7: "Self employed", 8: "Contractor", 9: "Retired"}
# Current Study Level
category_col14 = {0: 'Other', 1: 'Technical or Other college diploma', 2: 'Undergraduate Degree',
                  3: 'Post Graduate Degree', 4: 'Honours Degree'}
# countries
category_col16 = {1: 'Cameroon', 2: "Cote d'Ivoire", 3: 'Ghana', 4: 'Kenya', 5: 'Nigeria',
                  6: 'South Africa', 7: 'Tanzania'}
# Past 3 months lending habit
category_cal18 = {0: 'Other', 1: 'More than 4 times', 2: 'Between 2-3 times', 3: 'Once', 4: 'Never'}

# Average lend amount
category_col19 = {1: 'Micro', 2: 'Small', 3: 'Medium', 4: 'Large'}
# amount ranges per country
amount_per_country = {1: {1: [10000], 2: [10001, 59000], 3: [59001, 290000], 4: [290001]},
                      2: {1: [10000], 2: [10001, 59000], 3: [59001, 290000], 4: [290001]},
                      3: {1: [90], 2: [91, 444], 3: [445, 2200], 4: [2201]},
                      4: {1: [1999], 2: [2000, 10499], 3: [10500, 49999], 4: [50000]},
                      5: {1: [6000], 2: [6001, 31000], 3: [31001, 160000], 4: [160001]},
                      6: {1: [250], 2: [251, 1200], 3: [1201, 6400], 4: [6401]},
                      7: {1: [44999], 2: [45000, 199999], 3: [200000, 1000000], 4: [1000001]}}
# Whom did you lend money
category_col20 = {0: "Unknown", 1: 'Family', 2: 'Friends', 3: 'Business colleagues', 4: "Other"}
# When do you expect to get repaid
category_col21 = {0: 'Other', 1: 'Less than a month', 2: 'At least 1 month but less than 3 months',
                  3: 'At least 3 months but less than 6 months', 4: 'At least 6 months but less than 12 months',
                  5: 'One year or more', 6: "Never - I don't expect to get repaid"}
# Lending fee, interest, guarantee,
category_col22_23_24 = {0: 'Unknown', 1: 'Always', 2: 'Most of the time', 3: 'About half the time', 4: 'Occasionally',
                        5: 'Never'}
# After lending for at least 10 times, how often money is repaid
category_col25 = {0: 'Other', 1: 'Every time', 2: 'At least 9 out of 10 times', 3: 'At least 7-8 out of 10 times',
                  4: 'At least 5-6 out of 10 times', 5: 'Less than 5 out of 10 times'}
# Most common use of the money that was lent
category_col26 = {1: 'To cover regular expenses (Rent, clothing, home appliances, etc.)',
                  2: 'To pay for one-time or sudden expenses (Wedding, medical emergencies, etc.)',
                  3: 'To invest or cover business expenses (Merchandise, salaries, etc..)',
                  4: 'To pay off other debts', 5: "I don't know"}
#
category_col27_28_34_35 = {0: 'Not sure', 1: 'Yes', 2: 'No'}
# Most Convenient way to get Loan
category_col29 = {1: 'Family', 2: 'Friends', 3: 'Bank', 4: 'Lending Club', 5: 'Micro finance', 6: 'None of them'}
#
category_col30_31_32 = {0: 'Other', 1: 'Definitely disagree', 2: '2', 3: '3', 4: '4', 5: 'Definitely agree'}
# Types of loans currently being paid off
category_col33 = {0: 'Other', 1: 'Student loan', 2: 'Mobile loan', 3: 'Bank loan', 4: 'Private loan', 5: 'Car loan',
                  6: "I don't owe", 7: 'Credit card loan', 8: 'Mortgage loan'}
# On an average, amount of debt being paid off each month of total household income
category_col36 = {1: 'Less than 5%', 2: '5% -10%', 3: '10% - 20%', 4: '20% - 30%', 5: '30% - 40%', 6: '40% - 50%',
                  7: 'More than half of my income goes to pay off rent', 8: "Don't Know"}
# credit score weights, where first member of a list is an internal group weight
# and the second member is a contributor to the overall group weight
# risk
cs_recipient_weights = {0: 0.0, 1: -0.05, 2: 0.10, 3: 0.10, 4: -0.05}
cs_interest_weights = {0: 0.0, 1: -0.10, 2: -0.05, 3: 0.05, 4: 0.08, 5: 0.12}
cs_collateral_weights = {0: 0.0, 1: -0.05, 2: -0.03, 3: 0.03, 4: 0.04, 5: 0.06}
# liquidity
cs_frequency_weights = {0: 0.0, 1: 0.10, 2: 0.07, 3: -0.02, 4: -0.05}
cs_duration_weights = {0: 0.0, 1: -0.02, 2: 0.02, 3: 0.03, 4: 0.04, 5: 0.05, 6: -0.02}
cs_amount_weights = {1: -0.05, 2: 0.03, 3: 0.05, 4: 0.07}
# collection
cs_collection_weights = {0: 0.0, 1: 0.35, 2: 0.25, 3: 0.15, 4: -0.10, 5: -0.30}
# usage
cs_usage_weights = {0: 0.0, 1: -0.10, 2: 0.05, 3: 0.15, 4: -0.05, 5: 0.05}
#
# lender score weights
#
ls_recipient_weights = {0: 0.0, 1: -0.05, 2: 0.10, 3: 0.10, 4: -0.05}
ls_interest_weights = {0: 0.0, 1: 0.08, 2: 0.05, 3: 0.02, 4: -0.02, 5: -0.03}
ls_collateral_weights = {0: 0.0, 1: 0.04, 2: 0.03, 3: 0.01, 4: -0.01, 5: -0.02}
# liquidity
ls_frequency_weights = {0: 0.0, 1: 0.10, 2: 0.07, 3: -0.02, 4: -0.05}
ls_duration_weights = {0: 0.0, 1: 0.01, 2: 0.02, 3: 0.02, 4: 0.04, 5: 0.05, 6: -0.04}
ls_amount_weights = {1: -0.05, 2: 0.03, 3: 0.05, 4: 0.07}
# collection
ls_collection_weights = {0: 0.0, 1: 0.35, 2: 0.25, 3: 0.15, 4: -0.10, 5: -0.30}
# usage
ls_usage_weights = {0: 0.0, 1: 0.05, 2: 0.02, 3: 0.06, 4: 0.02, 5: -0.05}
# credit ranking
credit_ranking = {1: [350], 2: [351, 550], 3: [551, 650], 4: [651, 750], 5: [751]}


def save_dictionary2csv(dictionary, output_path, field_names=['key', 'value']):
    try:
        with open(output_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for data in dictionary:
                writer.writerow(data)
    except IOError:
        print("I/O error")
