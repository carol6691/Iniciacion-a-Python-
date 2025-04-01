#clase Libro
class Libro():
    # Atributo de clase libros
    libros = []
    #definimos constructor de Libro con sus propiedades/atributos
    def __init__(self, titulo=None, autor=None, ISBN=None, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = disponible
    #definimos metodosx5 de la clase Libro (agregar, prestar, devolver, mostrar, buscar)
    def agregar(self):
        titulo = str(input("Introduce Título:"))
        autor = str(input("Introduce Autor:"))
        try:
            ISBN = int(input("Introduce ISBN:"))
            #creamos una instancia de la clase Libro con los valores ingresados por el usuario (titulo, autor, ISBN)
            nuevo_libro = Libro (titulo, autor, ISBN, True)
            #Acceder al atributo de clase libros a través de la clase Libro usando Libro.libros 
            #Libro.libros.append(nuevo_libro) agrega el nuevo libro (nuevo_libro) a esta lista.
            Libro.libros.append(nuevo_libro)
            #accedemos a los atributos de la instancia nuevo_libro
            print (f"El siguiente libro ha sido agregado al sistema:\n\
                    Titulo: {nuevo_libro.titulo}\n\
                    Autor: {nuevo_libro.autor}\n\
                    ISBN: {nuevo_libro.ISBN}\n\
                    Disponible: {"Si" if nuevo_libro.disponible==True else "No"}")
        #valuerror por si introducen texto en vez de num
        except ValueError:
            print("Introduce un número válido")
    def prestar(self):
        buscarISBN = int(input("Introduce ISBN del libro a prestar:"))
        #Usamos el bucle for para recorrer cada libro en la lista
        for libro in Libro.libros:
            #accedemos al atributo ISBN del libro
            if libro.ISBN == buscarISBN:
                #si coincide, cambiar disponible del libro a False
                libro.disponible = False
                print ("Libro prestado")
            else:
                print ("Libro no encontrado o no disponible")
    def devolver(self):
        buscarISBN = int(input("Introduce ISBN del libro a devolver:"))
        #Usamos el bucle for para recorrer cada libro en la lista
        for libro in Libro.libros:
            #accedemos al atributo ISBN del libro
            if libro.ISBN == buscarISBN:
                #si coincide, cambiar disponible del libro a True
                libro.disponible = True
                print ("Libro devuelto")
            else:
                print ("Libro no encontrado o no disponible")
    def mostrar (self):
        #Usamos el bucle for para recorrer cada libro en la lista
        for libro in Libro.libros:
            #accedemos a los atributo titulo, autor, ISBN y disponible del libro
            print (f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.ISBN}, Disponible: {"Si" if libro.disponible==True else "No"}")
    def buscar(self):
        buscarISBN = int(input("Introduce ISBN del libro a buscar:"))
        #Usamos el bucle for para recorrer cada libro en la lista
        for libro in Libro.libros:
            if libro.ISBN == buscarISBN:
                #si coinciden, mostramos los atributo titulo, autor, ISBN y disponibilidad del libro
                print (f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.ISBN}, Disponible: {"Si" if libro.disponible==True else "No"}")
                break
            else:
                print ("Libro no encontrado o no disponible")
#creamos una instancia de Libro y generamos el menú de gestión de biblioteca
libro = Libro()
while True:
    print("Bienvenido al Sistema de Gestión de Biblioteca:")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro")
    print("6. Salir")
    try:
        elige_opcion = int(input("Elige una opción:"))
        if elige_opcion == 1:
            #Acceder al metodo de clase a través de la instancia libro
            libro.agregar()
        elif elige_opcion == 2:
            libro.prestar()
        elif elige_opcion == 3:
            libro.devolver()
        elif elige_opcion == 4:
            libro.mostrar()
        elif elige_opcion == 5:
            libro.buscar()
        elif elige_opcion == 6:
            print ("Saliendo")
            break
        else:
            print ("Error. Introduce un número del 1 al 6")
    #valuerror por si introducen texto en vez de num
    except ValueError:
        print ("Introduce un número válido")




