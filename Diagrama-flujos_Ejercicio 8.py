
# DIAGRAMA DE FLUJOS EJERCICIO 8:

def calcular_vuelto(precio, pago):
    vuelto = pago - precio
    denominaciones = [20, 10, 5, 2, 1]
    cantidad_billetes = []

    for denominacion in denominaciones:
        cantidad = vuelto // denominacion
        cantidad_billetes.append(cantidad)
        vuelto -= cantidad * denominacion

    return cantidad_billetes

precio = float(input("Ingrese el precio: "))
pago = float(input("Ingrese el monto pagado: "))

vuelto_billetes = calcular_vuelto(precio, pago)
denominaciones = [20, 10, 5, 2, 1]

for i in range(len(denominaciones)):
    print(f"Billetes de ${denominaciones[i]}: {vuelto_billetes[i]}")

    