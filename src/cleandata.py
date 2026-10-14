import pandas as pd
from pathlib import Path

#List of Columns we actually need to train our data

COLUMNS = ["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR",
           "HS", "AS", "HST", "AST", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR",
           "B365H", "B365D", "B365A", "AvgH", "AvgD", "AvgA",
           "B365CH", "B365CD", "B365CA", "AvgCH", "AvgCD", "AvgCA"]

def clean_file(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["HomeTeam", "AwayTeam"])

    #We use this loop to drop the useless columns

    keep = []
    for c in COLUMNS:
        if c in df.columns:
            keep.append(c)
    df = df[keep].copy()

    #We need our values in datetime so we can sort according to recency

    text = df["Date"]
    four_digit_year = pd.to_datetime(text, format="%d/%m/%Y", errors="coerce")
    two_digit_year = pd.to_datetime(text, format="%d/%m/%y", errors="coerce")
    df["Date"] = four_digit_year.fillna(two_digit_year)

    return df

#Takes all the raw CSV files to convert them into one big CSV

frames = []
for f in sorted(Path("data/raw").glob("E[0-9][0-9].csv")):
    yy = int(f.stem[1:])
    df = clean_file(f)
    df["Season"] = f"20{yy:02d}/{yy + 1:02d}"
    frames.append(df)

matches = pd.concat(frames, ignore_index=True)
matches = matches.sort_values(["Date", "HomeTeam"]).reset_index(drop=True)

print(matches.groupby("Season").size())

Path("data/processed").mkdir(parents=True, exist_ok=True)
matches.to_csv("data/processed/matches.csv", index=False)