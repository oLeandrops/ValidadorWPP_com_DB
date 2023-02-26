from funcoesBD import insert
import pandas as pd
from datetime import date
df = pd.read_csv('JOB71906_OFICIODEREGISTRO__VALIDAR_PJ.csv',sep=',')
hoje =date.today()
hoje = f'{hoje.day}-{hoje.month}-{hoje.year}'
for i  in df.index:
    insert(int(df['DDD'][i]), str(df['TELEFONE'][i]),data=hoje, job ='71906_PJ')