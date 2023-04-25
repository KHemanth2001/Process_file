import pandas as pd

def process_file():
    df=pd.read_excel('D:\process_data\\venv\SeriesReport-20230425013159_b244d5.xlsx')
    df=df.loc[:248]
    melted_df = df.melt(id_vars=['Year'], value_vars=df.loc['Jan':'Dec'], var_name='Month',
                        value_name='Unemployment Level in thousand')
    melted_df.insert(2, "Date",melted_df["Month"]+' '+melted_df["Year"].astype(str), True)
    melted_df.to_excel('Unemployment_Level.xlsx',index=False)


process_file()
