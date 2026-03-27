buses = 0
destino = 0 
pasajeros = 0
precio = 0
total_recaudado = 0

buses = int(input("Ingrese el numero de buses: "))
pasajeros = int(input("Ingrese el numero de pasajeros: "))
precio = int(input("Ingrese valor del pasaje: "))
destino = int(input("Ingrese el destino: "))

total_recaudado = pasajeros * precio * buses

print("Usted recaudo un total de: ", total_recaudado)