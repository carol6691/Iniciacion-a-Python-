numero = 50
contador = 0
n = int(input("introduce numero:"))
while n!= numero:
    if n<numero:
        print ("el numero introducido es muy pequeno")
    elif n>numero:
        print ("el numero introducido es muy alto")
    n = int(input("introduce numero:"))
    contador+=1
print ("HAS ACERTADO!")
print ("Numero de intentos:", contador)
#next
