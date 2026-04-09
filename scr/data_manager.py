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

def economic_score(row):
    score = 0
    score += row["GDP_Growth"] * 2
    score -= row["Unemployment_Change"] * 5
    score -= max(0, row["Inflation"] - 4) * 2
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


condition_map = {
    "Recession Signal": "Severe recession detected due to GDP collapse",
    "Stagflation Risk": "High inflation with weak growth, stagflation risk",
    "Healthy Growth":   "Strong growth with improving jobs, healthy economy",
}


df["GDP_Growth"]        = df.groupby("Country")["GDP"].pct_change().mul(100).round(2)
df["Unemployment_Change"] = df.groupby("Country")["Unemployment"].diff().round(2)
df["Condition"]         = df.apply(get_condition, axis=1)
df["Contradiction"]     = df.apply(detect_contradiction, axis=1)
df["Insight"]           = df.apply(generate_insight, axis=1)
df["Economic_Score"]    = df.apply(economic_score, axis=1).round(2)
df["GDP_Predicted"]     = df.groupby("Country")["GDP"].transform(lambda x: x.rolling(3).mean())
df["Condition_Summary"] = df["Condition"].map(condition_map).fillna("Stable economy with no major risks")

