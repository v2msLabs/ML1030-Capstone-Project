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
