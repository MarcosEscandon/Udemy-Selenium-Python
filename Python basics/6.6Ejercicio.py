# Crea un programa con dos funciones, una area de cuadrado y otra area de una circunferencia

from cmath import pi


def area_cuadrado(base,altura):
    return base*altura

print(area_cuadrado(10,5))

def area_circunf(radio):
    return (radio**2)*pi

print(area_circunf(2))
