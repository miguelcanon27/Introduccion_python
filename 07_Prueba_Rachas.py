
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t # llamamos la distribucion T de student

"""el siguiente codigo realiza la prueba de rachas partiendo de un archivo de series de tiempo
trasforma a conjuntos estadisticos y genera la prueba para cada una de las realizaciones"""


name = 'Datos_mensuales.xlsx' # nombre del archivo


df = pd.read_excel(name,'QL_1',index_col=0) #llamamos el archivo, especificamos la hoja QL1

estaciones = df.columns # lista nombre de estaciones


for sta in estaciones[0:1]:

    serie = df[sta]

    data = pd.DataFrame(serie)
    data['year'] = df.index.year
    data['month'] = df.index.month


    df_mg = data.pivot(index='year', columns='month', values=serie.name)

    data_fill_adelante = df_mg .interpolate(axis=0)
    data_fill_lados = df_mg.interpolate(axis=1)

    data_fill = (data_fill_lados + data_fill_adelante) / 2.0

    data_fill = data_fill.interpolate(axis=0).interpolate(axis=1).fillna(df_mg.mean(axis=0))


    # para consultar la teoria de la prueba de rachas pueden dirigirse al siguiente link:
    # http://docs.google.com/viewer?a=v&pid=sites&srcid=bWF0aG1vZGVsbGluZy5vcmd8d3d3fGd4OjI2ZWNiNmZmNTY2MmJkY2I

    mean = data_fill.mean()  # determina el promedio

    #transformamos nuestros datos en un sistema binario, en este caso diferenciado por signos + valores encima del promedio,
    # - valores por debajo del promedio

    signos = data_fill.where(data_fill>=mean,other='-') # funcion que permite realizar una condicion, en este caso,
    # si la condicion no se cumple se asigna el valor asignado en "other"
    #asignamos el signo negativo a los valores que sean menores que el promedio, funcion que permite hacer condicionales

    signos = signos.where(data_fill<mean,other='+')
    #asignamos el signo positivo  a los valores que sean mayores que el promedio

    re_binario = np.where(signos.values[0:-1] == signos.values[1:],0,1)
    #transformamos los signos en rachas, observando la diferencia entre cada uno de los elementos,
    #signos iguales se asigna el valor 0, signos diferentes valor 1


    re = re_binario.sum(axis=0) + 1 # determinamos el numero empirico de rachas, sumatoria de la lista anterior de 0 y 1

    n = data_fill.count()  # coontar numero de datos

    rt = (n + 1) / 2.0  #rachas teorico
    sigma_r = np.sqrt(n - 1) / 2  # raizz cuadrada, desviacion estandar de la rachas teoricas

    alfa = 0.05 # nivel de significancia

    # tds  es el cuantil para el percentil (1-alfa) de la distribucion t de student, siendo alfa el nivel de significacion
    ts = t.isf(alfa,n-1)

    limit_izq = rt - (ts * sigma_r)  # intervalo a la izquierda

    limit_derecho = rt + (ts * sigma_r)  # intervalo a la derecha

    H0 = np.logical_and(re>=limit_izq,re<=limit_derecho) #funcion logica con dos argumentos

    H0_s = np.where(H0, 'Aceptada', 'Rechazada')  # condicional, si es Verdadero, el resultado sera Aceptado

    meses =  ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

    # creamos data frame con los resultados, indice meses y columna nombre de la estacion
    resultado = pd.DataFrame(H0_s,columns=[str(sta)],index=meses).T  # .T, traspone el dataframe
    print(resultado )
    # la prueba dara resultado para cada una de las realizaciones del conjunto estadistico, la prueba se realiza para todos los meses

    """
    estructura de resultado:
                     meses 
                    ene        feb        mar  ...        oct        nov        dic
    Nombre_Estacion  Rechazada  Rechazada  Rechazada  ...  Rechazada  Rechazada  Rechazada
    
    """