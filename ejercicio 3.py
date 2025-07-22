#mostrar todas las tablas de multiplicar del 1 al 10, mostrando el numero de la tabla y luego la multiplicacion del 1 al 10

for tabla in range(1,11):
    print(f"\nTABLA DEL {tabla}")
    for j in range(1,11):
        resultado = j * tabla
        print(f"{j} x {tabla} = {resultado}")