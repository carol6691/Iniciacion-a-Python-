#EJERCICIO 1a
def f(a, b):
    a = 2
    b = 4
    return (min(a, b))
print (f(2, 4))
#EJERCICIO 1b
def f(a, b):
    a = -1
    b = -4
    return (min(a, b))
print (f(-1, -4))
#EJERCICIO 2
str = "codigo de practica"
palabrasindividuales = str.split()
palabrasinvertidas = palabrasindividuales[::-1]
strinvertida = " ".join(palabrasinvertidas)
print (strinvertida)
#EJERCICIO 3
tupla = (1, 2, 3)
print(sum(tupla))
#EJERCICIO 4

#EJERCICIO 5
import random
x = ['carolina', 'cuchi', 'aaron']
random.shuffle(x)
print(' '.join(x))
#EJERCICIO 6
x1 = ["AvhrurjDKFNFJRMD"]
contador = 0
for word in x1:
    for letra in word:
        if letra.isupper():
            contador +=1
print (contador)
#EJERCICIO 7
lista1 = [4, 6, 8, 1, 0, 3]
print (lista1[-1])
#EJERCICIO 8
#EJERCICIO 9
#EJERCICIO 10
a=input('introduzca numero: ')
b=a[::-1]
if a == b:
    print ("el numero es capicula")
else:
    print ("no es capicupa")
#EJERCICIO
edad = 20
if edad >= 18:
    print ("f")
else:
    print ("no")