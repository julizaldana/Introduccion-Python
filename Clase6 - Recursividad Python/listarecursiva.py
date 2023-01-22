# RECORRER UNA LISTA DE FORMA RECURSIVA

#len()? 

def mostrarlistarecursiva(lista,indice):
    if indice != len(lista):
        print(lista[indice])
        mostrarlistarecursiva(lista, indice + 1)

lista = ['Toyota', 'Mazda', 'BMW', 'Nissan', 'Hyundai']
mostrarlistarecursiva(lista,0)
