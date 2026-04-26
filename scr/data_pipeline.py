import pandas as pd
from pathlib import Path
import functions
#dicetry
BASE_DIR = Path(__file__).resolve().parent.parent
SCR_DIR = BASE_DIR / "src"


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def raw_files():
    
    return {
        "GDP_GROWTH": BASE_DIR / "data-file" / "gdp growth.csv",
        "INFLATION": BASE_DIR / "data-file" / "inflation.csv",
        "UNEMPLOYMENT": BASE_DIR / "data-file" / "Unemployment.csv"
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
    df['Years'] = df['Years'].astype(int)


    return df


def merge_data(gdp_growth_df,inflation_df,unemployment):
    df=pd.merge(gdp_growth_df,inflation_df,on=['country', 'Years'],how='outer')
    df=pd.merge(df,unemployment,on=['country', 'Years'],how='outer')
    
    df.rename(columns={'value_x':'gdp growth',
                   'value_y':'inflation',
                   'value':'unemployment'},inplace=True)
    return df


def country_data(country_name,df):  

    
    country_df = df[df['country'] == country_name]
    return country_df



gdp_growth_df = data_loader(raw_files()["GDP_GROWTH"])
inflation_df =data_loader(raw_files()["INFLATION"])
unemployment = data_loader(raw_files()["UNEMPLOYMENT"])

df=merge_data(gdp_growth_df,inflation_df,unemployment)

df=df.rename(columns={
    "Years": "Year",
    "gdp growth": "gdp growth",
    "inflation": "Inflation",
    "unemployment": "Unemployment"
})

df = df.dropna(subset=["gdp growth", "Inflation", "Unemployment"])
df = df.reset_index(drop=True)


df["Unemployment_Change"] = df.groupby("country")["Unemployment"].diff().round(2)
df["Condition"]         = df.apply(functions.get_condition, axis=1)
df["Contradiction"]     = df.apply(functions.detect_contradiction, axis=1)
df["Insight"]           = df.apply(functions.generate_insight, axis=1)
df["Economic_Score"]    = df.apply(functions.economic_score, axis=1).round(2)
df["GDP_Predicted"]     = df.groupby("country")["gdp growth"].transform(lambda x: x.rolling(3).mean())
df["Condition_checker"] = df.apply(functions.check_get_condition, axis=1)
df["Regime"]           = df.apply(functions.get_regime, axis=1)

if __name__ == '__main__':
    print(df.info())
    print(df.head(2))
