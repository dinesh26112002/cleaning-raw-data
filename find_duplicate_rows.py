import pandas as pd

df = pd.read_csv('Covid Data.csv')

print(df.duplicated())
