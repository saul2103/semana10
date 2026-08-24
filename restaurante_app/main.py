from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    """Mostrar el menú principal del sistema"""
    print("\n" + "=" * 40)
    print("  RECETAS DE MI SIERRA")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Mostrar categorías")
    print("-" * 40)
    print("9. Salir")
    print("=" * 40)


def registrar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Registrar un nuevo producto"""
    try:
        nombre = input("Nombre del producto: ").strip()
        precio = float(input("Precio del producto: "))
        categoria = input("Categoría (entrada/plato fuerte/bebida/postre): ").strip()
        stock = int(input("Stock del producto: "))
        
        producto = Producto(nombre, precio, categoria, stock)
        if restaurante.registrar_producto(producto):
            print(f"Producto '{nombre}' registrado exitosamente.")
            archivo_servicio.guardar_productos(restaurante.obtener_productos())
        else:
            print(f"El producto '{nombre}' ya existe.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def buscar_producto(restaurante: Restaurante) -> None:
    """Buscar un producto por nombre"""
    nombre = input("Nombre del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(nombre)
    if producto:
        print(f"{producto}")
    else:
        print(f"Producto '{nombre}' no encontrado.")


def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Actualizar un producto existente"""
    nombre = input("Nombre del producto a actualizar: ").strip()
    producto = restaurante.buscar_producto(nombre)
    if not producto:
        print(f"Producto '{nombre}' no encontrado.")
        return

    try:
        nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ").strip()
        nuevo_precio = input(f"Nuevo precio ({producto.precio}): ").strip()
        nueva_categoria = input(f"Nueva categoría ({producto.categoria}): ").strip()
        nuevo_stock = input(f"Nuevo stock ({producto.stock}): ").strip()

        restaurante.actualizar_producto(
            nombre,
            nuevo_nombre if nuevo_nombre else None,
            float(nuevo_precio) if nuevo_precio else None,
            nueva_categoria if nueva_categoria else None,
            int(nuevo_stock) if nuevo_stock else None
        )
        print(f"Producto '{nombre}' actualizado exitosamente.")
        archivo_servicio.guardar_productos(restaurante.obtener_productos())
    except ValueError as e:
        print(f"Error: {e}")


def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Eliminar un producto"""
    nombre = input("Nombre del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(nombre):
        print(f"Producto '{nombre}' eliminado exitosamente.")
        archivo_servicio.guardar_productos(restaurante.obtener_productos())
    else:
        print(f"Producto '{nombre}' no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    """Listar todos los productos registrados"""
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("\n--- LISTA DE PRODUCTOS ---")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto}")


def registrar_usuario() -> None:
    """Registrar un nuevo usuario"""
    print("Funcionalidad de registro de usuario (pendiente de implementación)")


def listar_usuarios() -> None:
    """Listar usuarios registrados"""
    print("Funcionalidad de listado de usuarios (pendiente de implementación)")


def mostrar_categorias(restaurante: Restaurante) -> None:
    """Mostrar categorías disponibles"""
    categorias = set(p.categoria for p in restaurante.listar_productos())
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("\n--- CATEGORÍAS DISPONIBLES ---")
    for categoria in sorted(categorias):
        print(f"- {categoria}")


def main() -> None:
    """Función principal del programa"""
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio()

    # Cargar productos desde el archivo
    productos_cargados = archivo_servicio.cargar_productos()
    if productos_cargados:
        restaurante.cargar_productos(productos_cargados)
        print(f"Se cargaron {len(productos_cargados)} productos desde el archivo.")
    else:
        print("No se encontraron productos guardados.")

    # Menú principal
    while True:
        mostrar_menu()
        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                registrar_producto(restaurante, archivo_servicio)
            elif opcion == "2":
                buscar_producto(restaurante)
            elif opcion == "3":
                actualizar_producto(restaurante, archivo_servicio)
            elif opcion == "4":
                eliminar_producto(restaurante, archivo_servicio)
            elif opcion == "5":
                listar_productos(restaurante)
            elif opcion == "6":
                registrar_usuario()
            elif opcion == "7":
                listar_usuarios()
            elif opcion == "8":
                mostrar_categorias(restaurante)
            elif opcion == "9":
                archivo_servicio.guardar_productos(restaurante.obtener_productos())
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número válido.")
        except KeyboardInterrupt:
            archivo_servicio.guardar_productos(restaurante.obtener_productos())
            print("\nSistema cerrado correctamente.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
