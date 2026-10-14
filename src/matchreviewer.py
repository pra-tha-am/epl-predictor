import pandas as pd 
columns = ['Date', 'HomeTeam','AwayTeam','FTHG','FTAG','FTR']
df = pd.read_csv(r"C:\Users\Pratham Rai\OneDrive\Desktop\epl-predictor\data\processed\matches.csv", usecols = columns)
na_rows = df[df.isna().any(axis = 1)]
print(na_rows)
print(len(df), len(na_rows))