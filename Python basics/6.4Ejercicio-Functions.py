# Crear lista, pedir al usuario numeros para agregar. Crear listas de pares / impares

from ast import Num


lista=[]
num=0

def pedir():
    i=0
    while i<5:
        num=int(input("Ingrese un numero: "))
        lista.append(num)
        i+=1

def numeros():
    lista.sort()
    pares=[]
    impares=[]
    for i in lista:
        if(i%2 == 0):
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

pedir()
numeros()