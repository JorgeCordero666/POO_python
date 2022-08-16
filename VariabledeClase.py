'''Creación de variables de clase'''


class VariabledeClase:
    # Las variables de clase se asocian con las clases
    variable_clase = "Valor_variable_clase"

    def __init__(self, variable_instancia):
        # Las variables de instancia se asocian con los objetos
        self.variable_instancia = variable_instancia

    '''Creacion de metodos estaticos '''
    # Un metodo estatico no puede acceder a las variables de instancia
    # Tampoco puede acceder a la variable de instancia
    # Definicion
    @staticmethod
    def metodoEstatico():
        print(VariabledeClase.variable_clase)

    '''Metodos de clase '''
    # Definicion
    @classmethod
    def metodoClase(cls):
        print(cls.variable_clase)


# Acceder a una variable de clase
print(VariabledeClase.variable_clase)
'''
Para acceder a la variable de instancia 
se necesita crear un objeto primero
'''
miClase = VariabledeClase('Valor variable instancia')

# Las variables de instancia tienen un nuevo valor para cada objeto que se crea.
print(miClase.variable_instancia)
'''Se puede acceder a las vriables de clase usando el objeto'''
print(miClase.variable_clase)

# Creacion de objeto 2
miClase2 = VariabledeClase('Variable de instancia 2')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
'''Variables de clase al vuelo'''
# Forma de crear una variable de clase mientras programamos
VariabledeClase.variable_clase2 = "Variable de clase 2"
print(VariabledeClase.variable_clase2)
print(miClase.variable_clase2)

# Para acceder a los metodos estaticos se utiliza el nombre de la clase
VariabledeClase.metodoEstatico()

# Para llamar un metodo de clase se llama igual que el estatico
print("Metodo de clase ")
VariabledeClase.metodoClase()
# Se puede acceder a un metodo de clase desde un objeto

miObjeto1 = VariabledeClase('Objeto de la variable de instancia')
miObjeto1.metodoClase()
