# Tuples en Python

# Un tuple es una estructura de datos, que permite almacenar varios elementos de tipos diferentes en una unica variable.

#Los tuples son inmutables, quiere decir que no pueden ser modificados

#En Python los tuples pueden ser creados utilizando parentesis y pueden contener cualquier combinacion de tipos de datos


# Ejemplo de tuple

barca_player = ("Lewan", "Ferran", "Gavi", "Lamine")

#Podemos hacer muchas cosas con los tuples 

#Para obtener su longitud utilizamos len()

longitud_tuple = len(barca_player)
print(longitud_tuple) #nos arrojara cuatro, la longitud del tuple barca_player

#Acceder a un elemento indicando el indice (index)

position_two = barca_player[2]
print(position_two) #Arroja Gavi,(recordar que empieza a contar desde el 0)

#Acceder a mas de un valor con slicing

more_players = barca_player[0:3]
print(more_players) #Arroja los tres primeros valores indicados del 0 al 3

#Acceder al indice o index donde esta un valor

ferra_player = barca_player.index("Ferran")
print(ferra_player) #arroja 1 porque es la posicion donde se encuentra la string Ferran

