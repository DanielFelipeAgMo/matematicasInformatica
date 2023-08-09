num1 = "A"
num2 = "F"

# Conversión hexadecimal a decimal
decimal1 = int(num1, 16)
decimal2 = int(num2, 16)

# Multiplicación en decimal
multiplicacion_decimal = decimal1 * decimal2

# Conversión decimal a hexadecimal
multiplicacion_hexadecimal = hex(multiplicacion_decimal)[2:].upper()

print("Multiplicación hexadecimal:", multiplicacion_hexadecimal)
