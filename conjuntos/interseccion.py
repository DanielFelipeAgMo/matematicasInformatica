#Devuelve un nuevo conjunto con los elementos comunes entre los conjuntos dados.
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

interseccion = conjunto_a.intersection(conjunto_b)  

# También se puede usar el operador "&"
#interseccion = conjunto_a & conjunto_b

print(interseccion)  # Salida: {3}
