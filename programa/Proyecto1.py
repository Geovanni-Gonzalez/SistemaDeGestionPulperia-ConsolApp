"""
Proyecto Programado #1: Sistema de Gestión de Pulpería
Estudiante: [Nombre]
Carné: [Carné]

Restricciones: No usar len, append, remove, in (excepto for), replace.
"""

import os
from datetime import datetime

# ==========================================
# UI/UX Constants
# ==========================================
COLOR_RESET = "\033[0m"
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_HEADER = "\033[1;34m"

BANNER = r"""
  ____        _                  _       
 |  _ \ _   _| |_ __   ___ _ __ (_) __ _ 
 | |_) | | | | | '_ \ / _ \ '__|| |/ _` |
 |  __/| |_| | | |_) |  __/ |   | | (_| |
 |_|    \__,_|_| .__/ \___|_|   |_|\__,_|
               |_|                       
"""

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_header(titulo):
    limpiar_pantalla()
    print(COLOR_CYAN + BANNER + COLOR_RESET)
    print(COLOR_HEADER + f"{titulo.center(40)}" + COLOR_RESET)
    print(COLOR_MAGENTA + "="*40 + COLOR_RESET)

def input_bonito(texto):
    return input(f"{COLOR_YELLOW}{texto}{COLOR_RESET}")

def print_exito(texto):
    print(f"{COLOR_GREEN}✔ {texto}{COLOR_RESET}")

def print_error(texto):
    print(f"{COLOR_RED}✘ {texto}{COLOR_RESET}")

# ==========================================
# Funciones Auxiliares (Custom Built-ins)
# ==========================================

def mi_len(iterable):
    """Calcula la longitud de un iterable."""
    contador = 0
    for _ in iterable:
        contador += 1
    return contador

def mi_append(lista, elemento):
    """Agrega un elemento al final de la lista."""
    lista += [elemento]
    return lista

def mi_remove(lista, elemento):
    """Elimina la primera ocurrencia de un elemento de la lista."""
    nueva_lista = []
    eliminado = False
    for x in lista:
        if x == elemento and not eliminado:
            eliminado = True
        else:
            nueva_lista += [x]
    
    # Truco para modificar la lista original referencia (limitación sin métodos)
    # En Python puro sin métodos, lo mejor es retornar la nueva lista y reasignar
    return nueva_lista

def mi_split(texto, delimitador):
    """Divide un texto por un delimitador."""
    partes = []
    actual = ""
    for car in texto:
        if car == delimitador:
            partes += [actual]
            actual = ""
        else:
            actual += car
    partes += [actual]
    return partes

def mi_replace(texto, viejo, nuevo):
    """Reemplaza subcadenas."""
    # Implementación simple para reemplazo caracter a caracter o similar
    # Dado que split y join son métodos, haremos algo manual
    res = ""
    i = 0
    long_viejo = mi_len(viejo)
    while i < mi_len(texto):
        # Miriar si coincide
        coincide = True
        for j in range(long_viejo):
            if i + j >= mi_len(texto) or texto[i+j] != viejo[j]:
                coincide = False
                break
        
        if coincide:
            res += nuevo
            i += long_viejo
        else:
            res += texto[i]
            i += 1
    return res

def obtener_fecha_hora():
    """Retorna fecha y hora actuales como strings."""
    now = datetime.now()
    fecha = f"{now.day}/{now.month}/{now.year}"
    
    hora_val = now.hour
    ampm = "am"
    if hora_val >= 12:
        ampm = "pm"
        if hora_val > 12:
            hora_val -= 12
    if hora_val == 0:
        hora_val = 12
        
    minutos = str(now.minute)
    if mi_len(minutos) == 1:
        minutos = "0" + minutos
        
    hora = f"{hora_val}:{minutos} {ampm}"
    return fecha, hora

# ==========================================
# Variables Globales (Estado)
# ==========================================
USUARIOS = [] # Lista de listas [user, pass]
INVENTARIO = [] # Lista de listas [id, nombre, categoria, precio, cantidad]
FACTURAS = [] # Lista de listas
DETALLE_FACTURAS = [] # Lista de listas

