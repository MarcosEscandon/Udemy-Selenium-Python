# Imprimir los numeros del 1 al 10, pedir al usuario 2 numeros y mostrar los numeros entre esos

for i in range(1,11):
    print(i)

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

for i in range(numero1, numero2+1):
    print(i)