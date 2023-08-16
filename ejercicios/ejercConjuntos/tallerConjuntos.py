#Ejercicio 1 Unión e Intersección
#Dado dos conjuntos, calcula e imprime su unión y su intersección

conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

union = conjunto_a.union(conjunto_b)
interseccion = conjunto_a.intersection(conjunto_b)

print("Unión:", union)
print("Intersección:", interseccion)

#Ejercicio 2 Eliminar Duplicados
#Dada una lista de números, crea un conjunto a partir de la lista para eliminar los elementos duplicados y luego convierte el conjunto nuevamente en una lista.

numeros = [1, 2, 2, 3, 4, 4, 5, 6]
conjunto_numeros = set(numeros)
lista_sin_duplicados = list(conjunto_numeros)

print("Lista original:", numeros)
print("Lista sin duplicados:", lista_sin_duplicados)

#Ejercicio 3 Comprobación de Pertinencia
#Dado un conjunto y un valor, verifica si el valor está presente en el conjunto.

mi_conjunto = {10, 20, 30, 40, 50}
valor = 30

if valor in mi_conjunto:
    print(f"El valor {valor} está en el conjunto.")
else:
    print(f"El valor {valor} no está en el conjunto.")

#Ejercicio 4 Combinaciones de Palabras
#Dadas dos cadenas, crea conjuntos de letras únicas para cada cadena y luego calcula e imprime las letras que están presentes en ambos conjuntos.

cadena_a = "hola"
cadena_b = "adios"

conjunto_a = set(cadena_a)
conjunto_b = set(cadena_b)

letras_comunes = conjunto_a.intersection(conjunto_b)

print("Letras comunes:", letras_comunes)

#Ejercicio 5 Palabras Únicas
#Dada una lista de palabras, crea un conjunto de palabras únicas y luego ordena e imprime las palabras en orden alfabético.

palabras = ["manzana", "banana", "naranja", "manzana", "pera", "banana"]
conjunto_palabras = set(palabras)
palabras_unicas = sorted(list(conjunto_palabras))

print("Palabras originales:", palabras)
print("Palabras únicas:", palabras_unicas)

