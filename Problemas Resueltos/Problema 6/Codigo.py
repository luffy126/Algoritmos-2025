def calcularCuotaIndividual(totalAlcoholGel, precioAlcoholGel, totalMascarillas, precioMascarillas, totalSocios):
    totalGastado = (totalAlcoholGel * precioAlcoholGel) + (totalMascarillas * precioMascarillas)
    cuotaIndividual = totalGastado / totalSocios
    return cuotaIndividual

# Datos de ejemplo
totalAlcoholGel = 50  # Total de botellas de alcohol en gel
precioAlcoholGel = 3.5  # Precio de cada botella de alcohol en gel
totalMascarillas = 100  # Total de cajas de mascarillas desechables
precioMascarillas = 10  # Precio de cada caja de mascarillas desechables
totalSocios = 20  # Total de socios del sindicato

cuota = calcularCuotaIndividual(totalAlcoholGel, precioAlcoholGel, totalMascarillas, precioMascarillas, totalSocios)
print(f"La cuota individual que cada socio deberá pagar es: ${cuota:.2f}")
