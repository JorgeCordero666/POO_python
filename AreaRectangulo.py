# Tema: Ejercicio de utilizacion de clases y atributos de la clase
class Rectangulo:
    '''
    Calcular el area  de un rectangulo utilizando clases, objetos y metodos. 
    '''

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # Metodo para calcular el area de un rectangulo

    def calcularArea(self):
        area = self.base * self.altura
        return area


print("Programa para calcular el area un rectangulo")
h = float(input("Ingrese la altura del rectangulo: "))
b = float(input('Ingrese la base del rectangulo: '))
rectangulo1 = Rectangulo(b, h)
print(f"El area del rectangulo es: {rectangulo1.calcularArea():.2f}")
