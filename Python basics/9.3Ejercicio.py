# Clase -> Fabrica. Atributos -> Llantas, Color y Precio. Clase heredada de F -> Moto y Auto. Metodos -> Muestren q's y precio. Crear objetos.

class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio

class Auto(Fabrica):
    def datos(self):
        print("La catidad de llantas del auto: ",self.llantas)
        print("El color del auto es: ",self.color)
        print("El precio del auto es: $",self.precio)

class Moto(Fabrica):
    def datos(self):
        print("La catidad de llantas de la moto: ",self.llantas)
        print("El color es de la moto: ",self.color)
        print("El precio es de la moto: $",self.precio)

moto=Moto(2,"verde",10000)
moto.datos()

auto=Auto(4,"negro",20000)
auto.datos()