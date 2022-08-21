# Tema: Diseño de clases
class Producto:
    contadorProducto = 0

    def __init__(self, nombre, precio):
        Producto.contadorProducto += 1
        self._idProducto = Producto.contadorProducto
        self._nombre = nombre
        self._precio = precio

    @property
    def getNombre(self):
        return self._nombre

    @getNombre.setter
    def setNombre(self, nombre):
        self._nombre = nombre

    @property
    def getPrecio(self):
        return self._precio

    @getPrecio.setter
    def setPrecio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'Id Producto {self._idProducto} Nombre: {self._nombre} Precio: {self._precio}'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.0)
    print(producto1)
    producto2 = Producto('Pantalon', 150.0)
    print(producto2)
