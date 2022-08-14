# Tema: Herencia Multiple
'''Esta es una clase padre'''


class Color:
    def __init__(self, color):
        self._color = color

    @property
    # Metodo get color
    def getColor(self):
        return self._color

    # Metodo set color
    @getColor.setter
    def setColor(self, color):
        self._color = color

    def __str__(self):
        return f'Color [color: {self._color}]'
