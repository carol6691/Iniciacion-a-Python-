#Opciones = (1.Agregar Libro, 2.Prestar Libro, 3.Devolver Libro, 
#            4.Mostrar Libros, 5.Buscar, 6.Salir)
#print ("Bienvenido al Sistema de Gestión de Biblioteca", Opciones)
#print (input("Elige una opción:"))
#if 1 
#class Opciones:
#lista = ["carol", "miguel", "aaron"]
#print ((enumerate(lista)))
#next
class Libro():
    def __init__(self):
        self.titulo = "El caso Henry Quevert"
        self.autor = 124
        self.isbm = 123
        self.disponible = True
    def agregar(self):
        #habia una forma de introducir multiples valores 
        # a la vez? tema de intro a python final
        titulo_nuevoLibro = input("Introduce un nuevo libro:"\n
                           "Título: ")
    def prestar (self):
        self.disponible == False
        print ("Libro no disponible")
    def devolver(self):
        self.disponible == True:
        print ("Libro disponible")
    def mostrar (self):
        return self.__init__()
    def buscar(self):
        buscarISBM = int(input("Introduce ISBM:"))
        if self.isbm == buscarISBM:
            return self.__init__()
        else:
            print ("No encontrado")
    


    




