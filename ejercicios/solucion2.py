""" import math

palabra = "MURCIÉLAGO"
num_letras = len(palabra)
num_permutaciones = math.factorial(num_letras) 
num_letras_repetidas = palabra.count('A') * palabra.count('L')

num_permutaciones_diferentes = num_permutaciones // num_letras_repetidas

print("El número de permutaciones diferentes es:", num_permutaciones_diferentes)
#3628800
 """

#Forma larga o personal

palabra = "MURCIÉLAGO"
num_permutaciones_diferentes = 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
   
def permutaciones_con_repeticion(palabra):
    n = len(palabra)
    repeticiones = {}
    for letra in palabra:
        repeticiones[letra] = repeticiones.get(letra, 0) +1

    denominador = 1
    for repeticion in repeticiones.values():
        denominador *= factorial(repeticion)

        return factorial(n) // denominador

num_permutaciones_diferentes = permutaciones_con_repeticion(palabra)   
print(num_permutaciones_diferentes)