# This file maintains categorization dictionaries for categorical
# columns of the data set
# If you add more categories to a column extend the respective dictionary
# and run the data preprocessor
# NOTE: the dictionaries may contain more categories than the latest survey
# because the dictionaries wer compile based on the real values of the data set
# which, apparently over time collected all variations of the possible answers

cat_col2 = {'Difficult / Plus difficile': 1, 'Same / Pareil': 2, 'Easier / Plus facile': 3}
cat_col3_5 = {'No / Non': 1, 'Maybe / Peut-être': 2, 'Yes / Oui': 3}
cat_col4 = {'More / Plus': 1, 'Same / Pareil': 2, 'Less / Moins': 3}
cat_col6_7_8 = {'Improve / Améliorée': 1, 'Stay the same / La même': 2, 'Worsen / Détériorée': 3}
cat_col9 = {'Female / Femme': 1, 'Male / Homme': 2, 'Female /\xa0Femme': 1,
            'Male /\xa0Homme': 2}
cat_col10 = {'Separated, but not divorced / Séparé mais pas divorcé': 5,
             'Dating / En couple': 3, 'Married / Marié': 2, 'Widowed / Veuf (ve)': 7,
             'Not married, but living with my partner / Pas marié mais vivant avec mon partenaire': 5,
             'Divorced / Divorcé': 6, 'Single / Célibataire': 1, 'Married /\xa0Marié': 2,
             'Single /\xa0Célibataire': 1, 'Dating /\xa0En couple': 3}
cat_col11 = {'18-24': 2, '25-29': 3, '40-44': 6, '35-39': 5, '30-34': 4, '45-54': 7, '55-64': 8,
             'less than 17 years': 1, '65+': 9, '45+': 7, '-17': 1, '35 - 44': 5, '18 - 24': 2,
             '25 - 34': 3, '45 - 54': 7, '55 +': 8}
cat_col12 = {'High school, no diploma / BEPC': 2, 'Bachelor’s degree / Licence': 5,
             'Currently studying / Aux études': 9,
             'Trade/technical/vocational training / Diplome technique': 4,
             "Master's degree / Maitrise (DEA)": 6,
             'High school diploma / Baccalauréat': 3,
             'Professional Qualification e.g. CIMA / Qualification professionelle (ex. CFA)': 10,
             "No formal schooling / Pas d'étude": 1, 'Doctorate degree / Doctorat': 7,
             'Secondary School': 0, 'CPA T': 4, 'driver': 10, 'Certificate': 10, 'CPSP': 10,
             'basic computer knowledge': 2, 'DIPLOMA IN ICT': 10, 'Student': 9, 'WAEC': 10,
             'COLLEGE': 4, 'GCE': 10, 'Ordinary Level': 0, 'STUDENT': 9, 'student': 9,
             'STANDARD SEVEN': 9, 'ELECTRONICS': 3, 'College': 4, 'Honours': 5,
             'high school': 3, 'college': 4, 'honors': 5, 'Primary School ': 0, 'BECE': 4,
             'nationlal technical cert': 4, 'ssce': 4, 'national diploma(ND)': 4,
             'Diploma': 4, 'NOR': 0, 'adult education': 3, 'diploma': 4,
             "Certificat d'aptitude professionnelle": 10, 'RAS': 10}
