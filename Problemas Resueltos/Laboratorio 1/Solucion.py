## leer cantidad de reservas

cantidadReservas = int(input("Ingrese la cantidad de reservas: "))

while cantidadReservas < 1:
    print("Debe ingresar un número mayor o igual a 1.")
    cantidadReservas = int(input("Ingrese la cantidad de reservas: "))

print(f"Cantidad de reservas a procesar: {cantidadReservas}")

## --- VARIABLES GLOBALES ---

contadorHabSuite = 0
contadorHabSinDescuento = 0
contadorHabEstandar = 0
contadorHabEstandarConDesayuno = 0
contadorCategoriaBasica = 0
cantidadPagadaCatBasica = 0
cantidadNochesCatTop = 0
contadorHabTop = 0
contadorHabMillonPesos = 0

### --- PROCESAMIENTO DE RESERVAS ---

for i in range(1, cantidadReservas + 1):
    print (f"\n--- Reserva #{i} ---")
    cantidadNochesReservadas = int(input("Ingrese la cantidad de noches reservadas: "))

    tipoHabitacion = int(input("Ingrese el tipo de habitación (1=Estándar, 2=Suite, 3=Premium): "))
    if tipoHabitacion == 2:
        contadorHabSuite += 1

    cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))

    if tipoHabitacion == 1:
        contadorHabEstandar += 1
        while cantidadHuespedes != 1 or cantidadHuespedes != 2:
            print("La cantidad de huéspedes debe ser 1 o 2.")
            cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))
    
    elif tipoHabitacion == 2:
        while cantidadHuespedes < 1 or cantidadHuespedes > 4:
            print("La cantidad de huéspedes debe ser entre 1 y 4.")
            cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))

    elif tipoHabitacion == 3:
        while cantidadHuespedes < 1 or cantidadHuespedes > 6:
            print("La cantidad de huéspedes debe ser entre 1 y 6.")
            cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))

    ## Servicios adicionales

    ep = int(input("¿Desea el servicio de EP? (1=Sí, 0=No): "))
    while ep != 0 and ep != 1:
        print("Debe ingresar 0 o 1.")
        ep = int(input("¿Desea el servicio de EP? (1=Sí, 0=No): "))

    cs = int(input("¿Desea el servicio de CS? (1=Sí, 0=No): "))
    while cs != 0 and cs != 1:
        print("Debe ingresar 0 o 1.")
        cs = int(input("¿Desea el servicio de CS? (1=Sí, 0=No): "))
    
    db = int(input("¿Desea el servicio de DB? (1=Sí, 0=No): "))
    while db != 0 and db != 1:
        print("Debe ingresar 0 o 1.")
        db = int(input("¿Desea el servicio de DB? (1=Sí, 0=No): "))

    if tipoHabitacion == 1 and db == 1:
        contadorHabEstandarConDesayuno += 1

    spa = int(input("¿Desea el servicio de SPA? (1=Sí, 0=No): "))
    while spa != 0 and spa != 1:
        print("Debe ingresar 0 o 1.")
        spa = int(input("¿Desea el servicio de SPA? (1=Sí, 0=No): "))

    ## Propina
    propina = int(input("Ingrese el porcentaje de propina: "))
    
    ## calculo SUBtotal
    ## precio de base de la habitación 
    ## servicios adicionales
    ## descuento por cantidad de noches

    precioSubTotal = 0

    ## Calculo del precio base de la habitación

    if tipoHabitacion == 1:
        precioSubTotal += 45000 * cantidadNochesReservadas
    elif tipoHabitacion == 2:
        precioSubTotal += 80000 * cantidadNochesReservadas
    elif tipoHabitacion == 3:
        precioSubTotal += 120000 * cantidadNochesReservadas

    ## Calculo de los servicios adicionales

    if ep == 1:
        precioSubTotal += 5000 * cantidadNochesReservadas
    if cs == 1:
        precioSubTotal += 3000 * cantidadNochesReservadas
    if db == 1:
        precioSubTotal += 8000 * cantidadNochesReservadas * cantidadHuespedes
    if spa == 1:
        precioSubTotal += 12000 * cantidadNochesReservadas * cantidadHuespedes

    ## Descuento por cantidad de noches

    montoDescontado = 0

    if cantidadNochesReservadas <= 3:
        montoDescontado = 0
        contadorHabSinDescuento += 1

    if cantidadNochesReservadas > 3 and cantidadNochesReservadas <= 7:
        montoDescontado = precioSubTotal * 0.05 ## 5% de descuento
    elif cantidadNochesReservadas > 7 and cantidadNochesReservadas <= 14:
        montoDescontado = precioSubTotal * 0.10 ## 10% de descuento
    elif cantidadNochesReservadas > 14:
        montoDescontado = precioSubTotal * 0.15 ## 15% de descuento

    precioSubtotalConDescuento = precioSubTotal - montoDescontado

    ## Suma de propina e impuesto

    precioFinal = precioSubtotalConDescuento
    precioFinal += precioSubtotalConDescuento * (propina / 100) ## propina

    if tipoHabitacion == 1 or tipoHabitacion == 2:
        precioFinal += precioSubtotalConDescuento * 0.12 ## Impuesto del 12%
    elif tipoHabitacion == 3:
        precioFinal += precioSubtotalConDescuento * 0.17 ## Impuesto del 17%

    if precioFinal > 1000000:
        contadorHabMillonPesos += 1

    ## Categoria de la reserva
    categoriaReserva = 0

    cantidadServiciosAdicionales = ep + cs + db + spa
    if cantidadServiciosAdicionales == 0:
        categoriaReserva = 1 ## Básica
        contadorCategoriaBasica += 1
        cantidadPagadaCatBasica += precioFinal

    elif cantidadServiciosAdicionales == 1:
        categoriaReserva = 2 ## Clásica

    elif cantidadServiciosAdicionales > 1:
        categoriaReserva = 3 ## Top
        contadorHabTop += 1
        cantidadNochesCatTop += cantidadNochesReservadas

