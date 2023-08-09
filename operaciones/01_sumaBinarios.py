num1 = "1101"
num2 = "1010"

# Conversión binario a decimal
decimal1 = int(num1, 2)
decimal2 = int(num2, 2)

# Suma en decimal
suma_decimal = decimal1 + decimal2

# Conversión decimal a binario
suma_binario = bin(suma_decimal)[3:] 
print("Suma binaria:", suma_binario) 
