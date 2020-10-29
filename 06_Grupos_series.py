import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




"""en el siguiente script transformaremos una serie de tiempo en un conjunto estadistico - grupos"""

name = 'Datos_mensuales.xlsx' # nombre del archivo


df = pd.read_excel(name,'QL_1',index_col=0) #llamamos el archivo, especificamos la hoja QL1

estaciones = df.columns # lista nombre de estaciones

xls = pd.ExcelWriter('DATOS_IDEAM_GRUPOS.xlsx') # guardamos series como grupos estadisticos
for sta in estaciones[2:3]:

    serie = df[sta]

    data = pd.DataFrame(serie) # creamos un dataframe con la serie seleccionada
    data['year'] = df.index.year  # seleccionamos el año correspondiente a cada valor de nuestra serie
    data['month'] = df.index.month #seleccionamos el mes correspondiente a cada valor de nuestra serie
    # empleamos la funcion pivot, parte de nuestros datos, debemos seleccionar la columna de indice (año)
    #cuales deberian ser nuestras columnas, en este caso los meses y por ultimo debemos seleccionar el nombre de nuestra serie
    df_mg = data.pivot(index='year', columns='month', values=serie.name)


    # cambiamos nombres de las columnas
    df_mg.columns = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
    print(df_mg) # resultado grupos como conjunto estadistico

    # interpolacion de datos, por fila y columna, datos que no se interpolen se completan con el valor promedio del mes (columna)


    data_fill_adelante = df_mg .interpolate(axis=0) # interpola con los vecinos de la columna
    data_fill_lados = df_mg.interpolate(axis=1) # interpola con sus vecinos de fila

    data_fill = (data_fill_lados + data_fill_adelante) / 2.0 # promedia las dos formas de interpolar

    data_fill = data_fill.fillna(df_mg.mean(axis=0))#completar vacios con el promedio del mes (columnas)


    # algunos estadisticos
    estadisticas = data_fill.describe()

    mean = data_fill.mean(axis=0) # promedio

    std = data_fill.std(axis=0) # desviacion

    # grafico tipo barras
    plt.bar(mean.index, mean.values, 0.8, )
    plt.xlabel('Meses')
    plt.ylabel('m3/s/mes')
    plt.show()




    df_mg.to_excel(xls, sheet_name=str(sta), merge_cells=False) #guardamos en el archivo de excel generado anteriormente,
    # las hojas cambian su nombre por cada una de las estaciones


xls.save() # cerramos el archivo de excel