cat_col13 = {'Salaried employee / Salarié': 2, 'Unemployed / Sans emploi': 5,
             'Business owner / Commercant': 4,
             'Commission-based employee / Employé sous commission': 3,
             'Self Employed / Entrepreneur': 7, 'Contractor / Consultant': 8,
             'Student / Etudiant': 1,
             "Not looking for employment / Pas a la recherche d'emploi": 6,
             'Retired / Retraité': 9, 'self employed': 7,
             'Business owner and salaried employee': 4, 'Self Employed': 7,
             'CONSULTANT': 8, 'housewife': 5, 'retired': 9,
             'Salaried employee and student': 2, 'Retires': 9, 'Pastor': 3, 'Apprentice': 1,
             'Self employed': 7, 'Employed with business': 7, 'Part time employee': 2,
             'Business owner and also salaried employee': 2,
             'Employed and with a business': 2, 'Hair stylist': 2, 'Retired': 9,
             'Politician': 7, 'Salaried withBusiness': 2, 'Employee and Student': 2,
             'Part time student and business': 4, 'Student with Business': 4,
             'Busiiness and employee': 2, 'Employed, Business owner': 2,
             'Salaried and I have a business': 2, 'Employed and a business': 2,
             'Business and also employed': 2,
             'Advocate, Lecturer & Campaign agent ': 7, 'serving': 2, 'hairdresser ': 2,
             'serving corper': 2, 'Part time Business and student': 1,
             'Business and Employed': 2, 'Part time Business and Employed': 2,
             'Partime employee and student': 2, 'pharmaceutical technician': 2,
             'serving Corper': 2, 'serving youth corp member': 2, 'farmer I': 4,
             'Trader': 4, 'serving Corper:': 2, 'PARTLY STUDENT': 1, 'RETIRED': 9,
             'Part time student': 1, 'employed and business owner': 2,
             'part time student': 1, 'STUDENT AND BUSINESS': 1,
             'EMPLYMENT AND BUSINESS': 2, 'EMPLOYMENT AND BUSINESS': 2,
             'SELF EMPLOYEE': 7, 'chemical engineer': 2, 'Consultant': 7, 'farmer': 4,
             'student/Buz owner': 1, 'Non Working again': 5, 'driver': 2, 'Marketer': 3,
             'stylist-baber': 2, 'pastor': 3, 'Electrical Engineering': 2, 'engineering': 2,
             'business and salary earner': 2, 'films makre': 2, 'apprentice ': 1,
             'fashionist': 2, 'Driver': 2, 'Salaried employee /\xa0Salarié': 2,
             'Business owner /\xa0Commercant': 4, 'Unemployed /\xa0Sans emploi': 5,
             'Student /\xa0Etudiant': 1, 'student and worker': 1, 'national service': 2,
             'elève': 0, 'pasteur': 3, 'propre compte': 4, 'élève': 0, 'chantre': 3, 'menage': 5,
             'ferronnier': 2}
cat_col14 = {'Technical or Other college diploma / Collège technique': 1,
             'I am not a student / Je ne suis pas un étudiant': 2,
             'Undergraduate Degree / Université niveau Licence': 2,
             'Post Graduate Degree / Université Niveau Maitrise ou Doctorat': 3,
             'Honours Degree / Spécialisation': 4}
cat_col16 = {'Cameroon': 1, "Cote d'Ivoire": 2, 'Ghana': 3, 'Kenya': 4, 'Nigeria': 5,
             'South Africa': 6, 'Tanzania': 7}
cat_cal18 = {'Between 2-3 times': 2, 'Once': 3, 'More than 4 times': 1, 'Never': 4,
             'Once / Une fois': 3, 'Between 2-3 times /\xa0Entre 2 et 3 fois': 2,
             'More than 4 times / Plus de 4 fois': 1, 'Never / Jamais': 4,
             'Plus de 4 fois': 1, 'Entre 2 et 3 fois': 2, 'Aucune': 0, 'Une fois': 3,
             'Jamais': 4, 'Une fois, Entre 2 et 3 fois': 2,
             'Entre 2 et 3 fois, Plus de 4 fois': 2, 'Une fois, Plus de 4 fois': 3,
             'Jamais, Entre 2 et 3 fois': 4, 'Jamais, Une fois, Entre 2 et 3 fois': 4,
             'Une fois, Entre 2 et 3 fois, Plus de 4 fois': 3,
             'Jamais, Plus de 4 fois': 4,
             'Jamais, Une fois, Entre 2 et 3 fois, Plus de 4 fois': 4,
             'Jamais, Une fois': 4}
cat_col20 = {'Business colleagues': 3, 'Friends': 2, 'Family': 1,
             'Family /\xa0La famille': 1, 'Friends /\xa0Les amis': 2,
             'Business colleagues / Collegues de travail': 3,
             'Les amis': 2, 'La famille': 1, 'Collegues de travail': 3}
