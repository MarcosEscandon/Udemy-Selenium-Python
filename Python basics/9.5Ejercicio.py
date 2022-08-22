# tres clases Universidad, atributos nombre, carrera (atr especialidad), estudiante (atr nombre y edad). Objeto persona.

class Universidad():
    def __init__(self,siglas):
        self.siglas=siglas

class Carrera():
    def carrera(self,especialidad):
        self.especialidad=especialidad

class Estudiante(Universidad,Carrera):
    def datos(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        print("Mi nombre es {}, tengo {} años y estudio en la {} en la especialidad de {}".format(self.nombre,self.edad,self.siglas,self.especialidad))

persona=Estudiante("UTN")

persona.carrera("UTN")

persona.datos("Marcos",33)