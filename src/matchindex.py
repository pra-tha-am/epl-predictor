import pandas as pd
columns = ['Date', 'HomeTeam','AwayTeam','FTHG','FTAG','FTR']
df = pd.read_csv("data/processed/matches.csv")
failed_rows_H = df.loc[(df['FTHG'] > df['FTAG']) & (df['FTR'] != 'H')]
failed_rows_A = df.loc[(df['FTHG'] < df['FTAG']) & (df['FTR'] != 'A')]
failed_rows_D = df.loc[(df['FTHG'] == df['FTAG']) & (df['FTR'] != 'D')]
print(failed_rows_H)
print(failed_rows_A)
print(failed_rows_D)

df = pd.read_csv("data/processed/matches.csv", usecols = columns)
na_rows = df[df.isna().any(axis = 1)]
print(na_rows)
print(len(df), len(na_rows))

matches = pd.read_csv("data/processed/matches.csv", parse_dates=["Date"])
matches["match_id"] = matches.index
matches.to_csv("data/processed/matches.csv", index=False)