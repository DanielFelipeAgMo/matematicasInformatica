""" La destructuración (también conocida como "unpacking") en Python es una técnica que te permite extraer elementos de estructuras de datos como 
listas, tuplas y conjuntos, y asignarlos a variables individuales de manera más concisa. 
Puedes usar la destructuración en conjunto con la comprensión de conjuntos para crear conjuntos de una manera más eficiente.
Veamos un ejemplo de cómo puedes usar la destructuración en una comprensión de conjunto:
 """

 # Lista de coordenadas en el formato (x, y)
coordenadas = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Usando comprensión de conjunto con destructuración para crear un conjunto de valores "x"
conjunto_x = {x for x, _ in coordenadas}

print("Conjunto de valores x:", conjunto_x)

""" En este ejemplo, tenemos una lista de coordenadas donde cada elemento es una tupla en el formato (x, y). 
Utilizamos una comprensión de conjunto para crear un conjunto que contenga solo los valores de "x" de estas coordenadas. 
La destructuración se realiza en la parte for x, _ in coordenadas, donde estamos extrayendo el primer valor de cada tupla (el valor de "x")
y descartando el segundo valor (el valor de "y") usando _. """


#Supongamos que tienes una lista de nombres completos y quieres crear un conjunto que contenga solo los primeros nombres de cada persona. Puedes lograrlo utilizando la destructuración en una comprensión de conjunto de la siguiente manera:

# Lista de nombres completos en el formato "Nombre Apellido"
nombres_completos = ["Alice Smith", "Bob Johnson", "Charlie Brown", "David Lee"]

# Usando comprensión de conjunto con destructuración para crear un conjunto de primeros nombres
conjunto_primeros_nombres = {nombre for nombre, _ in map(str.split, nombres_completos)}

print("Conjunto de primeros nombres:", conjunto_primeros_nombres)


""" En este ejemplo, estamos usando la función str.split para dividir cada nombre completo en sus componentes "Nombre" y "Apellido". Luego, aplicamos la destructuración con nombre, _ en la comprensión de conjunto para extraer solo el primer nombre de cada par "Nombre Apellido".

El resultado será:

arduino

Conjunto de primeros nombres: {'David', 'Bob', 'Charlie', 'Alice'}

Aquí, la destructuración nos permite seleccionar solo los primeros nombres de manera concisa y crear un conjunto de esos primeros nombres utilizando una comprensión de conjunto. """



""" Supongamos que tienes una lista de palabras y deseas crear un conjunto que contenga todas las letras únicas que aparecen en esas palabras. Puedes lograrlo utilizando la destructuración y una comprensión de conjuntos de la siguiente manera:

python
 """
# Lista de palabras
palabras = ["manzana", "banana", "naranja", "pera", "kiwi"]

# Usando comprensión de conjunto con destructuración para crear un conjunto de letras únicas
conjunto_letras_unicas = {letra for palabra in palabras for letra in palabra}

print("Conjunto de letras únicas:", conjunto_letras_unicas)

""" En este ejemplo, estamos utilizando dos ciclos for en la comprensión de conjuntos. El primer ciclo itera a través de las palabras en la lista palabras, y el segundo ciclo itera a través de las letras en cada palabra. La destructuración no se utiliza aquí, pero la combinación de ciclos for y la comprensión de conjuntos nos permite crear un conjunto de todas las letras únicas en las palabras.

El resultado será:


Conjunto de letras únicas: {'z', 'w', 'r', 'n', 'j', 'a', 'i', 'e', 'b', 'p', 'k', 'm', 'u'}

Este conjunto contiene todas las letras únicas que aparecen en las palabras de la lista, y la comprensión de conjuntos nos permite crearlo de manera concisa. """