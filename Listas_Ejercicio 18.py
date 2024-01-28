
# LISTAS EJERCICIO 18:

def encontrar_segundo_menor(secuencia):
    # Eliminar duplicados y ordenar la secuencia
    secuencia_ordenada = sorted(set(secuencia))
    
    # Si hay al menos dos elementos únicos, retornar el segundo
    if len(secuencia_ordenada) >= 2:
        return secuencia_ordenada[1]
    else:
        return "No se encontró un segundo menor, la secuencia tiene menos de dos elementos únicos"

# Ejemplo de uso
secuencia = [5, 2, 8, 3, 9, 5, 6]
print("La secuencia es:", secuencia)
print("El segundo menor es:", encontrar_segundo_menor(secuencia))
