# Tema: Herencia Simple
'''Esta clase es hija y hereda de '''
from Vehiculo import *


class Bicicleta(Vehiculo):

    # Metodo Constructor
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    # Metodo str
    def __str__(self):
        return f'{super().__str__()} y el tipo de bicicleta es: {self.tipo}'

# Para comprobar si esta correcto se crearon objetos de las respectivas clases hijas


bicicleta1 = Bicicleta('Verde', 2, 'BMX')
print(bicicleta1)
