# Sistema de Gestión de Pulpería - Documentación

## 1. Portada

**Proyecto Programado #1**
**Nombre:** [Tu Nombre]
**Carné:** [Tu Carné]
**Curso:** Taller de Programación

## 2. Manual de Usuario

### Ejecución

Para iniciar el programa, asegúrese de tener Python instalado.
Ejecute el archivo principal desde la consola:

```bash
python programa/Proyecto1.py
```

### Funcionalidades

1. **Inventario**: Requiere iniciar sesión (ej: `pperez`, `1234`).
   - Agregar, Modificar, Borrar productos.
   - Agregar Inventario (Stock).
   - Reportes de inventario.
2. **Facturar**:
   - Ingrese el nombre del cliente.
   - Ingrese códigos de productos para agregarlos al carrito.
   - Escriba 'FIN' para procesar la factura.
3. **Reportes**:
   - Visualice ventas, facturas, clientes y utilidades.
   - Exporte reportes a archivos `csv` (opcional implementado).

## 3. Descripción del Problema

Se requiere un sistema para administrar una pequeña pulpería, permitiendo gestionar el inventario de productos, realizar ventas (facturación) y generar reportes administrativos básicos. El sistema debe persistir datos en archivos de texto y respetar restricciones de no usar funciones nativas de alto nivel.

## 4. Diseño del Programa

### Algoritmos Usados

- **Lectura/Escritura Secuencial**: Uso de archivos planos `.txt` separados por `.` o `,`.
- **Búsqueda Lineal**: Para encontrar productos por ID o facturas.
- **Helpers Personalizados**: Implementación de `mi_len`, `mi_split`, `mi_append` para evitar built-ins prohibidos.

### Estructuras de Datos

- Listas de Listas: `INVENTARIO = [[id, nombre, cat, precio, stock], ...]`.

## 5. Análisis de Resultados

- **Objetivos Alcanzados**: Gestión completa de inventario, facturación, y reporte. Persistencia de datos correcta.
- **Extras**: Se implementó exportación a archivo y reporte por rango de fechas.

## 6. Conclusión

El desarrollo permitió reforzar la lógica de programación al manipular estructuras de datos manualmente sin depender de atajos del lenguaje, simulando un entorno de bajo nivel o con restricciones estrictas.
