
# LISTAS EJERCICIO 19:

# Crear la lista de notas de los estudiantes
notas = [75, 80, 90, 60, 85, 95, 70, 55, 65, 72, 88, 92, 78, 68, 73, 81, 79, 83, 87, 91,
         76, 89, 62, 84, 77, 66, 74, 82, 86, 94, 71, 58, 69, 93, 67, 61, 59, 63, 64,
         90, 85, 78, 92, 87, 83, 79, 91, 88, 82, 84, 89, 86, 81, 77, 93, 80, 75, 94,
         76, 95, 73, 72, 74, 71, 68, 70, 69, 67, 66, 65, 62, 63, 64, 60, 58, 61, 59,
         55]

# Calcular el promedio de notas
promedio = sum(notas) / len(notas)

# Contar cuántos alumnos aprobaron y reprobaron
aprobados = len([nota for nota in notas if nota >= 70])
reprobados = len([nota for nota in notas if nota < 70])

# Mostrar los resultados
print(f"El promedio de notas del salón es: {promedio}")
print(f"El número de alumnos que aprobaron es: {aprobados}")
print(f"El número de alumnos que reprobaron es: {reprobados}")
