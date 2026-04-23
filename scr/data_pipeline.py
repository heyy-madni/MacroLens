import pandas as pd
from pathlib import Path

def raw_files():
    BASE_DIR = Path(__file__).resolve().parent.parent
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


        
    df = df.melt(id_vars=['country'],var_name='years',value_name='value')
    df['years'] = df['years'].astype(int)


    return df


def merge_data(gdp_growth_df,inflation_df,unemployment):
    df=pd.merge(gdp_growth_df,inflation_df,on=['country', 'years'],how='outer')
    df=pd.merge(df,unemployment,on=['country', 'years'],how='outer')
    
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

df_1=merge_data(gdp_growth_df,inflation_df,unemployment)


if __name__ == '__main__':
    print(df_1.info())
    print(df_1.columns.tolist())





