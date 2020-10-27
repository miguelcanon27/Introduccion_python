



##### Flujo por Gravedad


# y = a x + b

# y = ax + b
 # T = a * altitud + B


"""

a = -0.00496
b = 31.21

altitud = float(input('Introduzca el valor de altitud:'))

#print('Temperatura ',T )

# CONDICIONALES

if altitud > 1500:
    print('Error altitud mayor a 1500')
elif altitud < 400:
    print('Error altitud menor a 400')

else:
    T = a * altitud + b
    print('Temperatura ', T)
"""

# () acceder a funciones, tuplas
# [] acceder a los datos
# : usar ciclos, condicionales, funciones
# . acceder a caracteristicas, parametros
# '' cadenas alfanumericos

# Funciones

def temperatura (h):
    """
    Funcion que determina la tempeartura mediante la altitud
    :param h: altitud en msnm
    :return: temperatura
    """
    a = -0.00496
    b = 31.21

    if h > 1500:
        T = 999
    elif h < 400:
        T = -99
    else:
        T = a * h + b

    return T


#interaciones

lista = ['altitud_1','altitud_2','altitud_3','altitud_4'] # lista

dicci = {'altitud_1':1500,'altitud_2':200,'altitud_3':1000,'altitud_4':600} # diccionario

resultado = [] # lista vacia que almacenara los resultados
for n in lista: # ciclo for

    altitud = dicci[n] # selecionamos el valor de altitud en el diccionario 

    Te = temperatura(altitud) # corremos la funcion

    resultado.append(Te) #adicionamos el resultado a la lista vacia

print(resultado)























