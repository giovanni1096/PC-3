class Producto:
    def __init__(self, nombre, año, precio):
        self.nombre = nombre
        self.año = año
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):

        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al catálogo.")

    def mostrar_productos(self):

        print("Lista de Productos:")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Año: {producto.año}, Precio: {producto.precio}")

    def filtrar_por_año(self, año):
 
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        print(f"Productos del año {año}:")
        for producto in productos_filtrados:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}")

    def buscar_por_nombre(self, nombre):
        
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if productos_encontrados:
            print(f"Productos con el nombre '{nombre}':")
            for producto in productos_encontrados:
                print(f"Año: {producto.año}, Precio: {producto.precio}")
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")


catalogo = Catalogo()

producto1 = Producto("Filtro de Aceite", 2022, 16.99)
producto2 = Producto("Batería de Coche", 2020, 99.99)
producto3 = Producto("Pastillas de Freno", 2022, 49.99)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

catalogo.mostrar_productos()

catalogo.filtrar_por_año(2022)

catalogo.buscar_por_nombre("Freno")