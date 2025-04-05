# Solucion modularizando todo con funciones.

def leerNumeroReservas():
    cantidadReservas = int(input("Ingrese el número de reservas: "))
    while cantidadReservas < 1:
        print("El número de reservas debe ser al menos 1.")
        cantidadReservas = int(input("Ingrese el número de reservas: "))
    return cantidadReservas

def leerNumeroNoches():
    noches = int(input("Ingrese el número de noches: "))
    while noches < 1:
        print("El número de noches debe ser al menos 1.")
        noches = int(input("Ingrese el número de noches: "))
    return noches

def leerTipoHabitacion():
    tipoHabitacion = int(input("Ingrese el tipo de habitación (1: Estándar, 2: Suite, 3: Premium): "))
    while tipoHabitacion not in [1, 2, 3]:
        print("Tipo de habitación inválido. Por favor ingrese 1, 2, o 3.")
        tipoHabitacion = int(input("Ingrese el tipo de habitación (1: Estándar, 2: Suite, 3: Premium): "))
    return tipoHabitacion

def leerNumeroHuespedes(capacidad):
    huespedes = int(input("Ingrese el número de huéspedes: "))
    while huespedes < 1 or huespedes > capacidad:
        print(f"Número de huéspedes inválido. Debe estar entre 1 y {capacidad}.")
        huespedes = int(input("Ingrese el número de huéspedes: "))
    return huespedes

def leerServicios():
    servicios = {}
    for servicio in ['EP', 'CS', 'DB', 'SPA']:
        servicioInput = int(input(f"¿Desea {servicio} (0: No, 1: Sí): "))
        while servicioInput not in [0, 1]:
            print("Entrada inválida. Por favor ingrese 0 o 1.")
            servicioInput = int(input(f"¿Desea {servicio} (0: No, 1: Sí): "))
        servicios[servicio] = servicioInput
    return servicios

def leerPorcentajePropina():
    porcentajePropina = int(input("Ingrese el porcentaje de propina: "))
    mientras porcentajePropina < 0:
        print("El porcentaje de propina debe ser al menos 0.")
        porcentajePropina = int(input("Ingrese el porcentaje de propina: "))
    return porcentajePropina

def calcularCostoBase(tipoHabitacion, noches, tarifasHabitacion):
    return tarifasHabitacion[tipoHabitacion] * noches

def calcularCostoServicios(servicios, noches, huespedes, serviciosAdicionalesHabitacion, serviciosAdicionalesPersona):
    costoServiciosAdicionales = sum(servicios[s] * serviciosAdicionalesHabitacion.get(s, 0) for s in servicios) * noches
    costoServiciosAdicionales += sum(servicios[s] * serviciosAdicionalesPersona.get(s, 0) for s in servicios) * huespedes * noches
    return costoServiciosAdicionales

def aplicarDescuento(subtotal, noches, descuentos):
    for minNoches, tasaDescuento in descuentos:
        if noches >= minNoches:
            return subtotal * (1 - tasaDescuento)
    return subtotal

def calcularImpuesto(subtotal, tipoHabitacion, tasasImpuesto):
    return subtotal * tasasImpuesto[tipoHabitacion]

def calcularCostoTotal(subtotal, impuesto, porcentajePropina):
    return subtotal + impuesto + (subtotal * porcentajePropina / 100)

def determinarCategoriaReserva(servicios):
    cantidadServicios = sum(servicios.values())
    if cantidadServicios == 0:
        return "Básica"
    elif cantidadServicios == 1:
        return "Clásica"
    else:
        return "Top"

def imprimirResultados(subtotal, impuesto, costoTotal):
    print(f"Subtotal: ${round(subtotal, 0)}")
    print(f"Impuesto: ${round(impuesto, 0)}")
    print(f"Costo total: ${round(costoTotal, 0)}")

def imprimirEstadisticas(reservasSuite, reservasSinServicios, reservasConServiciosAdicionales, reservasEstandarLargas, reservasTop, subtotalMasAlto, reservasPremiumConMensaje, reservasCostosas, cantidadReservas):
    print(f"Porcentaje de reservas para habitación Suite: {round((reservasSuite / cantidadReservas) * 100, 2)}%")
    print(f"Número de reservas sin servicios adicionales: {reservasSinServicios}")
    print(f"Porcentaje de reservas con al menos un servicio adicional: {round((reservasConServiciosAdicionales / cantidadReservas) * 100, 2)}%")
    print(f"Número de habitaciones Estándar reservadas por más de 10 noches: {reservasEstandarLargas}")
    print(f"Número de reservas Top: {reservasTop}")
    print(f"Subtotal más alto: ${round(subtotalMasAlto, 0)}")
    print(f"Número de reservas en habitación Premium con mensaje de bienvenida: {reservasPremiumConMensaje}")
    print(f"Número de reservas con un costo total de al menos $1,000,000: {reservasCostosas}")
