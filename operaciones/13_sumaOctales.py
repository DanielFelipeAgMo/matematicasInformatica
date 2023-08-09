num1 = "23"
num2 = "10"

# Conversión octal a decimal
decimal1 = int(num1, 8)
decimal2 = int(num2, 8)

# Suma en decimal
suma_decimal = decimal1 + decimal2

# Conversión decimal a octal
suma_octal = oct(suma_decimal)[2:]

print("Suma octal:", suma_octal)
