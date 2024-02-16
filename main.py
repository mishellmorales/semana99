class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.id == producto.id:
                print("El ID del producto ya existe. Intente con otro ID.")
                return
        self.productos.append(producto)
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                print("Producto eliminado con éxito.")
                return
        print("No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                print("Producto actualizado con éxito.")
                return
        print("No se encontró ningún producto con ese ID.")

    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.nombre.lower():
                resultados.append(p)
        if len(resultados) == 0:
            print("No se encontraron productos con ese nombre.")
        else:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)

    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(producto)


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Salir")


if _name_ == "_main_":
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            continue  # Continuar con el siguiente ciclo del bucle
        elif opcion == "2":
            id = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto que desea actualizar: ")
            opcion_actualizar = input("Seleccione qué desea actualizar (cantidad/precio): ")
            if opcion_actualizar == "cantidad":
                cantidad = int(input("Ingrese la nueva cantidad: "))
                inventario.actualizar_producto(id, cantidad=cantidad)
            elif opcion_actualizar == "precio":
                precio = float(input("Ingrese el nuevo precio: "))
                inventario.actualizar_producto(id, precio=precio)
            else:
                print("Opción no válida.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
