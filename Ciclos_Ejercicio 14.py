
# CICLOS EJERCICIO 14:

total = 0
while True:
    numero = int(input("Ingrese un número entero positivo (o un número negativo para terminar): "))
    if numero < 0:
        break
    total += numero

print(f"La suma total de los números positivos ingresados es: {total}")
