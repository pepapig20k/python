class Vehiculo:
    def __init__(self, Color, Ruedas, Puertas):
        self.Color = Color
        self.Rueda = Ruedas
        self.Puertas = Puertas

    def imprimir1(self):
        print(self.Color, self.Rueda, self.Puertas)

class Coche(Vehiculo):
    def __init__(self, Color, Ruedas, Puertas, Velocidad, Cilindrada):
        super().__init__(Color, Ruedas, Puertas)
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
    
    def imprimir2(self):
        print("El terreneitor 3000 del chino ", self.Color, self.Rueda, self.Puertas, self.Velocidad, self.Cilindrada)

p = Coche("Amarillo", 4, 4, 120, 1900)

p.imprimir2()

