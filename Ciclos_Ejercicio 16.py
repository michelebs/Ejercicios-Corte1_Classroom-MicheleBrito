
# CICLOS EJERCICIO 16:

def suma_elementos(a, b):
    suma = 0
    for i in range(a, b + 1):
        if i % 2 == 0 and i % 3 == 0:
            suma += i
    return suma

# Ejemplo de uso
a = 1
b = 10
resultado = suma_elementos(a, b)
print(f"La suma de los elementos pares y múltiplos de tres entre {a} y {b} es: {resultado}")
