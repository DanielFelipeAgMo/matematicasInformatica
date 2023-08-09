""" Hay cuatro candidatos postulados para el mismo puesto. Para que la posición en las boletas de votación no influya en los votantes, es necesario imprimir las boletas con los nombres en todos los órdenes posibles.
¿Cuántas boletas diferentes habrá?
Un ordenamiento de los objetos, como los
nombres en las boletas, se llama permutación.
Esto se debe a que el orden, en este caso, es
importante. """

import math

candidatos = 4
#Calcular el número de permutaciones

numeroBoletas = math.perm(candidatos, candidatos)
print("El número de boletas posibles son: ", numeroBoletas)
