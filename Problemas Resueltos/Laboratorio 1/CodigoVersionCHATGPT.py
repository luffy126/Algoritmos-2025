# Solucion desarrollada exclusivamente por ChatGPT.

import math

# --- CONSTANTES ---
PRECIOS_HABITACION = {1: 45000, 2: 80000, 3: 120000}
CAPACIDAD_HABITACION = {1: 2, 2: 4, 3: 6}
IMPUESTO_HABITACION = {1: 0.17, 2: 0.17, 3: 0.17}

# Servicios por habitación (precio por noche)
SERVICIOS_HABITACION = {
    'EP': 5000,
    'CS': 3000
}

# Servicios por persona (precio por persona por noche)
SERVICIOS_PERSONA = {
    'DB': 8000,
    'SPA': 12000
}

# Descuentos por cantidad de noches
DESCUENTOS_NOCHES = [
    (15, 0.15),
    (8, 0.10),
    (4, 0.05),
    (1, 0.0)
]

# Categorías por cantidad de servicios adicionales
def obtener_categoria(servicios_totales):
    if servicios_totales == 0:
        return "Básica"
    elif servicios_totales == 1:
        return "Clásica"
    else:
        return "Top"

# --- INGRESO DE DATOS ---
while True:
    try:
        cantidad_reservas = int(input("Ingrese la cantidad de reservas a procesar (mínimo 1): "))
        if cantidad_reservas >= 1:
            break
        else:
            print("Debe ingresar un número mayor o igual a 1.")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

# --- VARIABLES ESTADÍSTICAS ---
contador_suite = 0
contador_sin_servicios = 0
contador_con_servicio = 0
contador_estandar_mas_10 = 0
contador_top = 0
mayor_subtotal = 0
contador_premium_mensaje = 0
contador_mayor_millon = 0

# --- PROCESAR RESERVAS ---
for i in range(1, cantidad_reservas + 1):
    print(f"\n--- Reserva #{i} ---")
    
    # Leer cantidad de noches
    while True:
        try:
            noches = int(input("Ingrese la cantidad de noches: "))
            if noches > 0:
                break
            else:
                print("Debe ser mayor a 0.")
        except ValueError:
            print("Entrada inválida.")

    # Tipo de habitación
    while True:
        try:
            tipo = int(input("Tipo de habitación (1=Estándar, 2=Suite, 3=Premium): "))
            if tipo in [1, 2, 3]:
                break
            else:
                print("Debe ingresar 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida.")

    if tipo == 2:
        contador_suite += 1

    # Número de huéspedes
    while True:
        try:
            huespedes = int(input(f"Ingrese número de huéspedes (máx {CAPACIDAD_HABITACION[tipo]}): "))
            if 0 < huespedes <= CAPACIDAD_HABITACION[tipo]:
                break
            else:
                print("Cantidad inválida para esta habitación.")
        except ValueError:
            print("Entrada inválida.")

    # Servicios adicionales
    servicios_solicitados = {}
    total_servicios = 0

    for s in ['EP', 'CS', 'DB', 'SPA']:
        while True:
            try:
                valor = int(input(f"¿Desea {s}? (1=Sí, 0=No): "))
                if valor in [0, 1]:
                    servicios_solicitados[s] = valor
                    if valor == 1:
                        total_servicios += 1
                    break
                else:
                    print("Debe ingresar 0 o 1.")
            except ValueError:
                print("Entrada inválida.")

    # Propina
    while True:
        try:
            propina_porcentaje = int(input("Ingrese porcentaje de propina (%): "))
            if propina_porcentaje >= 0:
                break
            else:
                print("Debe ser 0 o más.")
        except ValueError:
            print("Entrada inválida.")

    # --- CÁLCULOS ---
    subtotal = noches * PRECIOS_HABITACION[tipo]

    # Servicios por habitación
    for s in ['EP', 'CS']:
        if servicios_solicitados[s]:
            subtotal += noches * SERVICIOS_HABITACION[s]

    # Servicios por persona
    for s in ['DB', 'SPA']:
        if servicios_solicitados[s]:
            subtotal += noches * huespedes * SERVICIOS_PERSONA[s]

    # Guardar para estadísticas
    if total_servicios == 0:
        contador_sin_servicios += 1
    else:
        contador_con_servicio += 1

    if tipo == 1 and noches > 10:
        contador_estandar_mas_10 += 1

    # Descuento por noches
    descuento = 0
    for rango, porc in DESCUENTOS_NOCHES:
        if noches >= rango:
            descuento = porc
            break

    subtotal_descuento = subtotal * (1 - descuento)
    mayor_subtotal = max(mayor_subtotal, subtotal_descuento)

    # Impuesto
    impuesto = subtotal_descuento * IMPUESTO_HABITACION[tipo]

    # Propina
    propina = subtotal_descuento * (propina_porcentaje / 100)

    # Total
    total_final = round(subtotal_descuento + impuesto + propina)

    # Estadística Top
    categoria = obtener_categoria(total_servicios)
    if categoria == "Top":
        contador_top += 1

    # Estadística Premium
    if tipo == 3:
        contador_premium_mensaje += 1

    if total_final >= 1_000_000:
        contador_mayor_millon += 1

    print(f"Subtotal con descuento: ${round(subtotal_descuento)}")
    print(f"Total con impuestos y propina: ${total_final}")
    print(f"Categoría de la reserva: {categoria}")

# --- ESTADÍSTICAS FINALES ---
print("\n--- Estadísticas Finales ---")
print(f"Porcentaje de reservas en habitación SUITE: {round((contador_suite / cantidad_reservas) * 100)}%")
print(f"Reservas sin servicios adicionales: {contador_sin_servicios}")
print(f"Porcentaje con al menos un servicio: {round((contador_con_servicio / cantidad_reservas) * 100)}%")
print(f"Habitaciones ESTÁNDAR con más de 10 noches: {contador_estandar_mas_10}")
print(f"Cantidad de reservas TOP: {contador_top}")
print(f"Subtotal más alto: ${round(mayor_subtotal)}")
print(f"Reservas Premium con mensaje de categoría: {contador_premium_mensaje}")
print(f"Reservas con valor >= $1.000.000: {contador_mayor_millon}")
