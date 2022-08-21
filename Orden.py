# Tema: Diseño de clases
from Producto import *


class Orden:
    contadorOrdenes = 0  # Variable de clase
    # Contructor de la clase

    def __init__(self, productos):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._productos = list(productos)

    @property
    def getProductos(self):
        return self._productos

    @getProductos.setter
    def setProductos(self, productos):
        self._productos = productos

    def agregarProducto(self, productos):
        self._productos.append(productos)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.getPrecio
        return total

    def __str__(self):
        productosStr = ''
        for producto in self._productos:
            productosStr += producto.__str__() + '|'

        return f'Orden: {self._idOrden}, Productos: {productosStr}'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.0)

    producto2 = Producto('Pantalon', 150.0)

    productos1 = [producto1, producto2]

    orden1 = Orden(productos1)

    print(orden1)
