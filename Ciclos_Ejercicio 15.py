
# CICLOS EJERCICIO 15:

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

numero = int(input("Ingresa un número: "))
resultado = fizz_buzz(numero)
print(resultado)

