
# CICLOS EJERCICIO 11:

def suma_pares_menores(num):
    suma = 0
    for i in range(num):
        if i % 2 == 0:
            suma += i
    return suma

numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_pares_menores(numero)
print(f"La suma de todos los números pares menores que {numero} es: {resultado}")

