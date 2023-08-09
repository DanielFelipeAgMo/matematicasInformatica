def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal

def suma_decimales(num1, num2):
    suma = num1 + num2
    return suma

def resta_decimales(num1, num2):
    resta = num1 - num2
    return resta

def multiplicacion_decimales(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion

def division_decimales(num1, num2):
    division = num1 / num2
    return division

def calcular_binario():
    binario1 = input("Ingresa el primer número binario: ")
    binario2 = input("Ingresa el segundo número binario: ")
    decimal1 = binario_a_decimal(binario1)
    decimal2 = binario_a_decimal(binario2)

    print("El primer número en decimal es:", decimal1)
    print("El segundo número en decimal es:", decimal2)

    suma_decimal = suma_decimales(decimal1, decimal2)
    resta_decimal = resta_decimales(decimal1, decimal2)
    multiplicacion_decimal = multiplicacion_decimales(decimal1, decimal2)
    division_decimal = division_decimales(decimal1, decimal2)

    print("La suma en decimal es:", suma_decimal)
    print("La resta en decimal es:", resta_decimal)
    print("La multiplicación en decimal es:", multiplicacion_decimal)
    print("La división en decimal es:", division_decimal)

    binario_suma = decimal_a_binario(suma_decimal)
    binario_resta = decimal_a_binario(resta_decimal)
    binario_multiplicacion = decimal_a_binario(multiplicacion_decimal)
    binario_division = decimal_a_binario(division_decimal)

    print("La suma en binario es:", binario_suma)
    print("La resta en binario es:", binario_resta)
    print("La multiplicación en binario es:", binario_multiplicacion)
    print("La división en binario es:", binario_division)

calcular_binario()
