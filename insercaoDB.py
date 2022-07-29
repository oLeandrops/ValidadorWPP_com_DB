from funcoesBD import insert
import pandas as pd

df = pd.read_csv('FONE1.CSV')
insert(df['DDD'],df['TELEFONE'])