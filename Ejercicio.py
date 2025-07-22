# Pedir dos numeros al musuario y hacer operaciones basicas 

#aqui le pedimos los numero al usuario  y nos aseguramos que solo pueda entrar numeros
while True:
    try:     
          numero1 = int(input(" Ingrse un numero "))
   
          numero2 = int(input(" Ingrse un numero "))
          resutado = 0
          break
    except:
        print(" solo puede usar numeros ")

#aqui mostramos el resultado de la suma
resutado = numero1 + numero2
print(f" La suma de los  numeros es {resutado}")

#aqui mostramos el resultado de la resta
resutado = numero1 - numero2
print(f" La resta de los  numeros es {resutado}")

#aqui mostramos el resultado de la multiplicacion
resutado = numero1 * numero2
print(f" La multiplicacion de los  numeros es {resutado}")

#aqui mostramos el resultado de la divicion y si el segundo numero es 0 no hace nada
if numero2 == 0:
    print("NO HAY DIVISION POR 0")
else:
    resutado = numero1 / numero2
    print(f" La division de los  numeros es {resutado}")
