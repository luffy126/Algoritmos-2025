def calcular_inversion_y_precio_venta(n_cajas, costo_por_caja, tipo_cambio):
    # Paso 1: Calcular el costo total en dólares
    costo_total_usd = n_cajas * costo_por_caja
    
    # Paso 2: Convertir el costo total a pesos chilenos
    costo_total_clp = costo_total_usd * tipo_cambio
    
    # Paso 3: Calcular el costo por mascarilla
    n_mascarillas = n_cajas * 50
    costo_por_mascarilla_clp = costo_total_clp / n_mascarillas
    
    # Paso 4: Calcular el precio de venta con 100% de ganancia y agregar IVA del 19%
    precio_venta_sin_iva = costo_por_mascarilla_clp * 2  # 100% de ganancia
    precio_venta_con_iva = precio_venta_sin_iva * 1.19   # Agregar 19% de IVA
    
    return costo_total_clp, precio_venta_con_iva

# Ejemplo de uso
n_cajas = 10  # Número de cajas
costo_por_caja = 20  # Costo de cada caja en dólares
tipo_cambio = 800  # Tipo de cambio USD a CLP

costo_total_clp, precio_venta_con_iva = calcular_inversion_y_precio_venta(n_cajas, costo_por_caja, tipo_cambio)

print(f"Inversión total en pesos chilenos: {costo_total_clp} CLP")
print(f"Precio de venta por mascarilla con IVA: {precio_venta_con_iva} CLP")
