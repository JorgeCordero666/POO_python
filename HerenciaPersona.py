# Tema: Ejercicio de herencia simple
'''Esta es una clase padre'''


class HerenciaPersona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'


'''Esta es una clase hija de la clase HerenciaPadre'''
# Definicion de herencia


class Empleado (HerenciaPersona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


# Acceder a  los atributos de la clase heredada y la clase Empleado
'''
empleado1 = Empleado("Juan", 22, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
'''