# Rutas
DIR_PROGRAMA = "programa" # Asumiendo ejecución desde padre, ajuste dinámico abajo
PATH_ACCESO = "Acceso.txt"
PATH_INVENTARIO = "Inventario.txt"
PATH_FACTURAS = "Facturas.txt"
PATH_DETALLE = "FacturasDetalle.txt"

# Ajuste de rutas si se corre desde 'programa' o desde root
if os.path.exists("programa"):
    PATH_ACCESO = "programa/Acceso.txt"
    PATH_INVENTARIO = "programa/Inventario.txt"
    PATH_FACTURAS = "programa/Facturas.txt"
    PATH_DETALLE = "programa/FacturasDetalle.txt"

# ==========================================
# Gestión de Archivos
# ==========================================

def cargar_usuarios():
    global USUARIOS
    USUARIOS = []
    if not os.path.exists(PATH_ACCESO):
        return
    
    try:
        archivo = open(PATH_ACCESO, "r")
        for linea in archivo:
            limpia = linea.strip()
            if mi_len(limpia) > 0:
                datos = mi_split(limpia, ";")
                if mi_len(datos) >= 2:
                    USUARIOS = mi_append(USUARIOS, [datos[0], datos[1]])
        archivo.close()
    except:
        print("Error cargando usuarios.")

def cargar_inventario():
    global INVENTARIO
    INVENTARIO = []
    if not os.path.exists(PATH_INVENTARIO):
        return

    try:
        archivo = open(PATH_INVENTARIO, "r")
        for linea in archivo:
            limpia = linea.strip()
            if mi_len(limpia) > 0:
                # Formato: id;nombre;cat;precio;cant
                datos = mi_split(limpia, ";")
                if mi_len(datos) == 5:
                    # Convertir tipos
                    prod = [
                        datos[0].strip(),
                        datos[1].strip(),
                        datos[2].strip(),
                        int(datos[3].strip()),
                        int(datos[4].strip())
                    ]
                    INVENTARIO = mi_append(INVENTARIO, prod)
        archivo.close()
    except:
        print("Error cargando inventario.")

def guardar_inventario():
    try:
        archivo = open(PATH_INVENTARIO, "w")
        for prod in INVENTARIO:
            # 1; Coca Cola; Bebidas; 1000; 0
            linea = f"{prod[0]}; {prod[1]}; {prod[2]}; {prod[3]}; {prod[4]}\n"
            archivo.write(linea)
        archivo.close()
    except:
        print("Error guardando inventario.")


# ==========================================
# Gestión de Archivos (Continuación)
# ==========================================

def cargar_facturas():
    global FACTURAS, DETALLE_FACTURAS
    FACTURAS = []
    DETALLE_FACTURAS = []
    
    # Cargar Facturas Encabezado
    if os.path.exists(PATH_FACTURAS):
        try:
            archivo = open(PATH_FACTURAS, "r")
            for linea in archivo:
                limpia = linea.strip()
                if mi_len(limpia) > 0:
                    datos = mi_split(limpia, ",")
                    # 1,Pedro Perez,30/3/2023,1:30pm,4400,572,4972, Contado
                    if mi_len(datos) >= 8:
                        FACTURAS = mi_append(FACTURAS, datos)
            archivo.close()
        except:
            print("Error cargando facturas.")

    # Cargar Detalle
    if os.path.exists(PATH_DETALLE):
        try:
            archivo = open(PATH_DETALLE, "r")
            for linea in archivo:
                limpia = linea.strip()
                if mi_len(limpia) > 0:
                    datos = mi_split(limpia, ",")
                    # 1, 1,Coca Cola,2,1000,2000,260,2260
                    if mi_len(datos) >= 8:
                        # Limpiar espacios en blanco de cada campo
                        fila = []
                        for d in datos:
                            fila = mi_append(fila, d.strip())
                        DETALLE_FACTURAS = mi_append(DETALLE_FACTURAS, fila)
            archivo.close()
        except:
            print("Error cargando detalles.")

