class Dino:      # clases dinamicas
    _encendido = True

    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False
    def isEncendido(self):
        return self._encendido;

# para ocupar un constructor es = __init__