## --- CALCULOS FINALES ---

porcentajeCantidadSuite = round((contadorHabSuite / cantidadReservas) * 100)
print(f"Porcentaje de habitaciones Suite: {porcentajeCantidadSuite: }%")

porcentajeHabSinDescuento = round((contadorHabSinDescuento / cantidadReservas) * 100)
print(f"Porcentaje de habitaciones sin descuento: {porcentajeHabSinDescuento: }%")

## Cantidad de reservas de categoría estandar
if contadorHabEstandar > 0:
    porcentajeHabEstandar = round((contadorHabEstandarConDesayuno / contadorHabEstandar) * 100)
    print(f"Porcentaje de habitaciones estándar con desayuno: {porcentajeHabEstandar: }%")
else:
    print("No se registraron habitaciones estándar.")

## Promedio pagado por categoría básica
if contadorCategoriaBasica > 0:
    promedioPagadoCatBasica = round(cantidadPagadaCatBasica / contadorCategoriaBasica)
    print(f"Promedio pagado por categoría básica: ${promedioPagadoCatBasica}")
else:
    print("No se registraron reservas de categoría básica.")

## Promedio de noches reservadas en categoría Top

if contadorHabTop > 0:
    promedioNochesReservadasTop = round(cantidadNochesCatTop / contadorHabTop)
    print(f"Promedio de noches reservadas en categoría Top: {promedioNochesReservadasTop} noches")
else:
    print("No se registraron reservas de categoría Top.")

## Cantidad de reservas que superaron el millón de pesos
if contadorHabMillonPesos > 0:
    print(f"Cantidad de reservas que superaron el millón de pesos: {contadorHabMillonPesos}")
else:
    print("No se registraron reservas que superaron el millón de pesos.")
