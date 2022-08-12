# Definicion de clases en Python
class Persona:
    # Metodo init ---> Inicializar atributos
    # Definicion
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

# Encapsular datos
# definicion del metodo  Get nombre

    @property  # la palabra reservada @property modifica el metodo para utilizarlo como un atributo
    def nombre(self):
        print("LLamando metodo get nombre")
        return self._nombre

# definicion del metodo setter nombre
    @nombre.setter
    def nombre(self, nombre):
        print("LLamando metodo set nombre")
        self._nombre = nombre

# definicion del metodo get apellido
    @property
    def apellido(self):
        return self._apellido


# definicion del metodo setter apellido


    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

# definicion del metodo get edad
    @property
    def edad(self):
        return self._edad

# definicion del metodo set edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

# definicion de  un Metodo mostrarDetalle

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

# definicion del metodo destructor
    def __del__(self):
        print(f"Persona: {self._nombre}, {self._apellido}")


# Crear Objetos con Parametros
# Definicion
persona1 = Persona('Juan', 'Perez', 28)

# Hacer pruebas desde una clase:

if __name__ == '__main__':
    # Acceder al atributo de una clase
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)

    persona2 = Persona('Ana', 'Ortiz', 30)

    # Acceder al atributo de una clase
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    # Acceder a un metodo
    persona1.mostrarDetalle()
    persona2.mostrarDetalle()
    print(persona1.nombre)
    persona1.nombre = "Juan Carlos "
    print(persona1.nombre)
    persona1.apellido = "Lara"
    persona1.edad = 30
    persona1.mostrarDetalle()
    # Forma de saber en que clase estamos
    print(__name__)
