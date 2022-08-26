#Imprimir "hello world!" en consola
print("Hello world!")

"""Crear variables en python
Debe iniciar con letra y puede seguir
con una combinacion de letras, numeros o guion bajo(_)"""
Nombre = "Luis"
Edad = 12

#Imprimir el contenido de una variable en consola
print(Nombre) 
print("Mi edad es: ")
print(Edad)
print("")


#Cambiar el valor de una variable
Edad = 42       #Edad se actualiza y ahora tendra el valor 42
Edad = True     #Edad se vuelve a actualizar y ahora contiene el valor True

"""Se imprimira el ultimo valor guardado en la variable edad
En este caso mostrara el valor True"""
print(Edad)
print("")     

#------------------------Operaciones Basicas-----------------
num1 = 16
num2 = 8

#Suma
Resultado = num1 + num2
print("Suma")
print(Resultado)
print("")


#Resta
Resultado = num1 - num2
print("Resta")
print(Resultado)
print("")

#multiplicacion
Resultado = num1*num2
print("Multiplicacion")
print(Resultado)
print("")

#Division
#El resultado de la division devolvera un dato de tipo float
#Aunque la division sea exacta
Resultado = num1/num2
print("Division")
print(Resultado)
print("")

#Exponenciacion
#num1**num2 => num1^num2 (num1 elevado a la num2)
Resultado = num1**num2
print("Exponenciacion")
print(Resultado)
print("")

#-----------------------------------------------------


#Ingreso de datos en consola
"""Se utiliza la funcion input() la cual debe
estar guardada en una variable. Lo que se ingrese
en consola por medio de esta fucnion sera guardado
como un dato de tipo string"""

Nombre = input("Ingrese su nombre completo: ")
print(Nombre)
print("")


num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")


#Por esta razon al querer sumar dos numeros en vez de mostrar
#su resultado, se mostrara una concatenacion.
resultado = num1+num2
print(resultado)