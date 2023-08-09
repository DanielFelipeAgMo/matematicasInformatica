num1 = "15"
num2 = "6"

# Conversión octal a decimal
decimal1 = int(num1, 8)
decimal2 = int(num2, 8)

# Multiplicación en decimal
multiplicacion_decimal = decimal1 * decimal2

# Conversión decimal a octal
multiplicacion_octal = oct(multiplicacion_decimal)[2:]

print("Multiplicación octal:", multiplicacion_octal)
