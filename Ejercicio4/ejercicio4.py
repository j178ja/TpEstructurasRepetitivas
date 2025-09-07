
total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"El total acumulado es: {total}")