# Devuelve un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo.
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

diferencia = conjunto_a.difference(conjunto_b)  

# También se puede usar el operador "-"
#diferencia = conjunto_a - conjunto_b

print(diferencia)  # Salida: {1, 2}
