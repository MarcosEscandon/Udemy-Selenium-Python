# Crear clase Marino, metodo hablar. Clase heredada Pulpo. Clase heredada Foca, nuevo atributo

class Marino():
    def hablar(self):
        print("Hola ARGH")

class Pulpo(Marino):
    #pass
    def hablar(self):
        print("Soy un pulpo UEQWRWFDS")

class Foca(Marino):
    #pass
    def hablar(self, mensaje):
        self.mensaje=mensaje
        print(self.mensaje)

marino=Marino()
marino.hablar()

pulpo=Pulpo()
pulpo.hablar()

foca=Foca()
foca.hablar("Hola, soy una foca AUAU")