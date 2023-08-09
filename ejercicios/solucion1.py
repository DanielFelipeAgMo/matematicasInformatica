#import math

num_platos = 5
num_seleccionados = 3
num_combinaciones = (num_platos, num_seleccionados)


#print("el número de combinaciones es: ", num_combinaciones)

# forma larga o personal

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def combinaciones(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print("combinaciones: ",combinaciones(num_platos, num_seleccionados))
    

