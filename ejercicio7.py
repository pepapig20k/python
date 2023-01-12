class Clase:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def Promedio(self):
        if self.nota >= 4.5:
            print("La alumna ", self.nombre, "ha aprobado con la nota: ", self.nota)
        else:
            print("La alumna ", self.nombre, "Ha reprobado con la nota: ", self.nota)
c = Clase("Kata_la_Ow0", 5.9)
c.Promedio()

