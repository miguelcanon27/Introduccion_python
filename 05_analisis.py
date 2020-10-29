

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""en el siguiente script encontraran algunas funciones para leer y analizar series de tiempo mediante las librerias 
pandas y matplotlib"""

name = 'Datos_mensuales.xlsx' # nombre del archivo


df = pd.read_excel(name,'QL_1',index_col=0) #llamamos el archivo, especificamos la hoja QL1




estaciones = df.columns # lista nombre de estaciones

#plot a partir de la estructura de dataframe
#se grafican todos los elementos que contiene la base de datos

df.plot(figsize=(10,8))
plt.savefig('series_caudal.png',dpi=200) # se guarda la figura en formato png
plt.show() # comando para mostrar las imagenes

# ciclo que permite mostrar todas las graficas
for sta in estaciones[0:2]: # ciclo limitado para el primer y segun elemento
    plt.plot(df.index, df[sta], '--', color='r', linewidth=0.5) # caracteristicas del plot
    plt.title('Estacion  de caudal '+ str(sta)  )
    plt.ylabel('m3/s')
    plt.xlabel('meses')
    # plt.show()


# grafica donde se muestran dos series de tiempo en la misma figura
plt.plot(df.index,df[estaciones[0]],'--',color='r',linewidth=0.5)
plt.plot(df.index,df[estaciones[2]],'-.',color='b',linewidth=0.5)
plt.title('Estaciones caudal '  )
plt.ylabel('m3/s')
plt.xlabel('meses')
plt.show()


# determinar porcentaje de datos vacios teniendo en cuenta la fecha inicial y final de la base de datos

valores_vacios = df.isnull().sum() # determinamos los valores nulos (nan), luego sumamos

total_n = df.index.size # numero total de la serie en la fecha "esperada"

porcentaje = (valores_vacios/total_n) * 100

print(' % Faltantes ',porcentaje)

####funcion de llenado de datos


serie = df[13067020]

fill_1 = serie.interpolate() # funcion de interpolacion, por defecto metodo lineal
fill_2 = serie.interpolate(method='polynomial',order=3) # polinomio de orden 3

# graficamos la serie original, interpolacion lineal e interpolacion polinomial
plt.plot(serie.index, serie, color='r',label='orginal')
plt.plot(serie.index, fill_1, '--',color='b',label='lineal')
plt.plot(serie.index,fill_2,'-.',color='g',label='poly')
plt.legend()

plt.show()


resultado = pd.DataFrame(fill_1) # resultado de interpolacion lineal, el formato serie lo convertimos en dataframe
#
resultado.to_excel('datos_llenos.xlsx','QL_1') # exportamos a una hoja de excel









#     df_g.to_excel(xls,sheet_name=str(sta))
# xls.save()












