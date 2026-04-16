#imports
import pandas as pd
from pathlib import Path
from functions import \
        get_condition,\
        check_get_condition,\
        generate_insight,\
        get_regime,\
        economic_score,\
        detect_contradiction

#dicetry
BASE_DIR = Path(__file__).resolve().parent.parent
SCR_DIR = BASE_DIR / "src"
MULTI_COUNTRY_DATA_FILE = BASE_DIR / "data-file" / "multi_country_data.csv"


# set pandas display for me
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# Load the dataset
with open(MULTI_COUNTRY_DATA_FILE, 'r') as f:
    df = pd.read_csv(f)






#rename columns 
df = df.rename(columns={
    "year":         "Year",
    "gdp":          "GDP",
    "gdp_growth":   "GDP_Growth_Raw",
    "inflation":    "Inflation",
    "unemployment": "Unemployment"
})


# clean data
df = df.dropna(subset=["GDP", "Inflation", "Unemployment"])
df = df.drop(df[df["Year"] == 2024].index)
df = df.reset_index(drop=True)



# new columns
df["GDP_Growth"]        = df.groupby("Country")["GDP"].pct_change().mul(100).round(2)
df["Unemployment_Change"] = df.groupby("Country")["Unemployment"].diff().round(2)
df["Condition"]         = df.apply(get_condition, axis=1)
df["Contradiction"]     = df.apply(detect_contradiction, axis=1)
df["Insight"]           = df.apply(generate_insight, axis=1)
df["Economic_Score"]    = df.apply(economic_score, axis=1).round(2)
df["GDP_Predicted"]     = df.groupby("Country")["GDP"].transform(lambda x: x.rolling(3).mean())
df["Condition_checker"] = df.apply(check_get_condition, axis=1)
df["Regime"]           = df.apply(get_regime, axis=1)


#test

# print(df[df["Country"] == "India"][["Year", "GDP_Growth", "Unemployment_Change", "Inflation"]].to_string())
# print(df[df["Country"] == "India"][["Year",  "Regime"]].to_string())
# print(df.groupby([df["Country"] == "India"][["Year",  "Regime"]]))

# print(regime_periods().to_string())   

