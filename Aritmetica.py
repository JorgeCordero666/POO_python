
# Tema: Ejercicio de aplicacion de creacion de metodos y objetos
class Aritmetica:
    '''
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc 
    '''
    # Metodo Constructor

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Metodo sumar

    def sumar(self):
        suma = self.operandoA + self.operandoB
        return suma
    # Metodo restar

    def restar(self):
        resta = self.operandoA - self.operandoB
        return resta
    # Metodo multiplicar

    def multiplicar(self):
        multiplicar = self.operandoA * self.operandoB
        return multiplicar
    # Metodo dividir

    def dividir(self):
        if (self.operandoB == 0):
            print("La division para cero no es permitida")
        else:
            return self.operandoA / self.operandoB


print("CALCULADORA ARITMETICA BASICA".center(30, '*'))
operandoA = float(input('Ingrese un valor: '))
operandoB = float(input('Ingrese otro valor: '))
aritmetica1 = Aritmetica(operandoA, operandoB)
print(f' la suma de {operandoA} y {operandoB} es {aritmetica1.sumar()}')
print(f' la resta de {operandoA} y {operandoB} es {aritmetica1.restar()}')
print(
    f' la multiplicacion de {operandoA} y {operandoB} es {aritmetica1.multiplicar()}')
print(
    f' la division de {operandoA} y {operandoB} es {aritmetica1.dividir():.2f}')
