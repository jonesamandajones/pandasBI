import pandas as pd

df = pd.read_csv('RAINHAS.csv')

df['NOME'] = df['NOME'].str.strip()

df['ID'] = pd.to_numeric(df['ID'])

df['DATA_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'])

df['SEXO'] = df['SEXO'].replace(['F'], 'FEMININO')

df['SEXO'] = df['SEXO'].replace(['M'], 'MASCULINO')

print(df)