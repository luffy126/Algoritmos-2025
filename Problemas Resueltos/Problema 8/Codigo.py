def calcularInversionYPrecioVenta(nCajas, costoPorCaja, tipoCambio):
    # Paso 1: Calcular el costo total en dólares
    costoTotalUsd = nCajas * costoPorCaja
    
    # Paso 2: Convertir el costo total a pesos chilenos
    costoTotalClp = costoTotalUsd * tipoCambio
    
    # Paso 3: Calcular el costo por mascarilla
    nMascarillas = nCajas * 50
    costoPorMascarillaClp = costoTotalClp / nMascarillas
    
    # Paso 4: Calcular el precio de venta con 100% de ganancia y agregar IVA del 19%
    precioVentaSinIva = costoPorMascarillaClp * 2  # 100% de ganancia
    precioVentaConIva = precioVentaSinIva * 1.19   # Agregar 19% de IVA
    
    return costoTotalClp, precioVentaConIva

# Ejemplo de uso
nCajas = 10  # Número de cajas
costoPorCaja = 20  # Costo de cada caja en dólares
tipoCambio = 980  # Tipo de cambio USD a CLP (VALOR DEL DOLAR: 4/4/2025)

costoTotalClp, precioVentaConIva = calcularInversionYPrecioVenta(nCajas, costoPorCaja, tipoCambio)

print(f"Inversión total en pesos chilenos: {costoTotalClp} CLP")
print(f"Precio de venta por mascarilla con IVA: {precioVentaConIva} CLP")
