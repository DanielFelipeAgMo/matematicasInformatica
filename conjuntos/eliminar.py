#Puedes eliminar elementos de un conjunto utilizando los métodos remove() o discard(). 
#La diferencia es que remove() lanzará un error si el elemento no está presente, 
#mientras que discard() no arrojará ningún error.

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

conjunto_a.remove(3)
conjunto_a.discard(10)  # Si el elemento no existe, no ocurre ningún error
