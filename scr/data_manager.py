#imports
import pandas as pd
from pathlib import Path
from data_pipeline import df_1
from functions import \
        get_condition,\
        check_get_condition,\
        generate_insight,\
        get_regime,\
        economic_score,\
        detect_contradiction



#dicetry
BASE_DIR = Path(__file__).resolve().parent.parent
MULTI_COUNTRY_DATA_FILE = BASE_DIR / "data-file" / "multi_country_data.csv"
SCR_DIR = BASE_DIR / "src"











# set pandas display for me
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# Load the dataset
with open(MULTI_COUNTRY_DATA_FILE, 'r') as f:
    df = pd.read_csv(f, on_bad_lines='skip')







#rename columns 
df = df.rename(columns={
    "year":         "Year",
    "gdp_growth":   "gdp growth",
    "inflation":    "Inflation",
    "unemployment": "Unemployment"
})

df_1=df_1.rename(columns={
    "years": "Year",
    "gdp growth": "gdp growth",
    "inflation": "Inflation",
    "unemployment": "Unemployment"
})

# clean data
# print(df.columns)

df = df.dropna(subset=["GDP_Growth", "Inflation", "Unemployment"])
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




  

