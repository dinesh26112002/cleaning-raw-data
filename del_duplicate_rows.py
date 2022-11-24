import pandas as pd

df = pd.read_csv('Covid Data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())