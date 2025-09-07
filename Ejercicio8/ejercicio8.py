
# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingrese 100 números enteros:")

for i in range(100):
    numero = int(input(f"Número {i+1}: "))

    # Par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo, negativo o cero
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # Si es 0, no se suma ni a positivos ni a negativos

# Resultados
print("\nResultados:")
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
