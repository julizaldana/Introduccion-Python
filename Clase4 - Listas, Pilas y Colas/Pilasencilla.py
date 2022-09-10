#Lista sencilla de libros (PILA) - trabaja con el termino LIFO 

libros = ['El señor de los anillos','Harry Potter','Don Quijote']

print(libros)

#AGREGAR LIBROS A MI PILA DE LIBROS, .append()

libros.append('El Señor Presidente')
print(libros)

libros.append('100 años de soledad')
print(libros)

#SACAR UN LIBRO DE MI PILA DE LIBROS, .pop()

librofuera = libros.pop()
print("Nombre de libro que saco de mi pila de libros es:  " + librofuera)
print(libros)
