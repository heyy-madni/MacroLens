 #data_pipeline.py


#imports
import pandas as pd
from pathlib import Path
import functions as f

#dicetry
BASE_DIR = Path(__file__).resolve().parent.parent
SCR_DIR = BASE_DIR / "src"
SAVE_REPORT_DIR = BASE_DIR / "reports"

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def raw_files():
    
    return {
        "GDP_GROWTH": BASE_DIR / "data-file" / "gdp growth.csv",
        "INFLATION": BASE_DIR / "data-file" / "inflation.csv",
        "UNEMPLOYMENT": BASE_DIR / "data-file" / "Unemployment.csv",
        "INCOME_PER_CAPITA": BASE_DIR / "data-file" / "income per capita.csv"
    }




def data_loader(file_path):
    

    with open(file_path) as f:
        df=pd.read_csv(f,on_bad_lines='skip')

    df = df.rename(columns={
        'ï»¿"Country Name"': 'country'})
    
    df.drop(['Indicator Code',\
             'Country Code',\
            'Indicator Name',\
            '2025','1960',\
            'Unnamed: 70'],axis=1,inplace=True)


        
    df = df.melt(id_vars=['country'],var_name='Years',value_name='value')


    return df


def merge_data(gdp_growth_df,inflation_df,unemployment,income_per_capita_df=None):
    df=pd.merge(gdp_growth_df,inflation_df,on=['country', 'Years'],how='outer')
    df=pd.merge(df,unemployment,on=['country', 'Years'],how='outer')
    df=pd.merge(df,income_per_capita_df,on=['country', 'Years'],how='outer') if income_per_capita_df is not None else df
    df.rename(columns={'value_x':'gdp growth',
                   'value_y':'inflation',
                   'value':'unemployment'
                   },inplace=True)
    


    return df


def country_data(country_name,df):  

    
    country_df = df[df['country'] == country_name]
    return country_df




gdp_growth_df = data_loader(raw_files()["GDP_GROWTH"])
inflation_df =data_loader(raw_files()["INFLATION"])
unemployment = data_loader(raw_files()["UNEMPLOYMENT"])
income_per_capita_df = data_loader(raw_files()["INCOME_PER_CAPITA"])



df = merge_data(gdp_growth_df,inflation_df,unemployment)
df = pd.merge(df, income_per_capita_df, on=['country', 'Years'], how='outer')
df['Years'] = df['Years'].astype(int)
df['value'] = pd.to_numeric(df['value'], errors='coerce')


df=df.rename(columns={
    "Years": "Year",
    "gdp growth": "gdp growth",
    "inflation": "Inflation",
    "unemployment": "Unemployment",
    "value": "Income_Per_Capita"
})

df = df.dropna(subset=["gdp growth", "Inflation", "Unemployment", "Income_Per_Capita"])
df = df.reset_index(drop=True)


df["Unemployment_Change"] = df.groupby("country")["Unemployment"].diff().round(2)
df["Condition"]         = df.apply(f.get_condition, axis=1)
df["Contradiction"]     = df.apply(f.detect_contradiction, axis=1)
df["Insight"]           = df.apply(f.generate_insight, axis=1)
df["Economic_Score"]    = df.apply(f.economic_score, axis=1).round(2)
df["GDP_Predicted"]     = df.groupby("country")["gdp growth"].transform(lambda x: x.rolling(3).mean())
df["Condition_checker"] = df.apply(f.check_get_condition, axis=1)
df["Regime"]           = df.apply(f.get_regime, axis=1)


# file = str(SAVE_REPORT_DIR) + 'report.csv'
# df.to_csv(file, index=False)

if __name__ == '__main__':
    print(df.head())

    # print(df['Income_Per_Capita'].describe())
