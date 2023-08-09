import math

num_ases = 4
total_cartas = 52
num_seleccionadas = 5

combinaciones_sin_as = math.comb(total_cartas - num_ases, num_seleccionadas)
combinaciones_totales = math.comb(total_cartas, num_seleccionadas)
combinaciones_con_un_as = combinaciones_totales - combinaciones_sin_as

print(combinaciones_sin_as)
print(combinaciones_totales)
print(combinaciones_con_un_as)