def guardar_nueva_factura(encabezado, detalles):
    # Guardar Encabezado
    try:
        archivo = open(PATH_FACTURAS, "a") # Append
        linea = f"{encabezado[0]},{encabezado[1]},{encabezado[2]},{encabezado[3]},{encabezado[4]},{encabezado[5]},{encabezado[6]},{encabezado[7]}\n"
        archivo.write(linea)
        archivo.close()
        
        # Actualizar memoria global
        global FACTURAS
        FACTURAS = mi_append(FACTURAS, encabezado)
    except:
        print("Error escribiendo factura.")

    # Guardar Detalles
    try:
        archivo = open(PATH_DETALLE, "a")
        for d in detalles:
            linea = f"{d[0]}, {d[1]}, {d[2]}, {d[3]}, {d[4]}, {d[5]}, {d[6]}, {d[7]}\n"
            archivo.write(linea)
            
            global DETALLE_FACTURAS
            DETALLE_FACTURAS = mi_append(DETALLE_FACTURAS, d)
        archivo.close()
    except:
        print("Error escribiendo detalle.")

def producto_fue_vendido(pid):
    cargar_facturas() # Asegurar tener lo último
    for d in DETALLE_FACTURAS:
        if d[1] == str(pid):
            return True
    return False

# ==========================================
# Lógica de Negocio (Continuación)
# ==========================================


# ==========================================
# Lógica de Negocio (Restaurada)
# ==========================================

def login():
    intentos = 0
    while intentos < 3:
        imprimir_header("ACCESO AL SISTEMA")
        print("Por favor ingrese sus credenciales.")
        user = input_bonito("Usuario: ")
        pwd = input_bonito("Clave: ")
        
        # Validar
        encontrado = False
        for u in USUARIOS:
            if u[0] == user and u[1] == pwd:
                encontrado = True
                break
        
        if encontrado:
            print_exito("Acceso Correcto.")
            input("Presione ENTER para continuar...")
            return True
        else:
            print_error("Credenciales inválidas.")
            intentos += 1
            input("Presione ENTER para reintentar...")
            
    print_error("Demasiados intentos fallidos.")
    return False

def menu_principal():
    cargar_usuarios()
    cargar_inventario()
    
    logged_in = False
    
    while True:
        imprimir_header("MENÚ PRINCIPAL")
        print(f"{COLOR_CYAN}[I]{COLOR_RESET} Inventario")
        print(f"{COLOR_CYAN}[F]{COLOR_RESET} Facturar")
        print(f"{COLOR_CYAN}[R]{COLOR_RESET} Reportes")
        print(f"{COLOR_RED}[S]{COLOR_RESET} Salir")
        
        opcion = input_bonito("Seleccione una opción: ").upper()
        
        if opcion == "S":
            print("Saliendo y guardando datos...")
            guardar_inventario()
            break
            
        elif opcion == "I":
            if not logged_in:
                if login():
                    logged_in = True
                    submenu_inventario()
                else:
                    print("Acceso denegado al módulo de inventario.")
            else:
                 submenu_inventario()
                 
        elif opcion == "F":
            modulo_facturacion()
            
        elif opcion == "R":
            modulo_reportes()
            
        else:
            print("Opción inválida.")

def submenu_inventario():
    while True:
        imprimir_header("GESTIÓN DE INVENTARIOS")
        print(f"[A] Agregar producto")
        print(f"[M] Modificar producto")
        print(f"[B] Borrar producto")
        print(f"[I] Agregar inventario (Stock)")
        print(f"[R] Reporte de productos")
        print(f"{COLOR_RED}[S] Volver{COLOR_RESET}")
        
        op = input_bonito("Opción: ").upper()
        
        if op == "S":
            break
        elif op == "A":
            agregar_producto()
        elif op == "M":
            modificar_producto()
        elif op == "B":
            borrar_producto()
        elif op == "I":
            agregar_stock()
        elif op == "R":
            reporte_productos_simple()
        else:
            print("Opción no válida.")

def generar_id_producto():
    if mi_len(INVENTARIO) == 0:
        return "1"
    
    max_id = 0
    for p in INVENTARIO:
        try:
            pid = int(p[0])
            if pid > max_id:
                max_id = pid
        except:
            pass
    return str(max_id + 1)

