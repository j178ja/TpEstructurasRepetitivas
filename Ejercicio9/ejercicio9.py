
suma = 0

print("Ingrese 100 números enteros:")

for i in range(100):
    numero = int(input(f"Número {i+1}: "))
    suma += numero

media = suma / 100

print("\nLa media de los 100 números ingresados es:", media)
