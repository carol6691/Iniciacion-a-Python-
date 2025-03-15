class Coche():
    def __init__(self):
        self.largo = 200
        self.ancho = 100
        self.ruedas = 4
        self.color = "rojo"
        self.is_enMarcha = False
    def arrancar (self):
        self.is_enMarcha = True
    def estado (self):
        if (self.is_enMarcha == True):
            return "el coche esta arrancado"
        else:
            return "el coche esta parado"
Opel = Coche()
Kia = Coche()
print ("el largo es", Opel.largo, "cm")
print (Opel.estado())
Opel.arrancar()
print (Opel.estado())
Opel.ruedas = 5
Kia.ruedas = 6
print ("opel tiene", Opel.ruedas, "ruedas")
print ("kia tiene", Kia.ruedas, "ruedas")
def __del__(self):
        print("xx")
#next
class Coche():
    def __init__(self, largo, ancho, ruedas, color, is_enMarcha):
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.color = color
        self.is_enMarcha = is_enMarcha
coche1 = Coche(400, 200, 4, "verde", True)
coche2 = Coche (100, 200, 5, "rojo", False)
del coche1
print (coche2.ruedas)
print (coche2.ruedas)
#next - EJERCICIO
class Usuario():
    def __init__(self):
        self.nombre = "Carolina"
        self.edad = 33
        self.login = "clliberos"
        self.password = "secret"
        self.email = "carol@gmail.com"
        self.telefono = 697954567
    def Resumen(self):
        print ("los datos del ususario son:\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Login: {self.login}\n"
            f"Password: {self.password}\n"
            f"Email: {self.email}\n"
            f"Telefono: {self.telefono}") 
    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce tu edad"))
        if 100>edadIntroducida>0:
            self.edad = edadIntroducida
            print ("edad correcta")
        else:
            print ("introduce de nuevo edad")
            edadIntroducida = int(input("Introduce tu edad"))
    def muestraEdad(self):
        return (self.edad)
    
administrador = Usuario()
print (administrador.muestraEdad())
print ("edad:", administrador.muestraEdad())
administrador.email = "cambiado"
print ("email new:", administrador.email)

class Bici (Usuario):
    is_carenado = 79
miBici = Bici()
print (miBici.is_carenado)

class Moto(Usuario):
    pass
miMoto = Moto()
print (miMoto.muestraEdad())
class Kwas(Usuario):
    pass
    def cilindrada(self):
        self.cilindrada = 3000
    def muestraEdad(self):
        return (self.edad, self.edad, self.cilindrada)
mikwas = Kwas()
print (mikwas.muestraEdad())
#next
class Padre():
    def __init__(self, ojos, cejas):
        self._ojos = ojos
        self._cejas = cejas
class Hijo(Padre):
    def __init__(self, ojos, cejas, cara):
        super().__init__(ojos, cejas)
        self.cara = cara
Tomas = Hijo ('Marrones', 'Negras', 'Redonda')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)



