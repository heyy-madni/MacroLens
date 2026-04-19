import pandas as pd
from data_manager import BASE_DIR

gdp_growth_raw = BASE_DIR / "data-file" / "gdp growth.csv"
inflation_raw = BASE_DIR / "data-file" / "inflation.csv"
unemployment_raw = BASE_DIR / "data-file" / "Unemployment.csv"



def data_loader(file_path,skip_years=None,dropna=False):
    

    with open(file_path) as f:
        df=pd.read_csv(f,on_bad_lines='skip')

    df = df.rename(columns={
        'ï»¿"Country Name"': 'country',
        'Indicator Name': f'indicator({df["Indicator Name"].iloc[0]})' })
    
    df.drop(['Indicator Code','Country Code','2025','1960','Unnamed: 70'],axis=1,inplace=True)
    
    if skip_years !=None:
        df.drop(skip_years,axis=1,inplace=True)

    if dropna ==True:
        df.dropna(inplace=True)
        



    return df


gdp_growth_df = data_loader(gdp_growth_raw)
inflation_df =data_loader(inflation_raw)
unemployment = data_loader(unemployment_raw,'1962',True)



# print(gdp_growth_df.info(),\
#       inflation_df.info(),\
#        unemployment.info())



