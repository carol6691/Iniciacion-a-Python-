d = {'20904563': 33, 
     '73382456': 61}
texto = input ('Introduce DNI: ')
if texto in d:
    print ("Tu edad es", d[texto])
else:
    while True:
        texto2 = input ('Introduce edad: ')
        if texto2.isnumeric():
            num = int(texto2)
            d[texto]=num
            print ("Anadido")
            break
        else:
            print ("Vuelve a introducir edad")
print (d)