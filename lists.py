# Creemos una lista, para crear una lista utilizamos []
#En el ejemplo podemos observar que una lista puede contener strings, entero y flotantes

list = ["Jhon Mayer", 1,1.5,'gravity',2,3]
print(list)

# Podemos usar indexacion positiva o negativa para acceder a algun valor

print('Usando indexacion\n Positiva:', list[0],'\n Negativa:' ,list[-3])

# Operaciones en listas

#Slice 
print(list[1:3]) 
#Podemos obtener elementos de una lista.

#extend
list.extend(["new light"])
print(list)
#Con el metodo extend podemos agregar elementos a la lista

#append
list.append(['blues', 7])
print(list)
# Con append agregamos un elemento a la lista.

#========================================================================#

#Las listas son mutables, pueden ser modificadas.

#Modificar basado en index

A = ["disco", 10, 1.2]
print('antes de cambio', A)
A[0] = 'Live in LA'
print('despues de cambio', A)
