# Tema: Herencia Simple
'''Esta es una clase hija que hereda de Vehiculo'''
from Vehiculo import *


class Coche(Vehiculo):
    # Metodo Constructor
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    # Metodo str

    def __str__(self) -> str:
        return f'{super().__str__()} y la velocidad del coche es: {str(self.velocidad)}'


# Para comprobar si esta correcto se crearon objetos de las respectivas clases hijas
coche1 = Coche('Rojo', 4, 40)
print(coche1)
