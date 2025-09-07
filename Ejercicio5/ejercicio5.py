import random

# Generar un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

valor=int(input("Ingrese un valor entre 0 y 9 : "))

while valor != numero_aleatorio:
    if valor < 0 or valor > 9:
        print("El valor ingresado no es correcto.")
    else:
        print("Incorrecto, intenta de nuevo.")

        #pedir nuevamente el valor
    valor=int(input("Ingrese un valor entre 0 y 9 : "))

    # CUANDO ACIERTA
    if valor==numero_aleatorio:
        print("Felicidades, adivinaste el numero")
        break