from funcoesBD import insert
import pandas as pd

df = pd.read_csv('FONE1.CSV')
for i  in df.index:
    insert(int(df['DDD'][i]), str(df['TELEFONE'][i]))