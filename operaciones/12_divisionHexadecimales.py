num1 = "C"
num2 = "2"

# Conversión hexadecimal a decimal
decimal1 = int(num1, 16)
decimal2 = int(num2, 16)

# División en decimal
division_decimal = decimal1 / decimal2

# Conversión decimal a hexadecimal
division_hexadecimal = hex(int(division_decimal))[2:].upper()

print("División hexadecimal:", division_hexadecimal)
