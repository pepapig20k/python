import pickle
class Vehículo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
automotora = Vehículo("Audi", "e-tron", 2022)

auto = open("automotora", "wb")

pickle.dump(automotora ,auto)

auto = open("automotora","rb")

automotora = pickle.load(auto)
auto.close()