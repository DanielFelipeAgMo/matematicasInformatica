num1 = "1101"
num2 = "1010"

# Conversión binario a decimal
decimal1 = int(num1, 2)
decimal2 = int(num2, 2)

# División en decimal
division_decimal = decimal1 // decimal2

# Conversión decimal a binario
division_binario = bin(division_decimal)[2:]

print("División binaria:", division_binario)
