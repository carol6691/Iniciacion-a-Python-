numero = 50
n = int(input("introduce numero:"))
while n!= numero:
    if n<numero:
        print ("el numero introducido es muy pequeno")
        n = int(input("introduce numero:"))
    elif n>numero:
        print ("el numero introducido es muy alto")
        n = int(input("introduce numero:"))
print ("HAS ACERTADO!")
#next

