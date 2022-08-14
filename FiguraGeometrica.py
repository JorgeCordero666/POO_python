# Tema: Herencia Multiple
'''Esta es una clase padre'''


class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def getAncho(self):
        return self._ancho

    @getAncho.setter
    def setAncho(self, ancho):
        self._ancho = ancho

    @property
    def getAlto(self):
        return self._alto

    @getAlto.setter
    def setAlto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'Figura Geometrica: su ancho es: {self._ancho} y su alto es: {self._alto}'
