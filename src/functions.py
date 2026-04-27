# functions.py

import os
from report_genrator import over_view_of_economy_chart, generate_report


####################### helpers ########################

def normalize_country(name: str) -> str:
    name = name.strip().lower()
    if name in ("india", ""):
        return "India"
    elif name in ("usa", "us", "united states", "america"):
        return "United States"
    elif name == "china":
        return "China"
    return name.title()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


####################### data functions ########################

def get_condition(row):
    if row["gdp growth"] < -2:
        return "Recession Signal"
    elif row["Inflation"] > 8 and row["gdp growth"] < 2:
        return "Stagflation Risk"
    elif row["gdp growth"] > 3 and row["Unemployment"] < 5:
        return "Healthy Growth"
    elif row["Inflation"] > 8:
        return "Inflation Risk"
    else:
        return "Stable"

def generate_insight(row):
    return f"{int(row['Year'])}: {row['Condition']} with {row['Contradiction']}"

def check_get_condition(row):
    condition = get_condition(row)
    contradictions = []

    if condition == "Healthy Growth" and row["Inflation"] > 8:
        contradictions.append("High Inflation despite Healthy Growth label")
    if condition == "Stable" and row["gdp growth"] < 0:
        contradictions.append("Near-recession GDP despite Stable label")
    if condition == "Recession Signal" and row["Unemployment"] < 0:
        contradictions.append("Unemployment falling despite Recession label")
    if condition == "Stagflation Risk" and row["gdp growth"] > 3:
        contradictions.append("Strong growth despite Stagflation label")
    if condition == "Inflation Risk" and row["gdp growth"] > 3:
        contradictions.append("Strong growth despite Inflation Risk label")
    if condition == "Inflation Risk" and row["Unemployment"] < 0:
        contradictions.append("Falling Unemployment despite Inflation Risk label")
    if condition == "Recession Signal" and row["Inflation"] < 2:
        contradictions.append("Low Inflation despite Recession label")
    if condition == "Stable" and row["Inflation"] > 8:
        contradictions.append("High Inflation despite Stable label")

    return contradictions if contradictions else None

def detect_contradiction(row):
    if row["gdp growth"] > 3 and row["Unemployment"] > 0:
        return "Jobless Growth"
    elif row["gdp growth"] < 0 and row["Unemployment"] < 0:
        return "Data Contradiction / Lag Effect"
    else:
        return "No Contradiction"

def get_regime(row):
    if row["Economic_Score"] > 5:
        return "Expansion"
    elif row["Economic_Score"] < -10:
        return "Crisis"
    else:
        return "Transition"

def economic_score(row):
    score = 0
    score += row["gdp growth"] * 3
    score -= row["Unemployment"] * 4
    score -= max(0, row["Inflation"] - 4) * 1
    return score

def compare_countries(df, country1=None, country2=None, country3=None, year: int = 2020):
    countries = df["country"].unique()
    if country1 is None: country1 = countries[0]
    if country2 is None: country2 = countries[1]
    if country3 is None: country3 = countries[2]

    c1_df = df[(df["country"] == country1) & (df["Year"] == year)]
    c2_df = df[(df["country"] == country2) & (df["Year"] == year)]
    c3_df = df[(df["country"] == country3) & (df["Year"] == year)]

    if c1_df.empty or c2_df.empty or c3_df.empty:
        return [f"Data not found for one or more countries in {year}."]

    c1, c2, c3 = c1_df.iloc[0], c2_df.iloc[0], c3_df.iloc[0]

    insights = []
    for label, c in [(country1, c1), (country2, c2), (country3, c3)]:
        insights.append(f"{label} in {year}: {c.Condition} with {c.Contradiction} and Economic Score of {c.Economic_Score}\n")

    pairs = [(country1, c1, country2, c2), (country1, c1, country3, c3)]
    for n1, d1, n2, d2 in pairs:
        insights.append(f"Comparison: {n1} has {'higher' if d1.Economic_Score > d2.Economic_Score else 'lower'} economic score than {n2}\n")
        insights.append(f"Comparison: {n1} has {'higher' if d1.Inflation > d2.Inflation else 'lower'} Inflation than {n2}\n")
        insights.append(f"Comparison: {n1} has {'higher' if d1.Unemployment > d2.Unemployment else 'lower'} Unemployment than {n2}\n")

    return insights

