num1 = "1A"
num2 = "B"

# Conversión hexadecimal a decimal
decimal1 = int(num1, 16)
decimal2 = int(num2, 16)

# Resta en decimal
resta_decimal = decimal1 - decimal2

# Conversión decimal a hexadecimal
resta_hexadecimal = hex(resta_decimal)[2:].upper()

print("Resta hexadecimal:", resta_hexadecimal)
