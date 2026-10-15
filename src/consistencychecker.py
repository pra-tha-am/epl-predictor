import pandas as pd
df = pd.read_csv(r"C:\Users\Pratham Rai\OneDrive\Desktop\epl-predictor\data\processed\matches.csv")
failed_rows_H = df.loc[(df['FTHG'] > df['FTAG']) & (df['FTR'] != 'H')]
failed_rows_A = df.loc[(df['FTHG'] < df['FTAG']) & (df['FTR'] != 'A')]
failed_rows_D = df.loc[(df['FTHG'] == df['FTAG']) & (df['FTR'] != 'D')]
print(failed_rows_H)
print(failed_rows_A)
print(failed_rows_D)