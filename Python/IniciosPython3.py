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
#
lista = ["carol", "miguel"]
print (list(enumerate(lista, start=1), f"{indice}: {valor}", end=' '))


