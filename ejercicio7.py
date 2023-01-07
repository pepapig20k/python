class Clase:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def Promedio(self):
        print(self.nombre, self.nota)

        if self.nota >= 4.5:
            print("Ha Aprobado ")
        else:
            print("Ha Reprobado ")
c = Clase("Kata_la_Ow0", 3.9)
c.Promedio()

