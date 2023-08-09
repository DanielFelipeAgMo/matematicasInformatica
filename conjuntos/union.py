#    Python proporciona diversos métodos y operadores para trabajar con conjuntos:

#Unión: Devuelve un nuevo conjunto con todos los elementos de los conjuntos dados.
conjunto_a = {1, 2, 3}

conjunto_b = {3, 4, 5}

union = conjunto_a.union(conjunto_b) 

# También se puede usar el operador "|"
#union = conjunto_a | conjunto_b

print(union)  # Salida: {1, 2, 3, 4, 5}
