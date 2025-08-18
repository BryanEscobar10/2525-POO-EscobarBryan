#SISTEMA DE GESTION DE INVENTARIO

class Producto:
    # Clase que representa un producto dentro del inventario
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    # Métodos getters y setters para acceder y modificar los atributos
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio = precio

    # Método para representar el producto como texto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    # Clase que gestiona una lista de productos
    def __init__(self):
        self.productos = []

    # Añade un nuevo producto al inventario
    def añadir_producto(self, producto):
        # Verificar que el ID no se repita
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        # Elimina un producto según su ID
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado con éxito.")
                return
        print("No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nuevo_precio=None):
        # Actualiza el precio de un producto según su ID
        for p in self.productos:
            if p.get_id() == id:
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado con éxito.")
                return
        print("No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        # Busca productos cuyo nombre contenga el texto ingresado
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        # Muestra todos los productos del inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Lista de productos en inventario:")
            for p in self.productos:
                print(p)


# ---------------- INTERFAZ DE USUARIO -----------------
def menu():
    # Función que muestra un menú interactivo para gestionar el inventario
    inventario = Inventario()

    while True:
        print("\n📌 MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
        # Se piden los datos y se crea un nuevo producto
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
        # Eliminar producto por ID
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
        # Actualizar precio de un producto
            id = input("ID del producto a actualizar: ")
            precio = input("Nuevo precio (Enter para no cambiar): ")
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id, nuevo_precio)

        elif opcion == "4":
        # Buscar producto por nombre
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
        # Mostrar todos los productos del inventario
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()