#Opciones = (1.Agregar Libro, 2.Prestar Libro, 3.Devolver Libro, 
#            4.Mostrar Libros, 5.Buscar, 6.Salir)
#print ("Bienvenido al Sistema de Gestión de Biblioteca", Opciones)
#print (input("Elige una opción:"))
#if 1 
#class Opciones:
#lista = ["carol", "miguel", "aaron"]
#print ((enumerate(lista)))
#clase Libro
class Libro():
    libros = []
    #definimos constructor de Libro con sus propiedades/atributos
    def __init__(self, titulo, autor, ISBN, disponible):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True
    #definimos metodo agregar un libro a la clase
    def agregar(self):
        titulo = str(input("Introduce Título:"))
        autor = str(input("Introduce Autor:"))
        try:
            ISBN = int(input("Introduce ISBN:"))
        except ValueError:
            print("Introduce un número válido")
            ISBN = int(input("Introduce ISBN:"))
        return f'Título: {self.titulo}, Autor: {self.autor},ISBN: {self.ISBN}'
        nuevo_libro = {"titulo:", titulo, " autor:", autor, "ISBN:", ISBN}
        libros.append(nuevo_libro)
        for libro in libros:
            print (f"Título: {libro['titulo']}, Autor: {libro['autor']}, ISBN: {libro['ISBN']}")
    def prestar (self):
        self.disponible == False
        print ("Libro prestado")
    def devolver(self):
        self.disponible == True
        print ("Libro disponible")
    def mostrar (self):
        for libro in libros:
            print (f"Título: {libro['titulo']}, Autor: {libro['autor']}, ISBN: {libro['ISBN']}")
    def buscar(self):
        buscarISBN = int(input("Introduce ISBN:"))
        if self.ISBN == buscarISBN:
            return f"Título: {libro['titulo']}, Autor: {libro['autor']}, ISBN: {libro['ISBN']}"
        else:
            print ("No encontrado")

nuevo_libro = Libro(titulo, autor, ISBN)



    
    




