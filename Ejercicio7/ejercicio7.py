
# Pedir n�mero al usuario
n = int(input("Ingrese un n�mero entero positivo: "))

suma = 0
for i in range(0, n + 1):  
    suma += i

print("La suma de los n�meros entre 0 y", n, "es:", suma)
