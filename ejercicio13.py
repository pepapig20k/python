paises = input("Indicame paises separados por comas:  ")

lista_paises = list(set(paises.split(",")))

lista_paises.sort()

print(",".join(lista_paises))