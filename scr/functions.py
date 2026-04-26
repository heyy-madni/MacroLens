####################### data functions ########################
# 


def get_condition(row):
    if row["gdp growth"] < -2:
        return "Recession Signal"
    elif row["Inflation"] > 8 and row["gdp growth"] < 2:
        return "Stagflation Risk"
    elif row["gdp growth"] > 3 and row["Unemployment"] < 0:
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
        contradictions.append("High inflation despite Healthy Growth label")
    
    if condition == "Stable" and row["gdp growth"] < 0:
        contradictions.append("Near-recession GDP despite Stable label")
    
    if condition == "Recession Signal" and row["Unemployment"] < 0:
        contradictions.append("Unemployment falling despite Recession label")
    
    if condition == "Stagflation Risk" and row["gdp growth"] > 3:
        contradictions.append("Strong growth despite Stagflation label")
    
    if condition == "Inflation Risk" and row["gdp growth"] > 3:
        contradictions.append("Strong growth despite Inflation Risk label")

    if condition == "Inflation Risk" and row["Unemployment"] < 0:
        contradictions.append("Falling unemployment despite Inflation Risk label")
    
    if condition == "Recession Signal" and row["Inflation"] < 2:
        contradictions.append("Low inflation despite Recession label")

    if condition == "Stable" and row["Inflation"] > 8:
        contradictions.append("High inflation despite Stable label")


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




def compare_countries(df, country1=None, country2=None, country3=None, Years: int = 2020):
    
    countries = df["country"].unique()
    if country1 is None: country1 = countries[0]
    if country2 is None: country2 = countries[1]
    if country3 is None: country3 = countries[2]

    c1_df = df[(df["country"] == country1) & (df["Years"] == Years)]
    c2_df = df[(df["country"] == country2) & (df["Years"] == Years)]
    c3_df = df[(df["country"] == country3) & (df["Years"] == Years)]

    if c1_df.empty or c2_df.empty or c3_df.empty:
        return [f"Data not found for one or more countries in {Years}."]

    c1, c2, c3 = c1_df.iloc[0], c2_df.iloc[0], c3_df.iloc[0]


    insight =[]

    insight.append(f"{country1} in {Years}: {c1.Condition} with {c1.Contradiction} and Economic Score of {c1.Economic_Score}\n")
    insight.append(f"{country2} in {Years}: {c2.Condition} with {c2.Contradiction} and Economic Score of {c2.Economic_Score}\n")
    insight.append(f"{country3} in {Years}: {c3.Condition} with {c3.Contradiction} and Economic Score of {c3.Economic_Score}\n")

    insight.append(f"Comparison: {country1} has {'higher' if c1.Economic_Score > c2.Economic_Score else 'lower'} economic score than {country2}\n")
    insight.append(f"Comparison: {country1} has {'higher' if c1.Economic_Score > c3.Economic_Score else 'lower'} economic score than {country3}\n")

    insight.append(f"Comparison: {country1} has {'higher' if c1.inflation > c2.inflation else 'lower'} Inflation than {country2}\n")
    insight.append(f"Comparison: {country1} has {'higher' if c1.inflation > c3.inflation else 'lower'} Inflation than {country3}\n")

    insight.append(f"Comparison: {country1} has {'higher' if c1.unemployment > c2.unemployment else 'lower'} Unemployment than {country2}\n")
    insight.append(f"Comparison: {country1} has {'higher' if c1.unemployment > c3.unemployment else 'lower'} Unemployment than {country3}\n")

    return insight


def regime_periods(df, country="India"):
    df = df[df["country"] == country].copy()


    df["Regime_change"] = df["Regime"] != df["Regime"].shift()
    df["Regime_ID"] = df["Regime_change"].cumsum()
    

    data = df.groupby("Regime_ID").agg(
        Country=("country", "first"),
        Regime=("Regime", "first"),
        Start=("Years", "min"),
        End=("Years", "max"),
        Avg_Score=("Economic_Score", "mean")
    ).reset_index(drop=True)

    return data


def back_testing(df,*Years: int, country='India'):
    

    filtered_df = df[df["Years"].isin(Years)]
    if country:
        filtered_df = filtered_df[filtered_df["country"] == country]
    a = filtered_df[["Years", "country", "Condition", "Contradiction", "Economic_Score"]]
    for row in a.itertuples(index=False, name="Row"):
        print(f"{row.Years  } {row.country}: {row.Condition} with {row.Contradiction} and Economic Score of {row.Economic_Score}")




####################### menu functions ########################


def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def choice_1(df):
    clear_console()
    country = input("Enter the country for overview (default: India): ")
    if country == "india"or country == "India" or not country:
        country = "India"
    elif country == "usa" or country == "US"or country == "USA" or country == "united states":
        country = "United States"
    elif country == "china"or country == "China":
        country = "China"
          
    if not country:
        print(" entered country not found. Defaulting to India.")
              
    clear_console()

    from report_genrator import  over_view_of_economy_chart
    

    over_view_of_economy_chart(df=df,choice=country)
    input("Press Enter to return to the menu...")
    clear_console()



def choice_2(df, country):
    
    from report_genrator import generate_report
    clear_console()
    generate_report(df, country=country)
    input("Press Enter to return to the menu...")
    clear_console()

    #  
    # print(df.columns)
    # choice_2()

def choice_3(df):
    clear_console()
    print("Back Testing Options:")
    print("1. Custom Years Back Testing")
    print("2. Regime Periods")
    print("3. Condition Checker")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        Years = int(input("Enter the Years for back testing: "))
        back_testing(df, Years)
    
    elif choice == "2":
        country = input("Enter the country for regime periods (default: India): ") or "India"
        if country == "india"or country == "India" or not country:
            country = "India"
        elif country == "usa" or country == "US"or country == "USA" or country == "united states":
            country = "USA"
        elif country == "china"or country == "China":
            country = "China"
        print(regime_periods(df, country))
    
    elif choice == "3":
        choice_3_3(df, input("Enter the country for condition checker (default: India): ") or "India")


def choice_3_3(df, country):
        
        clear_console()
        
        filtered_df = df[df["country"] == country]
        print("Condition Checker Results:")


        result = filtered_df[["Years", "country", "Condition", "Condition_checker"]]
        col_widths = {col: max(result[col].astype(str).fillna("None").map(len).max(), len(col)) for col in result.columns}

        header = "  ".join(col.ljust(col_widths[col]) for col in result.columns)
        separator = "  ".join("-" * col_widths[col] for col in result.columns)
        print(header)
        print(separator)
        for _, row in result.iterrows():
            print("  ".join(str(row[col]).ljust(col_widths[col]) for col in result.columns))
        else:
            print("Invalid choice. Returning to menu.")
        input("Press Enter to return to the menu...")
        clear_console()



def choice_5(df):
    choice = input("""
 1 list oof countries supported
 2 list of Years supported
 3 functions used in the project and their purpose
 4 data sources and their description
 5 back to menu
""")
    
    if choice == "5":
        return
    

    if choice == "1":
        
        print("Countries supported:")
        print(df["country"].unique())

    elif choice == "2":
        
        print("Years supported:")
        print(df["Years"].unique())

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
        print("Data source is from World Bank")
        print("1. GDP Growth: Annual percentage growth rate of GDP at market prices based on constant local currency.")
        print("2. Inflation: Annual percentage change in the cost to the average consumer of acquiring a basket of goods and services that may be fixed or changed at specified intervals, such as Yearsly.")
        print("3. Unemployment: Percentage of the total labor force that is unemployed but actively seeking employment and willing to work.")
    else:
        print("Invalid choice. Returning to menu.")



















