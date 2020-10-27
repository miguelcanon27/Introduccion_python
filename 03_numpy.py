# libreria numpy

# es una biblioteca de soporte numerico para arreglos y matrices multidimensionales
# que cuenta con multiples funciones matematicas

#listas y array

# Los arrays son un tipo de dato, similar a las listas, pero orientados especialmente al cálculo numérico.
# podriamos considerarlos vectores o matrices

# listas no estan pensadas para el procesamiento numerico

#### convertir una lista en arreglo
y = [2, 4,5,6,7,8,1,2,34]

x = np.array(y)


# crear un vector con valores en un rango
a = np.arange(1,10)


# crear una matriz a partir de un vecor

m = a.reshape(3,3)


# generar una matriz identidad
m_ide = np.identity(10)

vector = np.random.random(9)
matrix = np.random.random((3,2))

print(vector)
print(np.mean(vector))

# operadores

sum = np.sum(x)

min = np.min(x)
max = np.max (x)

exp = np.exp(x)


