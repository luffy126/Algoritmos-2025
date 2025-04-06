# --- INGRESO DE DATOS ---
cantidadReservas = int(input("Ingrese la cantidad de reservas a procesar (mínimo 1): "))
while cantidadReservas < 1:
    print("Debe ingresar un número mayor o igual a 1.")
    cantidadReservas = int(input("Ingrese la cantidad de reservas a procesar (mínimo 1): "))

# --- VARIABLES ---
contadorSuite = 0
contadorSinServicios = 0
contadorConServicio = 0
contadorEstandarMas10 = 0
contadorTop = 0
mayorSubtotal = 0
contadorPremiumMensaje = 0
contadorMayorMillon = 0

# --- PROCESAR RESERVAS ---
for i in range(1, cantidadReservas + 1):
    print(f"\n--- Reserva #{i} ---")
    
    # Leer cantidad de noches
    noches = int(input("Ingrese la cantidad de noches: "))
    while noches <= 0:
        print("Debe ser mayor a 0.")
        noches = int(input("Ingrese la cantidad de noches: "))
    
    # Tipo de habitación
    tipo = int(input("Tipo de habitación (1=Estándar, 2=Suite, 3=Premium): "))
    while tipo not in [1, 2, 3]:
        print("Debe ingresar 1, 2 o 3.")
        tipo = int(input("Tipo de habitación (1=Estándar, 2=Suite, 3=Premium): "))

    if tipo == 2:
        contadorSuite += 1

    # Número de huéspedes
    if tipo == 1:
        capacidadHabitacion = 2
    elif tipo == 2:
        capacidadHabitacion = 4
    else:
        capacidadHabitacion = 6
        
    huespedes = int(input(f"Ingrese número de huéspedes (máx {capacidadHabitacion}): "))
    while huespedes <= 0 or huespedes > capacidadHabitacion:
        print("Cantidad inválida para esta habitación.")
        huespedes = int(input(f"Ingrese número de huéspedes (máx {capacidadHabitacion}): "))

    # Servicios adicionales
    serviciosSolicitados = {'EP': 0, 'CS': 0, 'DB': 0, 'SPA': 0}
    totalServicios = 0

    for servicio in serviciosSolicitados:
        valor = int(input(f"¿Desea {servicio}? (1=Sí, 0=No): "))
        while valor not in [0, 1]:
            print("Debe ingresar 0 o 1.")
            valor = int(input(f"¿Desea {servicio}? (1=Sí, 0=No): "))
        serviciosSolicitados[servicio] = valor
        if valor == 1:
            totalServicios += 1

    # Propina
    propinaPorcentaje = int(input("Ingrese porcentaje de propina (%): "))
    while propinaPorcentaje < 0:
        print("Debe ser 0 o más.")
        propinaPorcentaje = int(input("Ingrese porcentaje de propina (%): "))

    # --- CÁLCULOS ---
    if tipo == 1:
        precioHabitacion = 45000
    elif tipo == 2:
        precioHabitacion = 80000
    else:
        precioHabitacion = 120000
        
    subtotal = noches * precioHabitacion

    # Servicios por habitación
    if serviciosSolicitados['EP'] == 1:
        subtotal += noches * 5000
    if serviciosSolicitados['CS'] == 1:
        subtotal += noches * 3000

    # Servicios por persona
    if serviciosSolicitados['DB'] == 1:
        subtotal += noches * huespedes * 8000
    if serviciosSolicitados['SPA'] == 1:
        subtotal += noches * huespedes * 12000

    # Guardar para estadísticas
    if totalServicios == 0:
        contadorSinServicios += 1
    else:
        contadorConServicio += 1

    if tipo == 1 and noches > 10:
        contadorEstandarMas10 += 1

    # Descuento por noches
    descuento = 0
    if noches >= 15:
        descuento = 0.15
    elif noches >= 8:
        descuento = 0.10
    elif noches >= 4:
        descuento = 0.05

    subtotalDescuento = subtotal * (1 - descuento)
    if subtotalDescuento > mayorSubtotal:
        mayorSubtotal = subtotalDescuento

    # Impuesto
    impuesto = subtotalDescuento * 0.17

    # Propina
    propina = subtotalDescuento * (propinaPorcentaje / 100)

    # Total
    totalFinal = round(subtotalDescuento + impuesto + propina)

    # Estadística Top
    if totalServicios == 0:
        categoria = "Basica"
    elif totalServicios == 1:
        categoria = "Clasica"
    else:
        categoria = "Top"
        
    if categoria == "Top":
        contadorTop += 1

    # Estadística Premium
    if tipo == 3:
        contadorPremiumMensaje += 1

    if totalFinal >= 1000000:
        contadorMayorMillon += 1

    print(f"Subtotal con descuento: ${round(subtotalDescuento)}")
    print(f"Total con impuestos y propina: ${totalFinal}")
    print(f"Categoría de la reserva: {categoria}")

# --- ESTADÍSTICAS FINALES ---
print("\n--- Estadísticas Finales ---")
print(f"Porcentaje de reservas en habitación SUITE: {round((contadorSuite / cantidadReservas) * 100)}%")
print(f"Reservas sin servicios adicionales: {contadorSinServicios}")
print(f"Porcentaje con al menos un servicio: {round((contadorConServicio / cantidadReservas) * 100)}%")
print(f"Habitaciones ESTÁNDAR con más de 10 noches: {contadorEstandarMas10}")
print(f"Cantidad de reservas TOP: {contadorTop}")
print(f"Subtotal más alto: ${round(mayorSubtotal)}")
print(f"Reservas Premium con mensaje de categoría: {contadorPremiumMensaje}")
print(f"Reservas con valor >= $1.000.000: {contadorMayorMillon}")
