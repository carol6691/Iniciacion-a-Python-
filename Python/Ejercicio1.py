texto = input ('Introduce texto: ')
print (type(texto))
l = list()
if texto.isnumeric():
    num = int (texto)
    l.append (num)
    print ("numero", num, "ha sido anadido")
else:
    print ("no ha sido anadido")
    