# Solucion modularizando todo con funciones.

def leer_numero_reservas():
    cantidad_reservas = int(input("Ingrese el número de reservas: "))
    while cantidad_reservas < 1:
        print("El número de reservas debe ser al menos 1.")
        cantidad_reservas = int(input("Ingrese el número de reservas: "))
    return cantidad_reservas

def leer_numero_noches():
    noches = int(input("Ingrese el número de noches: "))
    while noches < 1:
        print("El número de noches debe ser al menos 1.")
        noches = int(input("Ingrese el número de noches: "))
    return noches

def leer_tipo_habitacion():
    tipo_habitacion = int(input("Ingrese el tipo de habitación (1: Estándar, 2: Suite, 3: Premium): "))
    while tipo_habitacion not in [1, 2, 3]:
        print("Tipo de habitación inválido. Por favor ingrese 1, 2, o 3.")
        tipo_habitacion = int(input("Ingrese el tipo de habitación (1: Estándar, 2: Suite, 3: Premium): "))
    return tipo_habitacion

def leer_numero_huespedes(capacidad):
    huespedes = int(input("Ingrese el número de huéspedes: "))
    while huespedes < 1 or huespedes > capacidad:
        print(f"Número de huéspedes inválido. Debe estar entre 1 y {capacidad}.")
        huespedes = int(input("Ingrese el número de huéspedes: "))
    return huespedes

def leer_servicios():
    servicios = {}
    for servicio in ['EP', 'CS', 'DB', 'SPA']:
        servicio_input = int(input(f"¿Desea {servicio} (0: No, 1: Sí): "))
        while servicio_input not in [0, 1]:
            print("Entrada inválida. Por favor ingrese 0 o 1.")
            servicio_input = int(input(f"¿Desea {servicio} (0: No, 1: Sí): "))
        servicios[servicio] = servicio_input
    return servicios

def leer_porcentaje_propina():
    porcentaje_propina = int(input("Ingrese el porcentaje de propina: "))
    while porcentaje_propina < 0:
        print("El porcentaje de propina debe ser al menos 0.")
        porcentaje_propina = int(input("Ingrese el porcentaje de propina: "))
    return porcentaje_propina

def calcular_costo_base(tipo_habitacion, noches, tarifas_habitacion):
    return tarifas_habitacion[tipo_habitacion] * noches

def calcular_costo_servicios(servicios, noches, huespedes, servicios_adicionales_habitacion, servicios_adicionales_persona):
    costo_servicios_adicionales = sum(servicios[s] * servicios_adicionales_habitacion.get(s, 0) for s in servicios) * noches
    costo_servicios_adicionales += sum(servicios[s] * servicios_adicionales_persona.get(s, 0) for s in servicios) * huespedes * noches
    return costo_servicios_adicionales

def aplicar_descuento(subtotal, noches, descuentos):
    for min_noches, tasa_descuento in descuentos:
        if noches >= min_noches:
            return subtotal * (1 - tasa_descuento)
    return subtotal

def calcular_impuesto(subtotal, tipo_habitacion, tasas_impuesto):
    return subtotal * tasas_impuesto[tipo_habitacion]

def calcular_costo_total(subtotal, impuesto, porcentaje_propina):
    return subtotal + impuesto + (subtotal * porcentaje_propina / 100)

def determinar_categoria_reserva(servicios):
    cantidad_servicios = sum(servicios.values())
    if cantidad_servicios == 0:
        return "Básica"
    elif cantidad_servicios == 1:
        return "Clásica"
    else:
        return "Top"

def imprimir_resultados(subtotal, impuesto, costo_total):
    print(f"Subtotal: ${round(subtotal, 0)}")
    print(f"Impuesto: ${round(impuesto, 0)}")
    print(f"Costo total: ${round(costo_total, 0)}")

def imprimir_estadisticas(reservas_suite, reservas_sin_servicios, reservas_con_servicios_adicionales, reservas_estandar_largas, reservas_top, subtotal_mas_alto, reservas_premium_con_mensaje, reservas_costosas, cantidad_reservas):
    print(f"Porcentaje de reservas para habitación Suite: {round((reservas_suite / cantidad_reservas) * 100, 2)}%")
    print(f"Número de reservas sin servicios adicionales: {reservas_sin_servicios}")
    print(f"Porcentaje de reservas con al menos un servicio adicional: {round((reservas_con_servicios_adicionales / cantidad_reservas) * 100, 2)}%")
    print(f"Número de habitaciones Estándar reservadas por más de 10 noches: {reservas_estandar_largas}")
    print(f"Número de reservas Top: {reservas_top}")
    print(f"Subtotal más alto: ${round(subtotal_mas_alto, 0)}")
    print(f"Número de reservas en habitación Premium con mensaje de bienvenida: {reservas_premium_con_mensaje}")
    print(f"Número de reservas con un costo total de al menos $1,000,000: {reservas_costosas}")
