#FORMA RECURSIVA PARA TRABAJAR UN FACTORIAL

#Utilizar el patron del factorial -> numero!=numero*(numero-1)!

#CONDICIONES: 0! = 1 , 1! = 1 

def factorial(numero):
    if (numero == 1 or numero==0):
        return 1
    return (numero*factorial(numero-1))


def menu():
    print('---------------------')
    print('Ingrese el número para obtener su factorial: ')
    entrada = input()
    print(factorial(int(entrada)))
menu()


# 5 * 24 = 120
# 4 * 6
# 3 * 2
# 2 * 1
# 1 *
# Se implementa ese patron matematico

#5*fact(5-1)->5*fact(4)->4*fact(3)->3*fact(2)->2*fact(1) luego se retorna un 1 
