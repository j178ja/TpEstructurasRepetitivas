valor1=int(input("Ingrese el primer valor: "))
valor2=int(input("Ingrese el segundo valor: "))


inicio = min(valor1, valor2) + 1
fin = max(valor1, valor2)

suma = 0
for i in range(inicio, fin):
    suma += i

print(f"La suma de los numeros enteros entre {valor1} y {valor2} (excluyendolos) es: {suma}")
