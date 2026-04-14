import pandas as pd
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent
SCR_DIR = BASE_DIR / "src"


MULTI_COUNTRY_DATA_FILE = BASE_DIR / "data-file" / "multi_country_data.csv"

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


with open(MULTI_COUNTRY_DATA_FILE, "r") as f:
    df = pd.read_csv(f)






df = df.rename(columns={
    "year":         "Year",
    "gdp":          "GDP",
    "gdp_growth":   "GDP_Growth_Raw",
    "inflation":    "Inflation",
    "unemployment": "Unemployment"
})



df = df.dropna(subset=["GDP", "Inflation", "Unemployment"])
df = df.drop(df[df["Year"] == 2024].index)
df = df.reset_index(drop=True)



def get_condition(row):
    if row["GDP_Growth"] < -2:
        return "Recession Signal"
    elif row["Inflation"] > 8 and row["GDP_Growth"] < 2:
        return "Stagflation Risk"
    elif row["GDP_Growth"] > 3 and row["Unemployment_Change"] < 0:
        return "Healthy Growth"
    elif row["Inflation"] > 8:
        return "Inflation Risk"
    else:
        return "Stable"

def detect_contradiction(row):
    if row["GDP_Growth"] > 3 and row["Unemployment_Change"] > 0:
        return "Jobless Growth"
    elif row["GDP_Growth"] < 0 and row["Unemployment_Change"] < 0:
        return "Data Contradiction / Lag Effect"
    else:
        return "No Contradiction"

def generate_insight(row):
    return f"{int(row['Year'])}: {row['Condition']} with {row['Contradiction']}"

def check_get_condition(row):
    condition = get_condition(row)
    contradictions = []
    
    if condition == "Healthy Growth" and row["Inflation"] > 8:
        contradictions.append("High inflation despite Healthy Growth label")
    
    if condition == "Stable" and row["GDP_Growth"] < 0:
        contradictions.append("Near-recession GDP despite Stable label")
    
    if condition == "Recession Signal" and row["Unemployment_Change"] < 0:
        contradictions.append("Unemployment falling despite Recession label")
    
    if condition == "Stagflation Risk" and row["GDP_Growth"] > 3:
        contradictions.append("Strong growth despite Stagflation label")
    
    if condition == "Inflation Risk" and row["GDP_Growth"] > 3:
        contradictions.append("Strong growth despite Inflation Risk label")

    if condition == "Inflation Risk" and row["Unemployment_Change"] < 0:
        contradictions.append("Falling unemployment despite Inflation Risk label")
    
    if condition == "Recession Signal" and row["Inflation"] < 2:
        contradictions.append("Low inflation despite Recession label")

    if condition == "Stable" and row["Inflation"] > 8:
        contradictions.append("High inflation despite Stable label")


    return contradictions if contradictions else None

def get_regime(row):
    if row["Economic_Score"] > 5:
        return "Expansion"
    elif row["Economic_Score"] < -10:
        return "Crisis"
    else:
        return "Transition"



def economic_score(row):

    score = 0
    score += row["GDP_Growth"] * 3
    score -= row["Unemployment_Change"] * 4
    score -= max(0, row["Inflation"] - 4) * 1
    return score


def back_testing(*years: int):
    a = df[df["Year"].isin(years)]
    for row in a.itertuples(index=False, name="Row"):  # type: ignore
        print(f"{row.Year} {row.Country}: {row.Condition} with {row.Contradiction} and Economic Score of {row.Economic_Score}")

def compare_countries(country1 =df["Country"].unique()[0], country2 =df["Country"].unique()[1], country3 =df["Country"].unique()[2], year: int=2020):
    c1 = df[(df["Country"] == country1) & (df["Year"] == year)].iloc[0]
    c2 = df[(df["Country"] == country2) & (df["Year"] == year)].iloc[0]
    c3 = df[(df["Country"] == country3) & (df["Year"] == year)].iloc[0]
    print(f"{country1} in {year}: {c1.Condition} with {c1.Contradiction} and Economic Score of {c1.Economic_Score}")
    print(f"{country2} in {year}: {c2.Condition} with {c2.Contradiction} and Economic Score of {c2.Economic_Score}")
    print(f"{country3} in {year}: {c3.Condition} with {c3.Contradiction} and Economic Score of {c3.Economic_Score}")
    print(f"Comparison: {country1} has {'higher' if c1.Economic_Score > c2.Economic_Score else 'lower'} economic score than {country2}")
    print(f"Comparison: {country1} has {'higher' if c1.Economic_Score > c3.Economic_Score else 'lower'} economic score than {country3}")

def regime_periods(country = None):

     
    df["Regime_change"] = df.groupby("Country")["Regime"].transform(
    lambda x: x != x.shift())

    df["Regime_ID"] = df.groupby("Country")["Regime_change"].transform(
    lambda x: x.cumsum())

    data = df.groupby(["Country", "Regime_ID"]).agg(
    Regime=("Regime", "first"),
    Start=("Year", "min"),
    End=("Year", "max"),
    Avg_Score=("Economic_Score", "mean")
).reset_index(drop=True)
    return data



df["GDP_Growth"]        = df.groupby("Country")["GDP"].pct_change().mul(100).round(2)
df["Unemployment_Change"] = df.groupby("Country")["Unemployment"].diff().round(2)
df["Condition"]         = df.apply(get_condition, axis=1)
df["Contradiction"]     = df.apply(detect_contradiction, axis=1)
df["Insight"]           = df.apply(generate_insight, axis=1)
df["Economic_Score"]    = df.apply(economic_score, axis=1).round(2)
df["GDP_Predicted"]     = df.groupby("Country")["GDP"].transform(lambda x: x.rolling(3).mean())
df["Condition_checker"] = df.apply(check_get_condition, axis=1)
df["Regime"]           = df.apply(get_regime, axis=1)



# print(df[df["Country"] == "India"][["Year", "GDP_Growth", "Unemployment_Change", "Inflation"]].to_string())
# print(df[df["Country"] == "India"][["Year",  "Regime"]].to_string())
# print(df.groupby([df["Country"] == "India"][["Year",  "Regime"]]))

# print(regime_periods().to_string())   

