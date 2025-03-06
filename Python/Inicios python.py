print ('Hello World!')
#next
carolina = 'guapa y morena y lista y guapa'
print ('es la mas' , carolina)
#next - funciones
def suma(a, b):
    return a+b
x=suma(1, 3) 
print (x)
#next - funciones y polimorfismo
def suma(a, b):
    return a+b
print (suma(1,4))
print (suma('Me gusta ', 'Python'))
#next - funciones y polimorfismo
def suma():
    num1 = "carolina"
    num2 = "miguel"
    print("suma =", num1 + num2)
suma()
#next - Recursividad
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
print (factorial(1))
#next - Devolviendo múltiples valores 
def tupla(lista):
    return max(lista), min(lista)
print (tupla([1, 3, 5]))
#next - Devolviendo múltiples valores 
def tupla():
    lista=[1, 3, 5]
    print(max(lista), min(lista))
tupla()
#next - Devolviendo múltiples valores
def tupla():
    lista = [1, 3, 5]
    print (lista)
tupla()
#next - ambito global vs ambito local
c='miguel'
print('amo a ', c)

def f():
    c='juan'
    print('odio a', c)
f()

print('amo a ', c)
#next -regla LEGB
A = 'global'
def f1():
    B = 'local f1'
    def f2():
        C = 'local f2'
        D = 'local f2'
        print (A, B, C, D, sep = '\n')
    f2()
f1()
#next -regla LEGB
A = 'global'
def f1():
    B = 'local f1'
    def f2():
        C = 'local f2'
        D = 'local f2'
        print (A, B, C, D, sep = '\n')
    def f3():
        E = 'local f3'
        print (A, B, E, sep = '\n')
    f3()
    f2()
f1()
#next - 
def f():
    a, b, c = (1, 2, 3)
    print (a, b, c)
f()
#next - 
def f(a, b, c):
    print (a, b, c)
f(1, 2, 3)
#next - 
def f():
    a, b, c = (1, 2, 3)
    return a, b, c
print (f())
#next - parametros y argumentos
def suma(a, b):
    return a+b
print (suma(2, 3))
#next - 
def u():
    l = [1, 2, 3, 4, 5]
    l[0] = 100
    return min(l)
print (u())
#next - 
def u(l):
    l[0] = 100
    print (min(l))
u([1, 2, 3, 4][:])
#next - 
def u(l):
    l[0] = 100
    return min(l)
l = [1, 2, 3, 4]
print (l)
print (u(l))
print (l)
#next - 
def u(l):
    l[0] = 100
    return min(l)
l = [1, 2, 3, 4]
print (l)
print (u(l[:]))
print (l)
#next - 
def a(*f):
    print (f)
a(1, 2, 3, 4)
a(1)
#next - 
def a(*f):
    return f
print (a(1, 2, 3, 4))
print (a(1))
#next - 
def a(**f):
    return f
print (a(a = 1, c = 2, b = 3, d = 4))
print (a(a = 1))
#next - 
def a(*a, b, c):
    return a, b, c
print (a(1, c = 3, b = 4))
