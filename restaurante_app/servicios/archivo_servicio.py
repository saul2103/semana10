import json
import os
from typing import List, Dict, Any, Optional, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario

class ArchivoServicio:
    def __init__(self) -> None:
        # Construir la ruta a datos dentro de restaurante_app
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.RUTA_JSON = os.path.join(base_dir, "datos", "productos.json")
        self._crear_directorio()

    def _crear_directorio(self) -> None:
        directorio = os.path.dirname(self.RUTA_JSON)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def guardar_productos(self, productos: List[Producto]) -> None:
        try:
            with open(self.RUTA_JSON, "w", encoding="utf-8") as archivo:
                json.dump(
                    [producto.to_dict() for producto in productos],
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar productos: {e}")

    def cargar_productos(self) -> List[Producto]:
        if not os.path.exists(self.RUTA_JSON):
            return []

        try:
            with open(self.RUTA_JSON, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if not isinstance(datos, list):
                    print("El archivo no contiene una lista válida.")
                    return []

                productos = []
                for item in datos:
                    try:
                        if not isinstance(item, dict):
                            continue
                        producto = Producto(
                            nombre=item["nombre"],
                            precio=float(item["precio"]),
                            categoria=item["categoria"],
                            stock=int(item["stock"])
                        )
                        productos.append(producto)
                    except (KeyError, ValueError, TypeError) as e:
                        print(f"Registro inválido omitido: {e}")
                        continue
                return productos
        except json.JSONDecodeError:
            print("Error: El archivo JSON no tiene un formato válido.")
            return []
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
            return []
        except Exception as e:
            print(f"Error inesperado al cargar productos: {e}")
            return []