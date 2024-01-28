
# DIAGRAMA DE FLUJOS EJERCICIO 7:

def calcular_tarifa(distancia):
    if distancia <= 200:
        tarifa = 5
    else:
        tramos_adicionales = (distancia - 200) / 200
        tarifa = 5 + (2 * tramos_adicionales)
        if tarifa > 19:
            tarifa = 19
    return tarifa

distancia_viajada = float(input("Ingrese la distancia viajada en metros: "))
costo_viaje = calcular_tarifa(distancia_viajada)
print(f"El costo del viaje es: ${costo_viaje:.2f}")

