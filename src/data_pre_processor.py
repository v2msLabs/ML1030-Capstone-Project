import pandas as pd

# categorises a column
def categorize(x, map, default_value=0):
    if (pd.isna(x)):
        return default_value
    else:
        return map[x]

