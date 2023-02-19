import pandas as pd

df = pd.read_csv('RAINHAS.csv')

df['NOME'] = df['NOME'].str.strip()

df['ID'] = pd.to_numeric(df['ID'])

df['DATA_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'])

print(df)