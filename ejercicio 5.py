#Hacer un programa que pida numeros al usuario hasta que ingrese 111

while True:

    numero = int(input(" Ingrese un numero"))
    
    if numero != 111:
        if 111 > numero:
            print("\n el numero es mayor")
        elif 111 < numero:
            print("\n el numero en menor")
    else:
        print("Programa finalizado")
        break