def producto_existe_nombre(nombre):
    for p in INVENTARIO:
        if p[1].lower() == nombre.lower():
            return True
    return False

def buscar_producto_por_id(pid):
    for i in range(mi_len(INVENTARIO)):
        if INVENTARIO[i][0] == pid:
            return i 
    return -1

def agregar_producto():
    global INVENTARIO 
    imprimir_header("AGREGAR PRODUCTO")
    nombre = input_bonito("Nombre: ").strip()
    if producto_existe_nombre(nombre):
        print_error("Error: Ya existe un producto con ese nombre.")
        input("Enter para continuar...")
        return
    
    categoria = input_bonito("Categoría: ").strip()
    try:
        precio = int(input_bonito("Precio Unitario: "))
        if precio < 0:
            print_error("El precio no puede ser negativo.")
            return
    except:
        print_error("Precio inválido.")
        return
        
    pid = generar_id_producto()
    nuevo = [pid, nombre, categoria, precio, 0]
    INVENTARIO = mi_append(INVENTARIO, nuevo)
    print_exito(f"Producto agregado con éxito. Código generado: {pid}")
    guardar_inventario()

def modificar_producto():
    print("\n[Modificar Producto]")
    pid = input("Ingrese Código del producto a modificar: ")
    idx = buscar_producto_por_id(pid)
    
    if idx == -1:
        print("Producto no encontrado.")
        return
    
    global INVENTARIO
    # Accedemos a la lista global para modificar el elemento mutable (lista interna)
    # Nota: Modificar el contenido de INVENTARIO[idx] NO requiere 'global INVENTARIO' 
    # si no reasignamos INVENTARIO. Pero por seguridad lo dejamos si fueramos a reasignar.
    # En este caso, modificamos prod que es referencia. 
    
    prod = INVENTARIO[idx]
    print(f"Valor actual - Nombre: {prod[1]}, Categ: {prod[2]}, Precio: {prod[3]}")
    
    n_nombre = input("Nuevo Nombre (Enter conserva actual): ").strip()
    if mi_len(n_nombre) > 0:
        if n_nombre.lower() != prod[1].lower() and producto_existe_nombre(n_nombre):
             print("Error: Nombre ya existe en otro producto.")
             return
        prod[1] = n_nombre
        
    n_cat = input("Nueva Categoría (Enter conserva actual): ").strip()
    if mi_len(n_cat) > 0:
        prod[2] = n_cat
        
    n_precio = input("Nuevo Precio (Enter conserva actual): ").strip()
    if mi_len(n_precio) > 0:
        try:
            val = int(n_precio)
            if val >= 0:
                prod[3] = val
            else:
                print("Precio negativo ignorado.")
        except:
            print("Precio inválido ignorado.")
            
    print("Producto modificado.")
    guardar_inventario()

def borrar_producto():
    global INVENTARIO
    print("\n[Borrar Producto]")
    pid = input("Código a borrar: ")
    idx = buscar_producto_por_id(pid)
    if idx == -1:
        print("No existe.")
        return
    
    prod = INVENTARIO[idx]
    
    if producto_fue_vendido(prod[0]):
        print("Error: No se puede borrar un producto que ha sido facturado.")
        return

    confirm = input(f"¿Está seguro de que desea borrar el producto {prod[0]}: {prod[1]}? (Si/No): ").lower()
    if confirm == "si":
        INVENTARIO = mi_remove(INVENTARIO, prod)
        print("Producto eliminado.")
        guardar_inventario()
    else:
        print("Cancelado.")

def agregar_stock():
    print("\n[Agregar Inventario]")
    pid = input("Código de producto: ")
    idx = buscar_producto_por_id(pid)
    if idx == -1:
        print("No existe.")
        return
        
    try:
        cant = int(input("Cantidad a agregar: "))
        if cant > 0:
            # Modificación in-place, no requiere global estricto, pero buena práctica
            INVENTARIO[idx][4] += cant
            print(f"Nuevo stock: {INVENTARIO[idx][4]}")
            guardar_inventario()
        else:
            print("Debe ser mayor a cero.")
    except:
        print("Dato inválido.")

