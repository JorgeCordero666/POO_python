# Tema: Herencia Multiple
'''Esta es una clase HIJA que hereda de FiguraGeometrica y Color'''
from FiguraGeometrica import *
from Color import *

# Definicion de la herencia multiple


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho
