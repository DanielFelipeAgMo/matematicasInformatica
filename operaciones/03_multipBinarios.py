num1 = "1101"
num2 = "1010"

# Conversión binario a decimal
decimal1 = int(num1, 2)
decimal2 = int(num2, 2)

# Multiplicación en decimal
multiplicacion_decimal = decimal1 * decimal2

# Conversión decimal a binario
multiplicacion_binario = bin(multiplicacion_decimal)[2:]

print("Multiplicación binaria:", multiplicacion_binario)
