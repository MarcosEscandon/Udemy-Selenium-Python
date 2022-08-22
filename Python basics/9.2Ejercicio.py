# Declarar dos enteros usando __init__ Calcular suma, resta, multip y div. Usando 1 metodo para imprimir cada una

class Calculadora():
    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))

    def suma(self):
        self.suma = self.valor1 + self.valor2
        print("La suma es de: ",self.suma)
    
    def resta(self):
        self.resta = self.valor1 - self.valor2
        print("La resta es de: ",self.resta)

    def multip(self):
        self.multip = self.valor1 * self.valor2
        print("La multip es de: ",self.multip)

    def div(self):
        self.div = self.valor1 / self.valor2
        print("La div es de: ",self.div)

calcular = Calculadora()
calcular.suma()
calcular.resta()
calcular.multip()
calcular.div()