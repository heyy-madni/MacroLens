import pandas as pd
from data_manager import BASE_DIR

gdp_growth = BASE_DIR / "data-file" / "gdp growth.csv"



with open(gdp_growth) as f:
    df=pd.read_csv(f,on_bad_lines='skip')

df = df.rename(columns={
    'ï»¿"Country Name"': 'country',
    'Indicator Name': 'indicator'
})



df.drop(['Indicator Code','Country Code'],axis=1,inplace=True)
print(df.info())




