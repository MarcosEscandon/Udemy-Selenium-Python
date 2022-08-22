# ecuacion resolvente

from math import sqrt

A = int(input("Ingrese el valor de a: "))
B = int(input("Ingrese el valor de b: "))
C = int(input("Ingrese el valor de c: "))
x1 = 0
x2 = 0

if((B**2)-(4*A*C)) < 0:
    print("No existe la raiz cuadrada de un numero negativo")
else: 
    x1 = (-B+sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B-sqrt((B**2)-(4*A*C)))/(2*A)
    print("La solucion es x1= ",x1,"\nx2=",x2)