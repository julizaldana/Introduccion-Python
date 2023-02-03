#MULTIPLICACIÓN RECURSIVA

#A nivel de eficiencia. Los valores de entrada tienen que ser no negativos.
'''def multrecursiva(numero1,numero2):
    if numero2 > 0:
        return (numero1 + multrecursiva(numero1,numero2-1))
    else:
        return 0'''  


def multrecursiva(numero1,numero2):
    if numero2 == 0:
        return 0      
    else:
        return (numero1 + multrecursiva(numero1,numero2-1))  


def menu():
    print("-----------------------")
    print("Ingrese los números para obtener la multiplicación recursiva:" )
    entrada1 = input()
    entrada2 = input()
    print("El resultado es: ")
    print(multrecursiva(int(entrada1),int(entrada2)))

menu()

# si numero1=8, numero2=2
# 8 * 2
# 2 == 0 no -> (8,(2-1))