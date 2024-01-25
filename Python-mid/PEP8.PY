#Correct identation

#Four spaces for identation are sufficient for appropiate readability.
#Blank lines are used to separate functions and classes
def calcular_cuadrado(numero):
    return numero ** 2

class Calculadora:
    def __init__(self, marca):
        self.marca = marca
        self.resultado = 0

    def sumar(self, numero):
        self.resultado += numero

    def obtener_resultado(self):
        return self.resultado

#Using spaces around operators and commas.

tuple_colors = ('rojo', 'verde', 'azul')

#Using functions for blocks of codes

#Wrong way

if a>b:

    c = c + 5

else:
    c = c - 3

#Correct Way 

def function_1(a, b):
    if a > b:
        c = c + 5
    else:
        c = c - 3
    return c

c = function_1(2, 3)
