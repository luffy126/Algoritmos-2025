# 1. Solicitar al usuario el sueldo mensual bruto.
# 2. Solicitar al usuario el porcentaje de bonificación.
# 3. Calcular la bonificación multiplicando el sueldo mensual bruto por el porcentaje de bonificación dividido por 100.
# 4. Calcular el monto bruto total sumando el sueldo mensual bruto y la bonificación.
# 5. Mostrar el monto bruto total.

def calcularMontoBrutoTotal(sueldoMensualBruto, porcentajeBonificacion):
    bonificacion = sueldoMensualBruto * (porcentajeBonificacion / 100)
    montoBrutoTotal = sueldoMensualBruto + bonificacion
    return montoBrutoTotal

# Solicitar al usuario el sueldo mensual bruto y el porcentaje de bonificación
sueldoMensualBruto = float(input("Ingrese el sueldo mensual bruto: "))
porcentajeBonificacion = float(input("Ingrese el porcentaje de bonificación: "))

# Calcular el monto bruto total
montoBrutoTotal = calcularMontoBrutoTotal(sueldoMensualBruto, porcentajeBonificacion)

# Mostrar el monto bruto total
print(f"El monto bruto total que recibirá el obrero es: {montoBrutoTotal}")
