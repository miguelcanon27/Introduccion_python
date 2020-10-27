

"""codigo estructura de datos comentario largo entre comillas"""
#tipos de datos

# int entero
#long enteros largos, se pueden representar en octal o hexacedcimal
# float valores reales de punto flotante
#complex (numeros complejos)



# numericas
a = 2
b = 2.3

#alfanumericas
name = 'miguel'



############## cadenas

titulo = 'Bienvenidos al Curso Evaluacion del Recurso Hidrico'

# como acceder a caracteres de una cadena

# print(titulo) # funcion print nos muestra el resultado 
# print(titulo[0]) # primer caracter
# print(titulo[0:11]) # conjunto de caracteres
# print(titulo[11:-30]) # conjunto de caracteres eliminando los 30 ultimos
# date = ' -26-10-2020' # cadena
# print(titulo+date) # concatenar cadenas


################# Operadores


# operadores aritmeticos

c = a + b # suma
d = a - b #resta
e = a * b # multiplicacion
f = a / b #division
g = a ** 2 # Potencia


#operadores logicos

print(a == b) #igualdad
print(a != b) # diferente
print(a > b) # a mayor
print(a <= b) # menor o igual

# #operadores compuestos
#
print(not True) #not
print(True and False)# and
print(True or False) # or

# print(a ==2 or a>2)

########### listas

#elementos separados por comas y encerrados entre corchetes [] para acceder empleamos [:]

lista = [1 , 2 , 5] # numericas

lista_a = ['hola','miguel'] # alfanumericas

lista_c = [2,'bienvenidos','hola',20,2.6,1.4444] # combinacion

print( lista + lista_a ) # concatenar dos listas




# tuplas

tupla = (1,3,'miguel')


print(type(lista))


# diccionario

diccio = {'nombre':'miguel',2:'canon',3:29}


print(diccio[2])
