cat_col21 = {'At least 3 months but less than 6 months': 3,
             'At least 1 month but less than 3 months': 2, 'Less than a month': 1,
             'One year or more': 5, 'At least 6 months but less than 12 months': 4,
             "Never - I don't expect to get repaid": 6,
             'At least 1 month but than 3 months': 2,
             'At least 3 months but less than 6 months / 3 - 5 mois': 3,
             "Less than a month / Moins d'un mois": 1,
             'At least 1 month but than 3 months /\xa01 - 2 mois': 2,
             'At least 6 months but less than 12 months / 6 - 11 mois': 4,
             "One year or more / Plus d'un an": 5, "Moins d'un mois": 1, '1 - 2 mois': 2,
             '3 - 5 mois': 3, '6 - 11 mois': 4, "Plus d'un an": 5}
cat_col22_23_24 = {'About half the time': 3, 'Occasionally': 4, 'Most of the time': 2, 'Never': 5,
                   'Always': 1, 'Never / Jamais': 5, 'Occasionally / Souvent': 4,
                   'Always /\xa0Toujours': 1, 'About half the time /\xa0La moitié du temps': 3,
                   'Most of the time /\xa0La majorité du temps': 2, 'Jamais': 5,
                   'La moitié du temps': 3, 'Souvent': 4, 'La majorité du temps': 2,
                   'Toujours': 1, 'About half the time / La moitié du temps': 3, 'Always / Toujours': 1,
                   'Most of the time / La majorité du temps': 2}
cat_col25 = {'At least 5-6 out of 10 times': 4, 'At least 7-8 out of 10 times': 3,
             'At least 9 out of 10 times': 2, 'Every time': 1,
             'Less than 5 out of 10 times': 5,
             'At least 5-6 out of 10 times / Au moins 5-6 fois sur 10': 4,
             'At least 7-8 out of 10 times / Au moins 7-8 fois sur 10': 3,
             'Less than 5 out of 10 times / Moins de 5 fois sur 10': 5,
             'At least 9 out of 10 times / 9 fois sur 10': 2,
             'Every time / Toutes les fois': 1, 'Au moins 7-8 fois sur 10': 3,
             'Toutes les fois': 1, 'Au moins 5-6 fois sur 10': 4, '9 fois sur 10': 2,
             'Moins de 5 fois sur 10': 5}
cat_col26 = {'To invest or cover business expenses (Merchandise, salaries, etc..)': 3,
             'To pay for one-time or sudden expenses (Wedding, medical emergencies, etc.)': 2,
             'To cover regular expenses (Rent, clothing, home appliances, etc.)': 1,
             'To pay off other debts': 4, "I don't know": 5,
             'Investment (commerce, merchandise, etc.)': 3,
             'Personal or family expenses (Health, education)': 1,
             'Pour payer des dépenses ponctuelles ou soudaines (mariage, urgences médicales, etc.)': 2,
             'Pour couvrir les dépenses régulières (loyer, vêtements, appareils ménagers, etc.)': 1,
             "Payer d'autres dettes": 4,
             'Pour investir ou couvrir les dépenses de votre entreprise (marchandises, salaires, etc.)': 3,
             'Je ne sais pas': 5, 'Régler les problèmes subits': 2,
             'Investir dans un projet': 3, "I don't know / Je ne sais pas": 5,
             'Personal or family expenses (Health, education) /\xa0Régler les problèmes subits': 1,
             'Investment (commerce, merchandise, etc.) / Investir dans un projet': 3}
cat_col27_28_34_35 = {'Yes': 1, 'No': 2, 'Not sure': 3, 'No - but I would like to apply': 2,
                      'Non': 2, 'Oui': 1, 'No / Non': 2, 'Yes /\xa0Oui': 1,
                      'No - but I would like to join one': 2,
                      "I don't know what a credit score is": 3, 'Yes / Oui': 1,
                      "Je ne sais pas ce que c'est": 3}
