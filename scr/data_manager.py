#imports
import pandas as pd
from pathlib import Path
from data_pipeline import df
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

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


df=df.rename(columns={
    "years": "Year",
    "gdp growth": "gdp growth",
    "inflation": "Inflation",
    "unemployment": "Unemployment"
})


df = df.dropna(subset=["gdp growth", "Inflation", "Unemployment"])
df = df.reset_index(drop=True)








df["Unemployment_Change"] = df.groupby("country")["Unemployment"].diff().round(2)
df["Condition"]         = df.apply(get_condition, axis=1)
df["Contradiction"]     = df.apply(detect_contradiction, axis=1)
df["Insight"]           = df.apply(generate_insight, axis=1)
df["Economic_Score"]    = df.apply(economic_score, axis=1).round(2)
df["GDP_Predicted"]     = df.groupby("country")["gdp growth"].transform(lambda x: x.rolling(3).mean())
df["Condition_checker"] = df.apply(check_get_condition, axis=1)
df["Regime"]           = df.apply(get_regime, axis=1)


print(df.head())




  

