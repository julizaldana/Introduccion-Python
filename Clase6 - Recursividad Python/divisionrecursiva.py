#DIVISION CON RESTAS SUCESIVAS 
# Se suma el 1, porque es el numero de veces, que se va a contar

'''def divrecursiva(numero1,numero2):
    if numero1 < numero2:
        return 0
    return (1 + divrecursiva(numero1-numero2,numero2))  
    '''    


def divrecursiva(numero1,numero2):
    if numero1 >= numero2:
        return (1 + divrecursiva(numero1-numero2,numero2))  
    return 0      



def menu():
    print("-----------------------")
    print("Ingrese los números para obtener la división recursiva:" )
    entrada1 = input()
    entrada2 = input()
    print("El resultado es: ")
    print(divrecursiva(int(entrada1),int(entrada2)))

menu()


# si numero1=8, numero2=2
# 8 < 2
# 1 + (8-2,2) = 1 + (6,2) como 6 > 2 continua
# 1 + (6-2,2) = 1 + (4,2) como 4 > 2 continua
# 1 + (4-2,2) = 1 + (2,2) como 2 >/ 2 continua
# 1 + (2-2,2) = 1 + (0,2) como 0 < 2 se para y retorna 0
# De abajo para arriba, 0 + 1 + 1 + 1 + 1 = 4