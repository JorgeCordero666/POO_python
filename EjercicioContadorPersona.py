class Persona:
    # Variable de clase
    contadorPersona = 0

    def __init__(self, nombre, edad):
        Persona.contadorPersona += 1
        self.idPersona = Persona.contadorPersona
        # Variable de instancia
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.idPersona}, Nombre: {self.nombre}, Edad: {self.edad}]'


# Creacion de objetos
persona1 = Persona('Damian', 21)
print(persona1)
persona2 = Persona('Karen', 22)
print(persona2)
persona3 = Persona('Daniel', 24)
print(persona3)
print(f'Valor contador personas: {Persona.contadorPersona}')
