
suma = 0

print("Ingrese 100 n�meros enteros:")

for i in range(100):
    numero = int(input(f"N�mero {i+1}: "))
    suma += numero

media = suma / 100

print("\nLa media de los 100 n�meros ingresados es:", media)