cat_col29 = {'Friends': 2, 'Family': 1, 'Lending Club': 4, 'Bank': 3, 'Micro finance': 5,
             'None of them ': 6, 'Loans are a bad idea ': 6, 'E no need ': 6, 'None': 6,
             'Place of work': 2, 'cellphone ie m-shwari': 5, 'sacco': 4,
             'Bank and lending club ': 3, 'tontin': 4, 'work place': 2, 'Friends and Family': 1,
             'business partners': 1, 'Banque': 3, 'Amis': 2, 'Tontine': 4, 'Famille': 1,
             'Friends /\xa0Amis': 2, 'Bank /\xa0Banque': 3,
             'Lending Club / Tontine': 4, 'Family /\xa0Famille': 1}
cat_col30_31_32 = {'4': 4, '2': 2, '3': 3, '5 - Definitely agree': 5, '1 - Definitely disagree': 1,
                   '5 - Complètement en accord': 5, '1 - Complètement en désaccord': 1}
cat_col33 = {'Student loan': 1, 'Mobile loan': 2, 'Bank loan': 3, 'Private loan': 4,
             'Car loan': 5, 'none': 6, 'no': 6, 'no one': 6, 'i dont owe anyone': 6,
             'Credit card loan': 7, 'NONE': 6, 'Mortgage loan': 8, 'none ': 6, 'not any': 6,
             ' none': 6, 'no ': 6, 'non of them currently': 6, 'NOT OWNING ': 6,
             'I DONT TAKE LOAN': 6, 'school fess': 1, 'Sacco': 3, 'SACCO loan': 3, 'Hakuna': 6,
             'None': 6, 'have  no loan': 6, 'I dont have any loan ': 6,
             'I dont have any loan at the moment ': 6, 'no loan': 6, 'NO': 6, 'No loan': 6,
             'Am not': 6, 'None ': 6, 'No': 6, 'Nope ': 6, 'Personal ': 4,
             "I didn't take loan": 6, "I don't owe": 6, "Pret personnel (ex. d'un ami)": 4,
             'Pret mobile': 2, 'Pret bancaire': 3, 'Pret auto': 5, "Pret d'étude": 1,
             'Carte de crédit (ex. carte bleu)': 7, 'Pret hypothécaire': 8}

cat_col36 = {'Less than 5%': 1, '5% -10%': 2, '10% - 20%': 3, '20% - 30%': 4,
             '30% - 40%': 5, '40% - 50%': 6,
             'More than half of my income goes to pay off rent': 7, "Don't Know": 8}
# the latest survey dictionaries(reversed).
#
gender = {2: "Male", 1: "Female"}
marital_status = {1: "Single", 2: "Married", 3: "Dating",
                  4: "Not married, but living with my partner",
                  5: "Separated, but not divorced", 6: "Divorced", 7: "Windowed"}
age_groups = {1: "Under 17", 2: "18-24", 3: "25-29", 4: "30-34", 5: "35-39", 6: "40-44",
              7: "45-54", 8: "55-64", 9: "65+"}
education = {1: "No formal schooling", 2: "High school, no diploma", 3: "High school diploma",
             4: "Trade/technical/vocational training", 5: "Bachelor’s degree",
             6: "Master's degree", 7: "Doctorate degree",
             9: "Currently studying", 10: "Professional Qualification e.g. CIMA"}
occupation = {1: "Student", 2: "Salaried employee", 3: "Commission-based employee",
              4: "Business owner", 5: "Unemployed", 6: "Not looking for employment",
              7: "Self employed", 8: "Contractor", 9: "Retired"}
study_subject = {1: "Technical or other college diploma", 2: "Undergraduate Degree",
                 3: "Post Graduate Degree", 4: "Honours Degree", 2: "I am not a student"}
countries = {1: 'Cameroon', 2: "Cote d'Ivoire", 3: 'Ghana', 4: 'Kenya', 5: 'Nigeria',
             6: 'South Africa', 7: 'Tanzania'}
