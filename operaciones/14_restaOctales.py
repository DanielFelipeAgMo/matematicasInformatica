num1 = "23"
num2 = "10"

# Conversión octal a decimal
decimal1 = int(num1, 8)
decimal2 = int(num2, 8)

# Resta en decimal
resta_decimal = decimal1 - decimal2

# Conversión decimal a octal
resta_octal = oct(resta_decimal)[2:]

print("Resta octal:", resta_octal)
