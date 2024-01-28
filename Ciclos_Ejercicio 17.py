
# CICLOS EJERCICIO 17:

def voltear_cifras(numero):
    numero_str = str(numero)
    numero_volteado = int(numero_str[::-1])
    return numero_volteado

# Ejemplo de uso
numero = 456
numero_volteado = voltear_cifras(numero)
print(numero_volteado)  # Esto imprimirá 654
