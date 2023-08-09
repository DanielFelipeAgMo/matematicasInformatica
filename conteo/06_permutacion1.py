#utilizando un enfoque combinatorio

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num_candidatos = 4

# Calcular el número de permutaciones utilizando la fórmula del factorial
num_boletas = factorial(num_candidatos)

print("El número de boletas diferentes es:", num_boletas)

    