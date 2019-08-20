export const questions = {
    '2': "Has it become more difficult or easier to find a job in your city?",
    '3': "Is this a good time for people to make a large purchase such as furniture or electrical appliances, given the economic climate?",
    '4': "Compared to the last 6 months, are you able to spend (more, the same or less) money on large purchases (furniture, electrical appliances) over the next 6 months?",
    '5': "Will you be able to meet your regular expenses over the next 6 months?",
    '6': "How do you expect your household’s income to change over the next 6 months?",
    '7': "How do you expect general economic conditions in your city to change over the next 6 months?",
    '8': "How do you expect general economic conditions in your country to change over the next 6 months?",
    '9': "Gender?",
    '10': "Marital status?",
    '11': "Age?",
    '12': "What's your highest level of education?",
    '13': "Occupation?",
    '14': "If you are a student, what level are you currently studying?",
    '15': "Race/Ethnicity",
    '16': "Country?",
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

export const options22_23_24 = {
    1: 'Always', 2: 'Most of the time', 3: 'About half the time', 4: 'Occasionally',
    5: 'Never'
}
export const optionMap22_23_24 = new Map(Object.entries(options22_23_24));

export const options26 = {
    1: 'To cover regular expenses (Rent, clothing, home appliances, etc.)',
    2: 'To pay for one-time or sudden expenses (Wedding, medical emergencies, etc.)',
    3: 'To invest or cover business expenses (Merchandise, salaries, etc..)',
    4: 'To pay off other debts', 5: "I don't know"
}
export const optionMap26 = new Map(Object.entries(options26));

export const countries = {
    1: 'Cameroon', 2: "Cote d'Ivoire", 3: 'Ghana', 4: 'Kenya', 5: 'Nigeria',
    6: 'South Africa', 7: 'Tanzania'
};
export const countryMap = new Map(Object.entries(countries));

export const options11 = {
    1: "Under 17", 2: "18-24", 3: "25-29", 4: "30-34", 5: "35-39", 6: "40-44",
    7: "45-54", 8: "55-64", 9: "65+"
};
export const optionMap11 = new Map(Object.entries(options11));

export const options12 = {
    1: "No formal schooling", 2: "High school, no diploma", 3: "High school diploma",
    4: "Trade/technical/vocational training", 5: "Bachelor’s degree",
    6: "Master's degree", 7: "Doctorate degree",
    9: "Currently studying", 10: "Professional Qualification e.g. CIMA"
};
export const optionMap12 = new Map(Object.entries(options12));

export const options18 = { 1: 'More than 4 times', 2: 'Between 2-3 times', 3: 'Once', 4: 'Never' };
export const optionMap18 = new Map(Object.entries(options18));

export const options20 = { 1: 'Family', 2: 'Friends', 3: 'Business colleagues', 4: "Other" };
export const optionMap20 = new Map(Object.entries(options20));

export const options19 = { 1: 'Micro', 2: 'Small', 3: 'Medium', 4: 'Large' };
export const optionMap19 = new Map(Object.entries(options19));

export const options21 = {
    1: 'Less than a month', 2: 'At least 1 month but less than 3 months',
    3: 'At least 3 months but less than 6 months', 4: 'At least 6 months but less than 12 months',
    5: 'One year or more', 6: "Never - I don't expect to get repaid"
};
export const optionMap21 = new Map(Object.entries(options21));

export const options25 = {
    1: 'Every time', 2: 'At least 9 out of 10 times', 3: 'At least 7-8 out of 10 times',
    4: 'At least 5-6 out of 10 times', 5: 'Less than 5 out of 10 times'
};
export const optionMap25 = new Map(Object.entries(options25));

export const options36 = {
    1: 'Less than 5%', 2: '5% -10%', 3: '10% - 20%', 4: '20% - 30%', 5: '30% - 40%', 6: '40% - 50%',
    7: 'More than half of my income goes to pay off rent', 8: "Don't Know"
};
export const optionMap36 = new Map(Object.entries(options36));

