import pandas as pd
import os


def read_data(dir_path: str):
    
    csv_files = os.listdir(dir_path)

    for file in csv_files:
        
        filename = file.replace('.csv', '_df')
        filepath = os.path.join(dir_path, file)
        globals()[filename] = pd.read_csv(filepath, sep=';', encoding='latin1', dtype=str)


def filter_data(df: pd.DataFrame, year_col: str, month_col: str, from_date: str, to_date: str, limit: int = None) -> pd.DataFrame:

    df = df.copy()
    df['DATE'] = pd.to_datetime(df[year_col] + '/' + df[month_col] + '/01')
    df = df[(df['DATE'] >= from_date) & (df['DATE'] < to_date)]
    df.drop(columns='DATE', inplace=True)
    
    if limit is not None:
        df = df.head(limit)
    
    return df

def get_sh4_from_ncm(df: pd.DataFrame, ncm_col: str, ) -> pd.DataFrame:

    df = df.copy()
    df['SH4'] = df[ncm_col].str.slice(0, 4)

    return df

def join_data(df1: pd.DataFrame, df2: pd.DataFrame, how: str, on: str) -> pd.DataFrame:

    df = pd.merge(df1, df2, how=how, on=on, validate='m:m')

    return df

def save_to_csv(df: pd.DataFrame, dir_path: str, filename: str, sort_by=None):

    try:

        if sort_by is not None:
            df = df.sort_values(by=sort_by)

        full_path = os.path.join(dir_path, filename)

        df.to_csv(full_path, index=False)
        print(f'File {filename} created successfully in {dir_path}.')
    except Exception as err:
        print(f'Error creating CSV file {filename} in {dir_path}:', err)


# Reading data
read_data('./rawData')

# Setting a limit
limit = 50000

# Filtering data
EXP_2023_MUN_df = filter_data(EXP_2023_MUN_df, 'CO_ANO', 'CO_MES', '2023-01-01', '2023-04-01', limit)
EXP_2023_df = filter_data(EXP_2023_df, 'CO_ANO', 'CO_MES', '2023-01-01', '2023-04-01', limit)

# Getting the SH4 column
EXP_2023_df = get_sh4_from_ncm(EXP_2023_df, 'CO_NCM')

# Merging the dataframes
merged_df = join_data(EXP_2023_MUN_df, EXP_2023_df, how='inner', on='SH4')

# Processing data
ncm_per_mun_count = merged_df.groupby(['CO_MUN', 'CO_NCM']).size().reset_index(name='Count')
total_per_mun = merged_df.groupby('CO_MUN').size().reset_index(name='Total')
percentage_df = pd.merge(ncm_per_mun_count, total_per_mun, on='CO_MUN')
percentage_df['Percentage'] = (percentage_df['Count'] / percentage_df['Total']) * 100


percentage_df.rename(columns={'CO_NCM': 'NCM', 'CO_MUN': 'Município'}, inplace=True)


percentage_df = pd.merge(percentage_df, NCM_df[['CO_NCM', 'NO_NCM_POR']], left_on='NCM', right_on='CO_NCM', how='left')
percentage_df = pd.merge(percentage_df, UF_MUN_df[['CO_MUN_GEO', 'NO_MUN']], left_on='Município', right_on='CO_MUN_GEO', how='left')


percentage_df = percentage_df[['CO_NCM', 'NO_NCM_POR', 'NO_MUN', 'Percentage']]
percentage_df.rename(columns={'CO_NCM': 'NCM','NO_NCM_POR': 'Tipo do Material', 'NO_MUN': 'Nome do Município', 'Percentage': 'Percentual'}, inplace=True)

# Saving the data as csv
save_to_csv(percentage_df, './finalDataSet', 'final_data.csv', sort_by='NCM')
