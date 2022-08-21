# Tema: Diseño de clase
from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.0)
producto2 = Producto('Pantalon', 150.0)
producto3 = Producto('Chaqueta', 50.0)
producto4 = Producto('Blusa', 70.00)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregarProducto(producto3)
orden1.agregarProducto(producto4)
orden2 = Orden(productos2)
print(orden1)
print("Total de la orden 1 es: ", orden1.calcularTotal())
print(orden2)
print("Total de la orden 2 es: ", orden2.calcularTotal())
