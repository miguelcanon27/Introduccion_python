
import pandas as pd

name = 'excel.csv.csv'

df = pd.read_csv(name,sep=',',index_col=0)

estaciones = df.index.unique()

inicio = df['Fecha'].min()
final = df['Fecha'].max()

new = pd.date_range(inicio,final,freq='MS')

datos = pd.DataFrame(index=new)

for st in estaciones:
    sel = df.loc[st][['Fecha','Valor']].set_index('Fecha')
    sel.columns = [st]

    datos = datos.join(sel,how='outer')

datos.to_excel('series_caudal.xlsx','caudal')








