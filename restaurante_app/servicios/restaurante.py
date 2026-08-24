from typing import List, Optional
from restaurante_app.modelos.producto import Producto

class Restaurante:
    def __init__(self) -> None:
        self._productos: List[Producto] = []

    def cargar_productos(self, productos: List[Producto]) -> None:
        self._productos = productos

    def obtener_productos(self) -> List[Producto]:
        return self._productos.copy()

    def registrar_producto(self, producto: Producto) -> bool:
        for p in self._productos:
            if p.nombre.lower() == producto.nombre.lower():
                return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def actualizar_producto(self, nombre: str, nuevo_nombre: Optional[str] = None,
                           nuevo_precio: Optional[float] = None,
                           nueva_categoria: Optional[str] = None,
                           nuevo_stock: Optional[int] = None) -> bool:
        producto = self.buscar_producto(nombre)
        if not producto:
            return False

        if nuevo_nombre is not None:
            producto.nombre = nuevo_nombre
        if nuevo_precio is not None:
            producto.precio = nuevo_precio
        if nueva_categoria is not None:
            producto.categoria = nueva_categoria
        if nuevo_stock is not None:
            producto.stock = nuevo_stock
        return True

    def eliminar_producto(self, nombre: str) -> bool:
        producto = self.buscar_producto(nombre)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        return self._productos.copy()