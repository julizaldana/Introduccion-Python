#PILA es un TDA - LIFO
#Representación de una pila mediante una lista, usando una clase

class Pila:

    def __init__(self):
        self.platos=[]

#FUNCIÓN APILAR - AGREGAR PLATOS

    def apilarPlatos(self,plato):
        self.platos.append(plato)           #Utilizamos .append(), nos ayuda a agregar un plato a la pila

    def estaVacia(self):
        return len(self.platos)==0


#FUNCIÓN DESAPILAR - QUITAR PLATOS

    def desapilarPlatos(self):
        if self.estaVacia():
            print("La pila está vacía")
            return None
        return self.platos.pop()        #Utilizamos .pop(), nos ayuda a eliminar un plato de una pila 

    def tamaño(self):
        return len(self.platos)

    def mostrarPlatos(self):
        print("El orden los platos es: ")
        print(self.platos)


p = Pila()

p.apilarPlatos('plato rojo')
p.apilarPlatos('plato verde')
p.apilarPlatos('plato amarillo')
print(p.mostrarPlatos())

p.desapilarPlatos()     #Se quitaría el plato amarillo
print(p.mostrarPlatos())