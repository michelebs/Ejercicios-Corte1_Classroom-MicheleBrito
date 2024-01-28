
# CICLOS EJERCICIO 10:

# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número para ver su tabla de multiplicación: "))

# Imprimir la tabla de multiplicación del número ingresado
print(f"Tabla de multiplicación del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

