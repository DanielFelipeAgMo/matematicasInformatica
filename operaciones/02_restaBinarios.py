num1 = "1101"
num2 = "1010"

# Conversión binario a decimal
decimal1 = int(num1, 2)
decimal2 = int(num2, 2)

# Resta en decimal
resta_decimal = decimal1 - decimal2

# Conversión decimal a binario
resta_binario = bin(resta_decimal)[2:]

print("Resta binaria:", resta_binario)
