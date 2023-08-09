import math

""" numeroLetras = len("PYTHON")
numeroPermutaciones = math.factorial(numeroLetras)

print(numeroPermutaciones) """

""" n = 10
r = 3

numCombinaciones = math.comb(n,r)
print(numCombinaciones) """
""" 
def Danielinpinpin(n):
    if n == 0:
        return 1
    else:
        return n * Danielinpinpin(n-1)
    
numPersonas = 10
tamanioEsquipo = 3

numCombinaciones = Danielinpinpin(numPersonas)// Danielinpinpin(tamanioEsquipo) * Danielinpinpin(numPersonas - tamanioEsquipo)
print(numCombinaciones) """


num_ases = 4
total_cartas = 52
num_seleccionadas = 5

combinaciones_sin_as = math.comb(total_cartas - num_ases, num_seleccionadas)
combinaciones_totales = math.comb(total_cartas, num_seleccionadas)

combinaciones_con_al_menos_un_as = combinaciones_totales - combinaciones_sin_as

print("El número de combinaciones con al menos un as es:", combinaciones_con_al_menos_un_as)

