# Los directiorios en Python consisten de key y values, podemos compararlos con listas en en donde
#podriamos decir que los index son los key y los elementos los values/elementos de un directorio

#Un ejemplo es que un directorio de direccion en el que calle podria ser el key y el valor de calle el elemento/valor

#En resumen, dentro de un directorio cada elemento es representado por un key y su valor corrrespondiente los diccionarios
#se crean con curly brackets {} que contienen keys y values separados por una coma 

#Los directorios se crean de la siguiente forma

john_mayer = {"Inside Wants Out":"1991","Room for Squares": "2001", "Heavier Things": "2004"} #estamos creando el directorio john mayer

#Acceder a valores de un key

keyValue = john_mayer["Inside Wants Out"]
print(keyValue) #Nos dira el 1991 que es el valor del key Inside wants out
