#RECURSIVIDAD: EL OBJETIVO ES SIMPLIFICAR Y REUTILIZAR LA MISMA FUNCION
#Obtener la suma de un numero dado restandole uno, por ejemplo: 6-> 6+5+4+3+2+1=21

def sumarecursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumarecursiva(numero-1)


def menu():
    print("-----------------------")
    print("Ingrese el número para obtener la suma recursiva:" )
    entrada = input()
    print(sumarecursiva(int(entrada)))

menu()


# 5 + 10 = 15
# 4 + 6
# 3 + 3
# 2 + 1
# 1
#Seguir el patrón matemático