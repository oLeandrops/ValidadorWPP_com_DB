from funcoesBD import insert
import pandas as pd
from datetime import date
df = pd.read_csv('FONE1.CSV')
hoje =date.today()
hoje = f'{hoje.day}-{hoje.month}-{hoje.year}'
for i  in df.index:
    insert(int(df['DDD'][i]), str(df['TELEFONE'][i]),data=hoje, job ='jobthais')