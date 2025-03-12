a, b = (3, 4)
print (a, b)
#next - 
t = [(1, 3), (2, 4)]
for a, b in t:
    print (a + b)
#next - 
t = [(1, 3), (2, 4)]
for a, b in t:
    print (a + b)
#next - 
t = [(1, 7), (2, 4)]
u = [(11, 5), (3, 2)]
for a, b in t + u:
    print (max(a, b), end = ' ')
#next - 
t = [(1, 7), (3, 0)]
u = [(11, 5), (3, 2)]
for a, b in t + u:
    print (max(a, b), end = ' ')
#next - 
t = [(1, 3), (4, 0)]
u = [(11, 5), (3, 2)]
for (a1, a2), (b1, b2) in zip (t, u):
    print (max(a1, b1), max(a2, b2))
#next - 
t = (1, 3, 4, 0)
u = (11, 5, 3, 2)
for a, b in zip (t, u):
    print (max(a, b), end = ' ')
print()
#next - 
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values)) 
for k, v in d.items():
    print('{}: {}'.format(k, v))
for k in d.keys():
    print(k, end=' ')
print()
for v in d.values():
    print(v, end=' ')
print()
#next - 
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values)) 
print (list (d.keys())[1])
#next - 
import random
letras = list('abcdef')
vocales = 'aeiou'
random.shuffle(letras)
print(''.join(letras))
#next - 
letras = list('abcdefgh')
vocales = 'aeiou'
print (list(enumerate(letras)))
#next - 
letras = list('abcdefgh')
for x in letras:
    print (x, end=', ')
    print()
#next - 
fichero = """\
bello
guapo
tonto es tonto
"""
f=open('texto.txt', 'w')
f.write(fichero)
f.close()
f=open('texto.txt', 'r')
print (next(f))
print (next(f))
print (next(f))
#next - 
lista = [1, 2, 3]
li = iter(lista)
print (next(li))
print (next(li))
print (next(li))
#next - 
class Repetidor:
    def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0
    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration
        self.counter +=1
        return self.item
    def __iter__(self):
        return self
rep = Repetidor (3, 'hola', )
for linea in rep:
        print(linea, end=' ')
print()
#next - 
miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
    print(x)
#next - 
peliculas = {"Love Actually":"Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
    print(peliculas[x])
#next - 
import random
dir (random)
#next
#lista = ["carol", "miguel"]
#print (list(enumerate(lista, start=1), f"{indice}: {valor}", end=' '))
#next
#num = int(input('Introduce un número: '))
#add = num+1
#print (add)
#next
#a, b, c = map(int, input("Introduzca 3 números: ").split())
#print ("Los números son:", a, b, c, end = " ")
#print()
#print ("Gracias")
#next
#mi_set = set()
#s = int(input("Introduzca el tamaño del set: "))
#print("Introduzca los elementos del set:")
#for i in range(s):
#    mi_set.add(int(input()))
#print(mi_set)
#next
#numeros = list(map(int, input("Introduzca X números: ").split()))
#print ("Los números son:", numeros, end = " ")
#print()
#next
#numeros = set(map(int, input("Introduzca X números: ").split()))
#print ("Los números son:", numeros, end = " ")
#print()
#next
#mi_tupla = (1, 2, 3)
#mi_lista = list(mi_tupla)
#mi_lista.append(int(input("Introduzca los elementos de la tupla:")))
#mi_tupla = tuple(mi_lista)
#print(mi_tupla)
#next
#t = int(input("Introduzca el tamaño de la tupla: ")) 
#mi_lista = []
#for i in range(t):
 #   mi_lista.append(int(input("Introduzca los elementos de la tupla:")))
#mi_tupla = tuple(mi_lista)
#print(mi_tupla)
#next
print ("G, H, I")
print("GHI", end = ':')
print()
print ("G", "H", "I", sep = "@")
#next
n = "Carolina"
print ("Hola", n ,". Que tal")
#next
n = "Carolina"
print (f"Hola {n}. Que tal")
#next
a = 1
b = -2
sum = a/b
print ("la suma es %f" %sum)
#next
def indexador(objeto, indice):
    return objeto [indice]
print (indexador('carolina', 0))
#next
def indexador(objeto, indice):
    return objeto [indice]
try:
    indexador('carolina', 10)
except IndexError: 
    print ("indice muy grande")
#next
def indexador(objeto, indice):
    return objeto [indice]
try:
    indexador('carolina', hola)
except IndexError: 
    print ("indice muy alto")
except NameError: 
    print ("error en el indice")
print ("FIN")
#next
z = 5
u = 2
assert (z>u), 'assert error'
print("el assert no se ha ejecutado")
#next
z = 5
u = 4
assert (z>u), 'assert error'
print("el assert no se ha ejecutado")
#next
#class mipropiaexcepcion (Exception):
#    pass
#try:
#    raise mipropiaexcepcion
#except mipropiaexcepcion:
#    print ("todo ok")
#next
#class mipropiaexcepcion (Exception):
#    def __init__(self, valor):
#        self.valor = valor
#    def __str__(self):
#        return str(self.valor)
#raise (mipropiaexcepcion("errorcito"))
#next
def indexador(objeto, indice):
    return objeto [indice]
try:
    indexador('carolina', 1)
    print("no se ejecuta")
except IndexError:
    print ("capturamos error")
else:
    print ("perfecto")
finally:
    print("se imprime haya o no excepcion")
print ("hola")

