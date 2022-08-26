'''Nota Importante:
    Las funciones siempre deben definirse antes de ser llamadas.'''

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

numx = 14
numy = 20

res = suma(numx,numy)
print(res)

def repetirMensaje(msg,n):
    return msg*n

mensaje = 'Hola'
print(repetirMensaje(mensaje,3))

def mostrarMensaje(msg):
    print(msg)

mostrarMensaje('Hola mundo!')