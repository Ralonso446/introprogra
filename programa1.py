cajas = 0
mause = 0
precio = 0
total_cancelar = 0

cajas = int(input("Ingrese el numero total de cajas: "))
mause = int(input("Ingrese la cantidad de mauses: "))
precio = int(input("Ingrese el precio unitario: "))

total_cancelar = cajas * mause * precio

print("Usted debe cancelar un total de: ", total_cancelar)