def regime_periods(df, country="India"):
    df = df[df["country"] == country].copy()
    df["Regime_change"] = df["Regime"] != df["Regime"].shift()
    df["Regime_ID"] = df["Regime_change"].cumsum()

    return df.groupby("Regime_ID").agg(
        Country=("country", "first"),
        Regime=("Regime", "first"),
        Start=("Year", "min"),
        End=("Year", "max"),
        Avg_Score=("Economic_Score", "mean")
    ).reset_index(drop=True)

def back_testing(df, year: int, country="India"):
    filtered_df = df[(df["Year"] == year) & (df["country"] == country)]
    for row in filtered_df[["Year", "country", "Condition", "Contradiction", "Economic_Score"]].itertuples(index=False):
        print(f"{row.Year} {row.country}: {row.Condition} with {row.Contradiction} and Economic Score of {row.Economic_Score}")


####################### menu functions ########################
    # fw3cf

def choice_1(df):
    clear_console()

    country = normalize_country(input("Enter the country for overview (default: India): "))
    
    clear_console()
    
    over_view_of_economy_chart(df=df, choice=country)
    input("Press Enter to return to the menu...")
    
    clear_console()

def choice_2(df, country):
    clear_console()
    generate_report(df, country=country)
    input("Press Enter to return to the menu...")
    clear_console()

def choice_3(df):
    clear_console()
    print("Back Testing Options:")
    print("1. Custom Year Back Testing")
    print("2. Regime Periods")
    print("3. Condition Checker")
    choice = input("Enter your choice: ")

    if choice == "1":
        year = int(input("Enter the Year for back testing: "))
        back_testing(df, year)
    elif choice == "2":
        country = normalize_country(input("Enter the country (default: India): ") or "India")
        print(regime_periods(df, country))
    elif choice == "3":
        country = normalize_country(input("Enter the country (default: India): ") or "India")
        choice_3_3(df, country)

def choice_3_3(df, country):
    clear_console()
    filtered_df = df[df["country"] == country]
    print("Condition Checker Results:")

    result = filtered_df[["Year", "country", "Condition", "Condition_checker"]]
    if result.empty:
        print("No data found for this country.")
        input("Press Enter to return to the menu...")
        return

    col_widths = {col: max(result[col].astype(str).fillna("None").map(len).max(), len(col)) for col in result.columns}
    header = "  ".join(col.ljust(col_widths[col]) for col in result.columns)
    separator = "  ".join("-" * col_widths[col] for col in result.columns)
    print(header)
    print(separator)
    for _, row in result.iterrows():
        print("  ".join(str(row[col]).ljust(col_widths[col]) for col in result.columns))

    input("Press Enter to return to the menu...")
    clear_console()

def choice_4(df):
    clear_console()
    country1 = normalize_country(input("Enter the first country (default: India): ") or "India")
    country2 = normalize_country(input("Enter the second country (default: USA): ") or "United States")
    country3 = normalize_country(input("Enter the third country (default: China): ") or "China")
    year_input = input("Enter the year for comparison (default: 2020): ")
    year = int(year_input) if year_input else 2020

    clear_console()
    for line in compare_countries(df, country1, country2, country3, year):
        print(line)
    input("Press Enter to return to the menu...")
    clear_console()

def choice_5(df):
    choice = input("""
 1. List of countries supported
 2. List of years supported
 3. Functions used in the project and their purpose
 4. Data sources and their description
 5. Back to menu
""")

    if choice == "5":
        return
    elif choice == "1":
        print("Countries supported:")
        print(df["country"].unique())
    elif choice == "2":
        print("Years supported:")
        print(df["Year"].unique())
    elif choice == "3":
        print("Functions used in the project and their purpose:")
        print("- get_condition: Determines economic condition based on indicators")
        print("- generate_insight: Creates insights from conditions and contradictions")
        print("- check_get_condition: Checks for contradictions in assigned conditions")
        print("- detect_contradiction: Identifies contradictions in economic data")
        print("- get_regime: Classifies economic regime based on score")
        print("- economic_score: Calculates an overall economic score")
        print("- compare_countries: Compares economic indicators between countries")
        print("- regime_periods: Identifies periods of different economic regimes")
        print("- back_testing: Tests conditions against historical data")
    elif choice == "4":
        print("Data sources and their description:")
        print("Source: World Bank")
        print("1. GDP Growth: Annual % growth rate of GDP at constant local currency prices.")
        print("2. Inflation: Annual % change in consumer price index.")
        print("3. Unemployment: % of labor force unemployed but actively seeking work.")
    else:
        print("Invalid choice. Returning to menu.")



















