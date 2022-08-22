# clase Alumno, atributos nombre y nota. Metodo para init atributos, imprimirlos y mostrar resultado

class Alumno():
    def datos(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def resultado(self):
        if self.nota < 6:
            print("Desaprobaste crack")
        else: 
            print("Aprobaste crack")

alumno1=Alumno()
alumno1.datos("Marcos",8)

alumno2=Alumno()
alumno2.datos("Nano",5)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()