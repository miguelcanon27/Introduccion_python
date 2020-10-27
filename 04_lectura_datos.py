


# importamos librerias
import pandas as pd

name = 'excel.csv.csv' # nombre del archivo

df = pd.read_csv(name,sep=',',index_col=0) # leemos archivos csv

estaciones = df.index.unique() # codigo de estaciones 

inicio = df['Fecha'].min() # fecha minima
final = df['Fecha'].max() # fecha maxima

new = pd.date_range(inicio,final,freq='MS') # rango de fechas

datos = pd.DataFrame(index=new) # data frame vacio, con las fechas como index

# ciclo que recorre cada una de las estaciones

for st in estaciones:
    sel = df.loc[st][['Fecha','Valor']].set_index('Fecha') # filtramos de la base de datos, solo las columnas Fecha y valor, 
    #con la funcion set_index, asignamos fecha como nuevo index
    sel.columns = [st] # nombramos la base de datos seleccionada de una columna con el nombre de la estacion

    datos = datos.join(sel,how='outer') # agregamos la base de datos al dataframe vacio

datos.to_excel('series_caudal.xlsx','caudal') # guardamos en excel








