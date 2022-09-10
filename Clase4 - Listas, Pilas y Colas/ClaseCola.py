#COLA - TDA que utiliza FIFO 
#Representación de una cola mediante una lista de Python

class Cola:

    def __init__(self):
        self.personas = []
    
    def cantidad(self):                 #Me retorna la cantidad de personas
        return len(self.personas)
    
    def insertar(self, persona):           #SE INSERTA ELEMENTO EN UNA COLA - Una persona entra en la cola
        self.personas.insert(0, persona)
    
    def extraer(self):                      #SE EXTRAE ELEMENTO EN UNA COLA - Una persona sale de la cola
        if self.cantidad():
            return self.personas.pop()
        else:
            return None
    
    def primer_persona(self):               #Se obtiene la primera posición de la cola
        if self.cantidad():
            return self.personas[-1]
    
    def ultima_persona(self):           #Se obtiene la útlima posición de la cola
        if self.cantidad():
            return self.personas[0]

    def mostrarColadePersonas(self):
        print("El orden de las personas en la cola es:")
        print(self.personas)
    


personasencola = Cola()
personasencola.insertar('Jennifer')
personasencola.insertar('Diego')
personasencola.insertar('Luis')
personasencola.insertar('Sofía')

print(personasencola.mostrarColadePersonas())

print(personasencola.primer_persona())    # Jennifer
print(personasencola.ultima_persona())    # Sofía
print(personasencola.cantidad())   # 4

print()

personaout = personasencola.extraer()
print("La primera persona en salir es: " + personaout) # Jennifer
print(personasencola.cantidad()) # 3

print(personasencola.primer_persona())  #Diego
print(personasencola.ultima_persona())  #Sofía
print(personasencola.mostrarColadePersonas())
