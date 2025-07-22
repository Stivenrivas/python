# Pedir dos numeros al musuario y hacer operaciones basicas 
while True:
    try:     
          numero1 = int(input(" Ingrse un numero "))   
          numero2 = int(input(" Ingrse un numero "))
          resutado = 0
          break
    except:
        print(" solo puede usar numeros ")

resutado = numero1 + numero2
print(f" La suma de los  numeros es {resutado}")

resutado = numero1 - numero2
print(f" La resta de los  numeros es {resutado}")

resutado = numero1 * numero2
print(f" La multiplicacion de los  numeros es {resutado}")


if numero2 == 0:
    print("NO HAY DIVISION POR 0")
else:
    resutado = numero1 / numero2
    print(f" La division de los  numeros es {resutado}")

