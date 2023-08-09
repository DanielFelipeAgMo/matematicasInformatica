num1 = "1A"
num2 = "B"

# Conversión hexadecimal a decimal
decimal1 = int(num1, 16)
decimal2 = int(num2, 16)

# Suma en decimal
suma_decimal = decimal1 + decimal2

# Conversión decimal a hexadecimal
suma_hexadecimal = hex(suma_decimal)[2:].upper()

print("Suma hexadecimal:", suma_hexadecimal)
