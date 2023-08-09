num1 = "24"
num2 = "4"

# Conversión octal a decimal
decimal1 = int(num1, 8)
decimal2 = int(num2, 8)

# División en decimal
division_decimal = decimal1 / decimal2

# Conversión decimal a octal
division_octal = oct(int(division_decimal))[2:]

print("División octal:", division_octal)
