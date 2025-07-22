#hacer un programa que muestre los numeros enre dos numeros

numero1 = int(input(" ingrese un numero"))

numero2 = int(input(" ingrese un numero"))
i = 0

if numero1 < numero2:
    for i in range(numero1+1, numero2):
        print(i)
else:
    for i in range(numero2+1, numero1):
         print(i)