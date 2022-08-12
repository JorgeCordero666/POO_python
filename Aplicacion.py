# Tema: Eliminacion de objetos e importacion de paquetes
# Definicion para llamar paquetes
from Persona import Persona

# Utilizar esos paquetes
print("Creacion de objetos".center(50, '-'))
persona3 = Persona("Karo", "Gomez", 30)
persona3.mostrarDetalle()

print("Eliminacion de objetos".center(50, '*'))
del persona3  # Eliminar Objetos
