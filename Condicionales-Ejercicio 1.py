# EJERCICIOS CONDICIONALES #1

# Pedir al usuario que ingrese un número flotante
numero = float(input("Por favor, ingresa un número flotante: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    par_impar = "par"
else:
    par_impar = "impar"

# Verificar si el número es positivo o negativo
if numero > 0:
    pos_neg = "positivo"
elif numero < 0:
    pos_neg = "negativo"
else:
    pos_neg = "cero"

# Imprimir el mensaje con el resultado
print(f"El número: {numero} es {par_impar} y {pos_neg}.")
