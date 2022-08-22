# pedir un numero y mostrar tabla de multiplicacion
numero = int(input("Ingrese un numero: "))
i = 0
multi = 0

while i <= 10:
    multi = numero * i
    print("{} x {} = {}".format(numero,i,multi))
    i += 1