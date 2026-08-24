# Sistema de Gestión de Restaurante - Recetas de mi Sierra

**Estudiante:** Bryan Saul Iza Llano

---

## ¿Qué es este proyecto?

Este es un programa que te permite administrar los productos de un restaurante. Puedes registrar nuevos platos, buscar los que ya tienes guardados, cambiar sus precios o cantidades, eliminarlos, y organizarlos por categorías.

La información se guarda automáticamente en un archivo, por lo que no se pierde cuando cierras el programa. Cuando lo abras nuevamente, todos tus productos seguirán allí.

El código está organizado de manera clara y ordenada, usando lo que se conoce como **programación orientada a objetos**. Esto significa que cada parte del programa tiene una responsabilidad específica y bien definida.

---

## Estructura del Proyecto

Los archivos están organizados de la siguiente manera:

```
proyecto/
├── README.md                        # Este archivo de documentación
└── restaurante_app/
    ├── main.py                      # Archivo principal donde se ejecuta el programa
    ├── __init__.py                  # Marca como paquete Python
    ├── datos/
    │   └── productos.json           # Archivo donde se guardan los productos
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py              # Clase que define un Producto
    │   └── usuario.py               # Clase que define un Usuario
    └── servicios/
        ├── __init__.py
        ├── restaurante.py           # Clase que maneja la lógica del restaurante
        └── archivo_servicio.py      # Clase que guarda y carga los productos
```

---

## ¿Qué hace cada archivo?

### **restaurante_app/main.py** - El menú del programa

Este es el archivo principal que ejecutas cuando quieres usar el programa. Aquí se encuentra:

- El **menú** que ves al ejecutar la aplicación
- Las funciones que responden a cada opción del menú
- La **interacción con el usuario**: pedir datos, mostrar resultados
- El ciclo principal que mantiene el programa corriendo

Cuando seleccionas una opción en el menú, `main.py` recolecta la información que escribes y la envía a las otras partes del programa.

### **modelos/producto.py** - Definición de un Producto

Define qué es un producto y qué información debe tener:

- **Atributos**: nombre, precio, categoría, stock
- **Validaciones**: Se asegura de que los datos tengan sentido
  - El nombre debe tener al menos 3 caracteres
  - El precio debe ser mayor a cero
  - La categoría debe ser: entrada, plato fuerte, bebida o postre
  - El stock no puede ser negativo
- **Métodos útiles**: convertir a texto, guardar en archivo

### **modelos/usuario.py** - Definición de un Usuario

Define qué es un usuario con sus datos básicos:

- **Atributos**: nombre, email
- **Métodos**: mostrar la información del usuario de forma legible

### **servicios/restaurante.py** - La lógica del negocio

Esta clase hace el trabajo principal del restaurante:

- **Registrar** un nuevo producto en la lista
- **Buscar** un producto por nombre
- **Actualizar** la información de un producto (cambiar precio, stock, etc.)
- **Eliminar** un producto que ya no quieres
- **Listar** todos los productos que tienes guardados

Esta clase NO muestra menús ni pide información al usuario. Solo hace el trabajo de guardar y gestionar los datos.

### **servicios/archivo_servicio.py** - Guardar y cargar datos

Se encarga de trabajar con el archivo `productos.json`:

- **Guardar** todos los productos en el archivo
- **Cargar** los productos que guardaste antes
- **Manejo de errores**: si el archivo no existe, lo crea automáticamente

---

## Validaciones (Reglas de entrada)

El programa no acepta cualquier información. Verifica que los datos tengan sentido:

**Para los Productos:**
- Nombre: No puede estar vacío, mínimo 3 caracteres
- Precio: Debe ser un número mayor que 0
- Categoría: Solo acepta las 4 categorías definidas
- Stock: Debe ser un número entero positivo o cero
- No permite productos duplicados (dos con el mismo nombre)

**Para los archivos:**
- Valida que el formato JSON sea correcto
- Si hay un producto con datos faltantes, lo ignora
- Muestra mensajes de error si hay problemas al leer o guardar

---

## Cómo ejecutar el programa

**Requisitos:**
- Tener Python 3.7 o superior instalado
- No necesitas instalar nada más (usa solo bibliotecas que vienen con Python)

**Pasos:**

1. Abre la terminal o línea de comandos en la carpeta del proyecto

2. Escribe este comando:
   ```
   python restaurante_app/main.py
   ```

