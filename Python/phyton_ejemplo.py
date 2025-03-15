# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.
#lista = []
#num_libros = int(input("Cuantos libros quieres incluir?"))
#for i in range(num_libros):
#    titulo = input(f"Ingresa el título {i + 1}: ")
#    autor = input(f"Ingresa el autor {i + 1}: ")
#    ISBN = input(f"Ingresa el ISBN {i + 1}: ")
#    lista.append(titulo)
#    lista.append(autor)
#    lista.append(ISBN)
#print(lista)
#    
libros = []
titulo = str(input("Introduce Título:"))
autor = str(input("Introduce Autor:"))
while True:
    try:
        ISBN = int(input("Introduce ISBN:"))
        break
    except ValueError:
        print("Introduce un número válido")

print (f'Título: {titulo}, Autor: {autor},ISBN: {ISBN}')
nuevo_libro = Libro.agregar()
libros.append(nuevo_libro)

#notaIn=int(input("Introduzca nota:"))
#if notaIn<5:
#    calificacion="Suspenso"
#else:
#    calificacion="Aprobado"
#print(calificacion)
#print(calificacion)
