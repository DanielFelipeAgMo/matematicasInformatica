conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

#dif_simetrica = conjunto_a.symmetric_difference(conjunto_b)  

# También se puede usar el operador "^"
dif_simetrica = conjunto_a ^ conjunto_b 

print(dif_simetrica)  # Salida: {1, 2, 4, 5}
