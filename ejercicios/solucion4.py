# Dígitos disponibles
digitos_disponibles = [1, 2, 3, 4]
# Inicializar contador de números de 3 dígitos
num_numeros_3_digitos = 0


# Generar los números de 3 dígitos sin repetición de dígitos
for digito_centenas in digitos_disponibles:
    for digito_decenas in digitos_disponibles:
        for digito_unidades in digitos_disponibles:
            # Verificar que los dígitos sean diferentes
            if (digito_centenas != digito_decenas) and (digito_centenas != digito_unidades) and (digito_decenas != digito_unidades):
                # Formar el número de 3 dígitos y contarlo
                numero_3_digitos = digito_centenas * 100 + digito_decenas * 10 + digito_unidades
                num_numeros_3_digitos += 1





print("la cantidad de números de 3 dígitos sin repetir son:", num_numeros_3_digitos) 

 
""" import math

num_digitos = 4
num_digitos_seleccionados = 3

num_arreglos = math.perm(num_digitos, num_digitos_seleccionados)

print("la cantidad de números de 3 dígitos sin repetir son:", num_arreglos)
 """