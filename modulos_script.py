class Juguete:
    nombre = ''
    precio = 0.0
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Mi nombre es {self.nombre} y mi precio es {self.precio}"

pep = Juguete('Roberto', 19.990)

print(pep)