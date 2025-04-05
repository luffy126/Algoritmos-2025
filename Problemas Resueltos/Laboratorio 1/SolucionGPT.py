# Solucion desarrollada con ChatGPT y Copilot.
import math
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

# --- VARIABLES ---
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
            capacidad_habitacion = 2 if tipo == 1 else (4 if tipo == 2 else 6)
            huespedes = int(input(f"Ingrese número de huéspedes (máx {capacidad_habitacion}): "))
            if 0 < huespedes <= capacidad_habitacion:
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
    precio_habitacion = 45000 if tipo == 1 else (80000 if tipo == 2 else 120000)
    subtotal = noches * precio_habitacion

    # Servicios por habitación
    for s in ['EP', 'CS']:
        if servicios_solicitados[s]:
            subtotal += noches * (5000 if s == 'EP' else 3000)

    # Servicios por persona
    for s in ['DB', 'SPA']:
        if servicios_solicitados[s]:
            subtotal += noches * huespedes * (8000 if s == 'DB' else 12000)

    # Guardar para estadísticas
    if total_servicios == 0:
        contador_sin_servicios += 1
    else:
        contador_con_servicio += 1

    if tipo == 1 and noches > 10:
        contador_estandar_mas_10 += 1

    # Descuento por noches
    descuento = 0
    if noches >= 15:
        descuento = 0.15
    elif noches >= 8:
        descuento = 0.10
    elif noches >= 4:
        descuento = 0.05

    subtotal_descuento = subtotal * (1 - descuento)
    mayor_subtotal = max(mayor_subtotal, subtotal_descuento)

    # Impuesto
    impuesto = subtotal_descuento * 0.17

    # Propina
    propina = subtotal_descuento * (propina_porcentaje / 100)

    # Total
    total_final = round(subtotal_descuento + impuesto + propina)

    # Estadística Top
    categoria = "Básica" if total_servicios == 0 else ("Clásica" if total_servicios == 1 else "Top")
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
