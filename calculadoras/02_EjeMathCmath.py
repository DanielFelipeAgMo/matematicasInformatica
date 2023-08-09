import math
import cmath

def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal

# Ejemplo de uso del módulo math
numero_decimal = 3.14
seno = math.sin(numero_decimal)
print("El seno de", numero_decimal, "es:", seno)

# Ejemplo de uso del módulo cmath
numero_complejo = complex(2, 3)
raiz_cuadrada = cmath.sqrt(numero_complejo)
print("La raíz cuadrada de", numero_complejo, "es:", raiz_cuadrada)

# Ejemplo de conversión decimal a binario utilizando las funciones definidas anteriormente
numero_decimal = 15
binario = decimal_a_binario(numero_decimal)
print("La representación binaria de", numero_decimal, "es:", binario)

# Ejemplo de conversión binario a decimal utilizando las funciones definidas anteriormente
numero_binario = "1101"
decimal = binario_a_decimal(numero_binario)
print("La representación decimal de", numero_binario, "es:", decimal)
