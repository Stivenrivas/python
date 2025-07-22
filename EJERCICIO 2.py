#hacer un programa que muestre los numeros enre dos numeros

#aqui le pedimos los numeros al usuarios ingresdo dos numeros y nos aseguramos que solo se puede ingresar numeros
while True:
    try:
        numero1 = int(input(" ingrese el primer numero"))
        numero2 = int(input(" ingrese el segundo numero"))
        break
    except:
        print("solo puede escribir numero")
i = 0

#aqui comparamos los dos numero para que la lista empice siempre con el mernor  y mostramos la lista
if numero1 < numero2:
    for i in range(numero1+1, numero2):
        print(i)
else:
    for i in range(numero2+1, numero1):
         print(i)
