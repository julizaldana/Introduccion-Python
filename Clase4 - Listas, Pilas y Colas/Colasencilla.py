#Lista sencilla, documentos a imprimir (COLA) -> Cola de Impresión, FIFO

colaimp = []

#Agregar un documento para imprimir, usando .append()

colaimp.append('Documento1')
print(colaimp)
colaimp.append('Documento2')
print(colaimp)
colaimp.append('Documento3')
print(colaimp)

#Sacando documentos de la cola, con .pop(0)

docimpreso = colaimp.pop(0)
print("El documento que sale de la cola y será impreso es: " + docimpreso)
print("La nueva cola de impresión es:" )
print(colaimp)