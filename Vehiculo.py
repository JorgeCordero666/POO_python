# Tema: Herencia Simple
'''Esta es una clase padre'''


class Vehiculo:

    # Metodo Constructor
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    # Metodo str
    def __str__(self) -> str:
        return f'Vehiculo Color: {self.color} y Numero de ruedas: {str(self.ruedas)}'
# Para comprobar si esta correcto se crearon objetos de las respectivas clases hijas
