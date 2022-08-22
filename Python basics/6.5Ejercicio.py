# pedir 2 numeros, si el 1ero es mayor retorna 1, si es a la inversa -1, si son iguales 0

def numeros():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    if (num1>num2):
        return 1
    elif(num2>num1):
        return -1
    else:
        return 0

print(numeros())