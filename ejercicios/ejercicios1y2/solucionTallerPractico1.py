""" En una clase de matemáticas, hay 8 estudiantes dispuestos a formar un equipo de proyecto. 
Si el equipo debe constar de 4 estudiantes, ¿cuántos equipos diferentes se pueden formar? """

""" import math

num_estudiantes = 8
num_equipos = 4

combinaciones_usando_math = math.comb(num_estudiantes, num_equipos)

print("Usando math.comb(), el número de equipos diferentes es:", combinaciones_usando_math) """

""" 
num_estudiantes = 8
num_equipos = 4

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combinaciones(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

num_equipos_alternativo = combinaciones(num_estudiantes, num_equipos)

print("Usando una función propia, el número de equipos diferentes es:", num_equipos_alternativo) """

#----------------------------------------------------------------------------------------------

""" 2.	En un menú de restaurante, hay 6 platos principales y los clientes pueden elegir 2 platos para su comida. 
¿Cuántas combinaciones posibles de platos pueden hacer los clientes? """

""" import math
num_platos = 6
num_seleccionados = 2

combinaciones_usando_math = math.comb(num_platos, num_seleccionados)

print("Usando math.comb(), el número de combinaciones posibles es:", combinaciones_usando_math) """

""" num_platos = 6
num_seleccionados = 2

num_combinaciones_alternativo = combinaciones(num_platos, num_seleccionados)

print("Usando una función propia, el número de combinaciones posibles es:", num_combinaciones_alternativo) """

#---------------------------------------------------------------------------------------------------
""" 1.	Un corredor de atletismo tiene 5 tipos diferentes de zapatos y desea usar uno diferente en cada una de las 3 carreras en las que participará. 
¿De cuántas formas puede elegir los zapatos para las carreras? """

""" import math
num_zapatos = 5
num_carreras = 3

permutaciones_usando_math = math.perm(num_zapatos, num_carreras)

print("Usando math.perm(), el número de formas de elegir los zapatos es:", permutaciones_usando_math) """

""" 
def permutaciones(n, r):
    return factorial(n) // factorial(n - r)

permutaciones_alternativo = permutaciones(num_zapatos, num_carreras)

print("Usando una función propia, el número de formas de elegir los zapatos es:", permutaciones_alternativo) """



#----------------------------------------------------------------------------------------------------
""" 2.	Un músico está organizando un concierto y tiene 7 canciones diferentes para tocar. 
Si planea tocar 4 canciones en total, ¿de cuántas formas diferentes puede elegir el setlist? """

""" import math
num_canciones = 7
num_seleccionadas = 4

permutaciones_usando_math = math.perm(num_canciones, num_seleccionadas)

print("Usando math.perm(), el número de formas de elegir el setlist es:", permutaciones_usando_math)


permutaciones_alternativo = permutaciones(num_canciones, num_seleccionadas)

print("Usando una función propia, el número de formas de elegir el setlist es:", permutaciones_alternativo) """

#-----------------------------------------------------------------------------------------------------
""" 1.	En una fiesta, hay 4 diferentes tipos de refrescos y 3 diferentes tipos de aperitivos. 
Si cada invitado elige un refresco y un aperitivo, ¿cuántas combinaciones de refresco y aperitivo diferentes pueden hacer los invitados? """

""" import math
num_refrescos = 4
num_aperitivos = 3

combinaciones_usando_math = math.comb(num_refrescos, 1) * math.comb(num_aperitivos, 1)

print("Usando math.comb(), el número de combinaciones diferentes es:", combinaciones_usando_math) """


#------------------------------------------------------------------------------------------------------
""" 2.	Un puzzle tiene 8 piezas diferentes y se pueden encajar en un tablero de 3x3. 
Si una pieza debe ir en el centro, ¿de cuántas formas diferentes se pueden colocar las otras 8 piezas alrededor de ella? """

""" import math
num_piezas = 8

# El centro ya está ocupado, por lo que hay 8 espacios disponibles para las otras piezas
permutaciones_usando_math = math.perm(num_piezas, num_piezas)

print("Usando math.perm(), el número de formas diferentes de colocar las piezas es:", permutaciones_usando_math)


permutaciones_alternativo = permutaciones(num_piezas, num_piezas)

print("Usando una función propia, el número de formas diferentes de colocar las piezas es:", permutaciones_alternativo) """


#------------------------------------------------------------------------------------------------------------------------
""" Conversión de decimal a binario:
    Número decimal: 42

Solución:
Utiliza la función bin() para convertir un número decimal a binario.

python

numero_decimal = 42
numero_binario = bin(numero_decimal)

print("La conversión de decimal a binario es:", numero_binario)

La salida será:

csharp

La conversión de decimal a binario es: 0b101010

    Conversión de binario a decimal:
        Número binario: 101010

Solución:
Utiliza la función int(numero_binario, base) para convertir un número binario a decimal.

python

numero_binario = "101010"
numero_decimal = int(numero_binario, 2)

print("La conversión de binario a decimal es:", numero_decimal)

La salida será:

csharp

La conversión de binario a decimal es: 42

    Conversión de decimal a octal:
        Número decimal: 128

Solución:
Utiliza la función oct() para convertir un número decimal a octal.

python

numero_decimal = 128
numero_octal = oct(numero_decimal)

print("La conversión de decimal a octal es:", numero_octal)

La salida será:

csharp

La conversión de decimal a octal es: 0o200

    Conversión de octal a decimal:
        Número octal: 54

Solución:
Utiliza la función int(numero_octal, base) para convertir un número octal a decimal.

python

numero_octal = "54"
numero_decimal = int(numero_octal, 8)

print("La conversión de octal a decimal es:", numero_decimal)

La salida será:

csharp

La conversión de octal a decimal es: 44

    Conversión de decimal a hexadecimal:
        Número decimal: 255

Solución:
Utiliza la función hex() para convertir un número decimal a hexadecimal.

python

numero_decimal = 255
numero_hexadecimal = hex(numero_decimal)

print("La conversión de decimal a hexadecimal es:", numero_hexadecimal)

La salida será:

csharp

La conversión de decimal a hexadecimal es: 0xff

    Conversión de hexadecimal a decimal:
        Número hexadecimal: 1A3

Solución:
Utiliza la función int(numero_hexadecimal, base) para convertir un número hexadecimal a decimal.

python

numero_hexadecimal = "1A3"
numero_decimal = int(numero_hexadecimal, 16)

print("La conversión de hexadecimal a decimal es:", numero_decimal)

La salida será:

csharp

La conversión de hexadecimal a decimal es: 419
 """