def reporte_productos_simple():
    print("\n[Reporte de Productos]")
    print(f"{'Código':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
    print("-" * 55)
    for p in INVENTARIO:
        print(f"{p[0]:<10} {p[1]:<20} {p[3]:<10} {p[4]:<10}")

# ==========================================
# Módulo de Facturación
# ==========================================

def modulo_facturacion():
    print("\n--- FACTURACIÓN ---")
    cliente = input("Nombre de cliente: ").strip()
    if mi_len(cliente) == 0:
        print("Nombre obligatorio.")
        return
        
    carrito = [] # Lista de [producto_ref, cantidad_compra]
    
    while True:
        pid = input("Código del producto a comprar (FIN para terminar): ").strip()
        if pid.upper() == "FIN":
            if mi_len(carrito) == 0:
                print("No compró nada. Cancelando.")
                return
            break
            
        idx = buscar_producto_por_id(pid)
        if idx == -1:
            print("Producto no encontrado.")
            continue
            
        prod = INVENTARIO[idx]
        print(f"Producto: {prod[1]} | Disponible: {prod[4]}")
        
        try:
            cant = int(input("Cantidad por comprar: "))
            if cant <= 0:
                print("Cantidad debe ser positiva.")
                continue
                
            if cant > prod[4]:
                print("No hay suficiente inventario.")
                continue
                
            # Restar de inventario RAM temporalmente (se guarda al finalizar factura)
            INVENTARIO[idx][4] -= cant
            carrito = mi_append(carrito, [prod, cant])
            
            # Detalle en pantalla
            precio = prod[3]
            subt = precio * cant
            imp = subt * 0.13
            tot = subt + imp
            print(f"{cant} x {prod[1]} | Unit: {precio} | Imp: {imp:.2f} | Total: {tot:.2f}")
            
        except ValueError:
            print("Cantidad inválida.")

    # Generar Factura Final
    fecha, hora = obtener_fecha_hora()
    
    # Calcular totales
    subtotal_gral = 0
    impuesto_gral = 0
    total_gral = 0
    
    print("\n" + "="*40)
    # Generar ID Factura
    cargar_facturas() # Sync
    id_factura = str(mi_len(FACTURAS) + 1)
    
    print(f"Factura {id_factura}")
    print(f"Fecha: {fecha} Hora: {hora}")
    print(f"Cliente: {cliente}")
    print(f"{COLOR_CYAN}{'Cant':<5} {'Producto':<15} {'Precio':<8} {'Imp':<8} {'Total':<8}{COLOR_RESET}")
    print(COLOR_MAGENTA + "-"*50 + COLOR_RESET)
    
    detalles_para_guardar = []
    
    for item in carrito:
        p = item[0]
        cant = item[1]
        precio = p[3]
        subt = precio * cant
        imp = subt * 0.13
        tot = subt + imp
        
        subtotal_gral += subt
        impuesto_gral += imp
        total_gral += tot
        
        print(f"{cant:<5} {p[1]:<15} {precio:<8} {imp:<8.0f} {tot:<8.0f}")
        
        # Preparar detalle
        # id_fact, id_prod, nombre, cant, precio, subt, imp, tot
        d = [
            id_factura, 
            p[0], 
            p[1], 
            str(cant), 
            str(precio), 
            str(int(subt)), 
            str(int(imp)), 
            str(int(tot))
        ]
        detalles_para_guardar = mi_append(detalles_para_guardar, d)
        
    print(COLOR_MAGENTA + "-" * 50 + COLOR_RESET)
    print(f"Sub total: {subtotal_gral:.0f}")
    print(f"Impuestos: {impuesto_gral:.0f}")
    print(f"{COLOR_GREEN}Total: {total_gral:.0f}{COLOR_RESET}")
    
    pago = input("Forma de pago (Efectivo/Sinpe/Tarjeta): ").capitalize()
    
    # Guardar
    # id, client, date, time, sub, tax, total, pay
    encabezado = [
        id_factura, 
        cliente, 
        fecha, 
        hora, 
        str(int(subtotal_gral)), 
        str(int(impuesto_gral)), 
        str(int(total_gral)), 
        pago
    ]
    
    guardar_nueva_factura(encabezado, detalles_para_guardar)
    guardar_inventario() # Confirmar resta de stock
    print("Factura guardada con éxito.")

# ==========================================
# Módulo de Reportes
# ==========================================


def reporte_rango_fechas():
    print("\n[Reporte por Rango de Fechas]")
    print("Formato DD/MM/AAAA (Ej: 30/03/2023)")
    f_inicio = input("Fecha Inicio: ").strip()
    f_fin = input("Fecha Fin: ").strip()
    
    # Parsear fechas manualmente a datetimes si es necesario o comparar strings
    # Dado que no podemos usar librerias externas complejas y el formato es fijo importado
    # Trataremos de convertir a enteros YYYYMMDD para comparar
    
    def fecha_a_entero(s):
        # s = 30/03/2023 -> 20230330
        partes = mi_split(s, "/")
        if mi_len(partes) == 3:
            return int(partes[2] + partes[1] + partes[0])
        return 0
        
    ini_val = fecha_a_entero(f_inicio)
    fin_val = fecha_a_entero(f_fin)
    
    if ini_val == 0 or fin_val == 0:
        print("Formato de fecha inválido.")
        return
        
    print(f"{'#':<5}{'Fecha':<12}{'Cliente':<20}{'Total':<10}")
    suma = 0
    encontrados = []
    
    for f in FACTURAS:
        # f[2] es la fecha string
        f_val = fecha_a_entero(f[2])
        if f_val >= ini_val and f_val <= fin_val:
            print(f"{f[0]:<5}{f[2]:<12}{f[1]:<20}{f[6]:<10}")
            try:
                suma += int(f[6])
                encontrados = mi_append(encontrados, f)
            except: pass
            
    print("-" * 47)
    print(f"TOTAL: {suma}")
    
    # Opcional Exportar
    preg = input("¿Exportar reporte? (s/n): ")
    if preg.lower() == "s":
        nombre = input("Nombre archivo: ")
        try:
            archivo = open(nombre, "w")
            archivo.write(f"REPORTE RANGO {f_inicio} - {f_fin}\n")
            for f in encontrados:
                archivo.write(f"{f[0]},{f[2]},{f[1]},{f[6]}\n")
            archivo.write(f"TOTAL,{suma}\n")
            archivo.close()
            print("Exportado.")
        except:
             print("Error escribiendo archivo.")

def modulo_reportes():
    cargar_facturas()
    while True:
        print("\n--- REPORTES ---")
        print("1. Reporte de Productos (Filtrados)")
        print("2. Reporte de Facturas")
        print("3. Reporte por Producto Vendido")
        print("4. Reporte por Cliente")
        print("5. Estado de Utilidades")
        print("6. Reporte por Rango de Fechas")
        print("7. Salir")
        
        op = input("Opción: ")
        
        if op == "7":
            break
        elif op == "1":
            submenu_reportes_productos()
        elif op == "2":
            reporte_facturas()
        elif op == "3":
            reporte_producto_vendido()
        elif op == "4":
            reporte_cliente()
        elif op == "5":
            estado_utilidades()
        elif op == "6":
            reporte_rango_fechas()
        else:
            print("Inválido.")

def submenu_reportes_productos():
    print("\n[Reportes de Productos]")
    print("a. Todos los productos")
    print("b. Por Categoría")
    print("c. Por Existencia (>0)")
    o = input("Opción: ").lower()
    
    lista = []
    if o == "a":
        lista = INVENTARIO
    elif o == "b":
        cat = input("Categoría (parcial): ").lower()
        for p in INVENTARIO:
            if cat in p[2].lower():
                lista = mi_append(lista, p)
    elif o == "c":
        for p in INVENTARIO:
            if p[4] > 0:
                lista = mi_append(lista, p)
    
    imprimir_header("REPORTE DE PRODUCTOS")
    print(f"{COLOR_CYAN}{'Cod':<5}{'Nombre':<20}{'Precio':<10}{'Stock':<5}{COLOR_RESET}")
    print(COLOR_MAGENTA + "-"*45 + COLOR_RESET)
    for p in lista:
         color_stock = COLOR_GREEN if p[4] > 5 else COLOR_RED
         print(f"{p[0]:<5}{p[1]:<20}{p[3]:<10}{color_stock}{p[4]:<5}{COLOR_RESET}")
         
    preg = input("¿Exportar a archivo? (s/n): ")
    if preg.lower() == "s":
        nombre = input("Nombre archivo: ")
        try:
            f = open(nombre, "w")
            f.write("REPORTE PRODUCTOS\n")
            for p in lista:
                 f.write(f"{p[0]},{p[1]},{p[3]},{p[4]}\n")
            f.close()
            print("Exportado.")
        except:
            print("Error exportando.")

def reporte_facturas():
    imprimir_header("REPORTE DE FACTURAS")
    print(f"{COLOR_CYAN}{'#':<5}{'Fecha':<12}{'Cliente':<20}{'Total':<10}{COLOR_RESET}")
    print(COLOR_MAGENTA + "-"*47 + COLOR_RESET)
    suma = 0
    # id,client,date,time,sub,tax,total,pay
    for f in FACTURAS:
        print(f"{f[0]:<5}{f[2]:<12}{f[1]:<20}{f[6]:<10}")
        try:
            suma += int(f[6])
        except: pass
    print(COLOR_MAGENTA + "-" * 47 + COLOR_RESET)
    print(f"{COLOR_GREEN}TOTAL: {suma}{COLOR_RESET}")
    input("Enter para continuar...")

def reporte_producto_vendido():
    nombre = input("Nombre producto (parcial): ").lower()
    print(f"Producto buscado: {nombre}")
    print(f"{'#Fact':<6}{'Fecha':<12}{'Precio':<8}{'Cant':<5}{'Imp':<8}{'Total':<8}")
    
    suma_total = 0
    
    # Recorrer detalles
    for det in DETALLE_FACTURAS:
        # det: id_fact, id_prod, nombre, cant, precio, subt, imp, tot
        prod_nom = det[2].lower()
        if nombre in prod_nom:
            # Buscar fecha de factura
            fecha = ""
            for fac in FACTURAS:
                if fac[0] == det[0]:
                    fecha = fac[2]
                    break
            
            print(f"{det[0]:<6}{fecha:<12}{det[4]:<8}{det[3]:<5}{det[6]:<8}{det[7]:<8}")
            try:
                suma_total += int(det[7])
            except: pass
            
    print("-" * 50)
    print(f"TOTAL VENDIDO: {suma_total}")

def reporte_cliente():
    nombre = input("Nombre cliente (parcial): ").lower()
    print(f"Cliente buscado: {nombre}")
    print(f"{'#Fact':<6}{'Fecha':<12}{'Total':<10}")
    suma = 0
    for f in FACTURAS:
        if nombre in f[1].lower():
            print(f"{f[0]:<6}{f[2]:<12}{f[6]:<10}")
            try:
                suma += int(f[6])
            except: pass
    print(f"TOTAL: {suma}")

def estado_utilidades():
    total_facturas = mi_len(FACTURAS)
    
    # Productos únicos vendidos
    prods_vendidos = []
    for d in DETALLE_FACTURAS:
        pid = d[1]
        ya_esta = False
        for x in prods_vendidos:
            if x == pid: 
                ya_esta = True
        if not ya_esta:
            prods_vendidos = mi_append(prods_vendidos, pid)
    
    cant_unicos = mi_len(prods_vendidos)
    
    sub_total = 0
    imp = 0
    tot = 0
    
    for f in FACTURAS:
        try:
            sub_total += int(f[4])
            imp += int(f[5])
            tot += int(f[6])
        except: pass
        
    print("\n[Estado de Utilidades]")
    print(f"Total Facturas: {total_facturas}")
    print(f"Cant. productos facturados únicos: {cant_unicos}")
    print(f"SubTotal Facturado: {sub_total}")
    print(f"Total Impuesto: {imp}")
    print(f"Total Facturado: {tot}")

def main():
    cargar_usuarios()
    if mi_len(USUARIOS) == 0:
        # Fallback si no existe archivo
        pass
        
    menu_principal()

if __name__ == "__main__":
    main()

