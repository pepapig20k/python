from functools import reduce

def impares(x):
    return x % 2 != 0
def suma_impares(numeros):
    impar = filter(impares, numeros)
    return reduce(lambda a, b: a + b, impar)
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = suma_impares(numeros)
print(result)