3. Verás un menú como este:
   ```
   ========================================
     RECETAS DE MI SIERRA
   ========================================
   1. Registrar producto
   2. Buscar producto
   3. Actualizar producto
   4. Eliminar producto
   5. Listar productos
   6. Registrar usuario
   7. Listar usuarios
   8. Mostrar categorías
   ----------------------------------------
   9. Salir
   ========================================
   ```

4. Escribe el número de la opción que quieres y presiona Enter

5. Para salir, escribe 9 o presiona Ctrl+C

---

## Ejemplo de uso

**Registrar un producto:**

```
Seleccione una opción: 1
Nombre del producto: Ceviche
Precio del producto: 15.50
Categoría (entrada/plato fuerte/bebida/postre): entrada
Stock del producto: 10
Producto 'Ceviche' registrado exitosamente.
```

**Listar productos:**

```
Seleccione una opción: 5

--- LISTA DE PRODUCTOS ---
1. Producto: Ceviche | Precio: $15.50 | Categoría: entrada | Stock: 10
```

---

## El archivo productos.json

Cuando guardas productos, se crean automáticamente en `restaurante_app/datos/productos.json`. Así se ven:

```json
[
    {
        "nombre": "Ceviche",
        "precio": 15.5,
        "categoria": "entrada",
        "stock": 10
    },
    {
        "nombre": "Lomo Saltado",
        "precio": 18.75,
        "categoria": "plato fuerte",
        "stock": 5
    }
]
```

Cada producto tiene su nombre, precio, categoría y cantidad disponible.

---

## Lo que falta por hacer

Las siguientes opciones están en el menú pero no funcionan todavía:

- Registro completo de usuarios (opción 6)
- Listado de usuarios (opción 7)

Estas funcionalidades se pueden agregar en el futuro siguiendo el mismo patrón que se usó para los productos.

---

## Características implementadas

El programa actualmente permite:

- **Registrar** nuevos productos con validación automática de datos
- **Buscar** un producto por nombre
- **Actualizar** información de productos (nombre, precio, categoría, stock)
- **Eliminar** productos que ya no quieres
- **Listar** todos los productos guardados
- **Mostrar** las categorías disponibles
- **Guardar** automáticamente los cambios en un archivo
- **Cargar** productos guardados al iniciar

---

## Cómo está diseñado el código

El proyecto sigue estas buenas prácticas:

**Responsabilidad única:** Cada clase hace una cosa bien definida
- `Producto` solo define qué es un producto
- `Restaurante` solo maneja la lista de productos
- `ArchivoServicio` solo se encarga de guardar y cargar archivos
- `restaurante_app/main.py` solo muestra el menú y pide información al usuario

**Fácil de cambiar:** Si necesitas cambiar algo, solo tocas la parte relevante
- Si cambias cómo se valida un producto, solo editas `producto.py`
- Si cambias el formato de archivo, solo editas `archivo_servicio.py`
- Si quieres una interfaz diferente, solo editas `restaurante_app/main.py`

**Reutilizable:** Puedes agregar nuevas clases sin romper las existentes
- Agregar una clase `Usuario` completa sin tocar el código de productos
- Agregar una clase `Bebida` que herede de `Producto`
- Cambiar de JSON a una base de datos sin afectar el resto

**Protección de datos:** Se valida la entrada del usuario automáticamente
- El programa no deja guardar un producto sin nombre
- No acepta precios negativos
- Verifica que la categoría sea válida

---

## Información del proyecto

**Curso:** Programación Orientada a Objetos
**Universidad:** Universidad Estatal Amazónica
**Nivel:** Semana 10 - Organización Modular Mejorada
**Estudiante:** Bryan Saul Iza Llano

---

## Preguntas frecuentes

**¿Dónde se guardan los productos?**
En el archivo `restaurante_app/datos/productos.json`. Se crea automáticamente la primera vez que guardas un producto.

**¿Qué pasa si el programa se cierra de repente?**
No hay problema. Los datos se guardan cada vez que haces una operación (registrar, actualizar o eliminar), así que siempre están seguros.

**¿Puedo editar el archivo `productos.json` directamente?**
Sí, pero ten cuidado. Si cambias el formato y no es JSON válido, el programa no podrá cargarlo.

**¿Cómo agrego nuevas categorías?**
Edita el archivo `restaurante_app/modelos/producto.py` y busca la lista de categorías válidas en la función `_validar_categoria()`.

**¿Cómo extiendo el programa para agregar usuarios?**
Ya existe la clase `Usuario` en `restaurante_app/modelos/usuario.py`. Puedes agregar métodos en `restaurante.py` para registrar y listar usuarios, igual que se hizo con los productos.

