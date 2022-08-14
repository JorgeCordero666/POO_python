from Cuadrado import *

cuadrado1 = Cuadrado(5, "Rojo")
print(f'Calculo del area: {cuadrado1.calcularArea()}')
print(cuadrado1)

# Metodo mro- Method Resolution Order --> Permite conocer la jerarquia de clases de la clase que mandamos a llamar
print(Cuadrado.mro())
