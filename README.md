# Sistema de Gestión de Pulpería - ConsolApp 🏪

**Estudiante:** Geovanni Gonzalez Aguilar
**Carné:** 2022163324
**Curso:** Taller de Programación

## 📋 Descripción

Este proyecto consiste en un sistema de consola desarrollado en **Python** para la administración de una pulpería (tienda de abarrotes). El sistema gestiona inventarios, procesa facturas de venta y genera reportes administrativos, cumpliendo con restricciones académicas estrictas (no uso de `len`, `append`, `remove`, etc.).

## ✨ Características Principales

- **Gestión de Inventario**: Agregar, modificar y borrar productos con validación de integridad referencial.
- **Facturación**: Carrito de compras, cálculo automático de impuestos (13%) y control de stock en tiempo real.
- **Persistencia de Datos**: Todos los datos se guardan automáticamente en archivos de texto (`.txt`).
- **Reportes**:
  - Ventas por producto y cliente.
  - Estado de utilidades.
  - **[NUEVO]** Reporte por rango de fechas.
  - Exportación a archivos externos.
- **UI Innovadora**: Interfaz de consola con colores (ANSI), banners ASCII y diseño limpio.

## 🚀 Ejecución

Para iniciar la aplicación, asegúrese de estar en la carpeta raíz del proyecto y ejecute:

```bash
python programa/Proyecto1.py
```

### Credenciales de Acceso

Para ingresar al módulo de inventario, utilice alguno de los siguientes usuarios:

- **Usuario**: `pperez` | **Clave**: `1234`
- **Usuario**: `ccastro` | **Clave**: `admin1234`
- **Usuario**: `mporras` | **Clave**: `mporras1`

## 📂 Estructura del Proyecto

```
SistemaDeGestionPulperia-ConsolApp/
├── programa/
│   ├── Proyecto1.py        # Código fuente principal
│   ├── Acceso.txt          # Base de datos de usuarios
│   ├── Inventario.txt      # Base de datos de productos
│   ├── Facturas.txt        # Encabezados de facturas
│   └── FacturasDetalle.txt # Detalle de items por factura
├── documentacion/
│   └── Documentacion.md    # Manual técnico y de usuario
├── project-info.json       # Metadatos del proyecto
└── README.md               # Este archivo
```

## 🛠️ Tecnologías

- **Lenguaje**: Python 3
- **Interfaz**: Consola (CLI) con secuencias de escape ANSI.
- **Base de Datos**: Archivos de Texto Plano.
