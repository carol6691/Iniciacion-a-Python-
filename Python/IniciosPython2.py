n_edad = 47
s_edad = "47"
print (n_edad)
print (s_edad)
print ('hola ' + str(n_edad))
print (33 + int(s_edad))
print (33.5 + float(s_edad))
print(type(n_edad))
print(type(s_edad))
''' next
next'''
A = 13
B = "14"
print (str(A))
print (float(A))
print (int(B))
print (float(B))
#next
print("Esta frase","termina aquí.")
print("Esta frase"+"termina aquí.")
#next
a = "uno"
b = "dos"
c = a + b
print (c)
c = a * 3
print (c)
#next
texto = "HOLA"
print (texto.lower())
#next
texto = "hola"
print (texto.capitalize())
#next
texto = "hola"
print (texto.count('o'))
#next
texto = "amor"
print (texto.find('a'))
#next
texto = "loco"
print (texto.find('o'))
#next
texto = "texto"
print (texto.find('t'))
#next
texto = "texto"
print (texto.rfind('t'))
#next
texto = "texto"
print (texto.isdigit())
#next
texto = "5"
print (texto.isdigit())
#next
texto = "5.5"
print (texto.isdigit())
#next
texto = "texto5"
print (texto.isdigit())
#next
texto = "texto"
print (texto.isalpha())
#next
texto = "texto5"
print (texto.isalpha())
#next
texto = "5.5"
print (texto.isalpha())
#next
texto = "  texto de hola "
print (texto.strip())
#next
texto = "texto de hola"
print (texto.replace("hola", "amor"))
#next

#next
n_numero2 = 34
n_numero3 = 34
n_numero2 != n_numero3
#next
n_numero2 = 34
n_numero3 = 35
n_numero2 != n_numero3
#next
n_numero6 = 34
n_numero6 += 1
n_numero6 = n_numero6 + 2
print(n_numero6)
#next
a = True
b = False
resultado = a and b
print (resultado)
#next
a = True
b = False
resultado = a or b
print (resultado)
#next
a = True
b = False
resultado = not b
print (resultado)
#next
a = (1, 2, 3, 4, 5)
print("La dirección de memoria es" , id(a))
#next
a = 65
print("La dirección de memoria es" , id(a))
#next
d = {'carolina': 33, 
     'juan': 61}
for k in d:
    info = '{}: {}'.format(k, d[k])
    print (info)
    
    
