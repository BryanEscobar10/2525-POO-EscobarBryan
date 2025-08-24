# SISTEMA DE GESTION DE INVENTARIO MEJORADO
import json
import os

class Producto:            #CLASE PRODUCTO
    def __init__(self, id, nombre, cantidad, precio):
        # Atributos principales de cada producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):     # Representación legible de un producto
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
    
    def to_dict(self):     # Convierte el objeto Producto a un diccionario (para guardar en JSON)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):    # Crea un objeto Producto a partir de un diccionario (al cargar desde JSON)
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

class Inventario:          #CLASE INVENTARIO
    def __init__(self):
        # Ruta fija del archivo JSON (ya que no reconocia el archivo sino que creaba otro)
        archivo = 'Parcial_2/Semana_9/Semana_10/inventario.json'
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):   #Carga los productos desde el archivo JSON.
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Reconstruye los productos como objetos Producto
                    self.productos = {pid: Producto.from_dict(prod) for pid, prod in data.items()}
            else:
                # Si no existe el archivo, se crea uno nuevo vacío
                self.productos = {}
                self.guardar_inventario()
        #Maneja errores comunes como permisos o formato incorrecto.
        except FileNotFoundError:
            print("Error: El archivo de inventario no fue encontrado. Se creará uno nuevo.")
            self.productos = {}
            self.guardar_inventario()
        except json.JSONDecodeError:
            print("Error: El archivo de inventario está dañado. Se reiniciará vacío.")
            self.productos = {}
            self.guardar_inventario()
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):           #Guarda los productos en el archivo JSON.
        #Convierte los objetos Producto a diccionarios antes de almacenarlos.
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump({pid: p.to_dict() for pid, p in self.productos.items()}, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):     #Añade un nuevo producto al inventario.
        if producto.id in self.productos:
            print("Error: Ya existe un producto con ese ID.")
            return
        self.productos[producto.id] = producto
        self.guardar_inventario()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id):          #Elimina un producto del inventario dado su ID.
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado con éxito.")
        else:
            print("No se encontró un producto con ese ID.")

    def actualizar_precio(self, id, nuevo_precio=None):     #Actualiza el precio de un producto dado su ID.
        if id in self.productos:
            if nuevo_precio is not None:
                self.productos[id].precio = nuevo_precio
                self.guardar_inventario()
            print("Precio actualizado con éxito.")
        else:
            print("No se encontró un producto con ese ID.")

    def actualizar_cantidad(self, id, nuevo_cantidad=None):  #Actualiza la cantidad de un producto dado su ID.
        if id in self.productos:
            if nuevo_cantidad is not None:
                self.productos[id].cantidad = nuevo_cantidad
                self.guardar_inventario()
            print("Cantidad actualizada con éxito.")
        else:
            print("No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):      #Buscar producto por nombre
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):              #Muestra todos los productos en el inventario.
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Lista de productos en inventario:")
            for p in self.productos.values():
                print(p)

# ---------------- INTERFAZ DE USUARIO -----------------
def menu():
    inventario = Inventario()

    while True:
        print("\n---MENÚ DE INVENTARIO---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar precio")
        print("4. Actualizar cantidad de un producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                # Crear un nuevo producto con datos ingresados por el usuario
                id = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                # Eliminar un producto existente
                id = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id)

            elif opcion == "3":
                # Actualizar solo el precio
                id = input("ID del producto a actualizar: ")
                precio = input("Nuevo precio (Enter para no cambiar): ")
                nuevo_precio = float(precio) if precio else None
                inventario.actualizar_precio(id, nuevo_precio)

            elif opcion == "4":
                # Actualizar solo la cantidad
                id = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (Enter para no cambiar): ")
                nuevo_cantidad = int(cantidad) if cantidad else None
                inventario.actualizar_cantidad(id, nuevo_cantidad)

            elif opcion == "5":
                # Buscar por nombre
                nombre = input("Nombre a buscar: ")
                inventario.buscar_por_nombre(nombre)

            elif opcion == "6":
                # Mostrar todo el inventario
                inventario.mostrar_productos()

            elif opcion == "7":
                # Finalizar el programa
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("⚠️ Opción inválida, intenta de nuevo.")

        except ValueError:
            # Maneja entradas no numéricas en cantidad o precio
            print("⚠️ Error: Ingresaste un dato no válido (se esperaba número).")
        except Exception as e:
            print(f"Error inesperado: {e}")


# Ejecutar el programa principal
if __name__ == "__main__":
    menu()
