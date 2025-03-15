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
    #definimos constructor de Libro con sus propiedades/atributos
    def __init__(self, titulo, autor, ISBN, disponible):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True
    #definimos metodo agregar un libro a la clase
    def agregar(self):
        lista = []
        print("Introduce Título:")
        for i in range(lista):
            lista.append(str(input))
        print("Título introducido")
        autor = str(input("Introduce Autor:"))
        print("Autor introducido")
        try:
            ISBN = int(input("Introduce ISBN:"))
            print("ISBN introducido")
        except ValueError:
            print("Introduce un número válido")
            ISBN = int(input("Introduce ISBN:"))
        
    def prestar (self):
        self.disponible == False
        print ("Libro prestado")
    def devolver(self):
        self.disponible == True
        print ("Libro disponible")
    def mostrar (self):
        return self.__init__()
    def buscar(self):
        buscarISBM = int(input("Introduce ISBM:"))
        if self.isbm == buscarISBM:
            return self.__init__()
        else:
            print ("No encontrado")
    


    




