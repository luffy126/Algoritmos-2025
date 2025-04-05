import math

def calcularVolumenCilindro(diametro, altura):
    radio = diametro / 2
    volumen = math.pi * (radio ** 2) * altura
    return volumen

def calcularLitrosPorHabitante(volumenCilindro, numeroHabitantes):
    litrosPorHabitante = volumenCilindro / numeroHabitantes
    return litrosPorHabitante

diametro = float(input("Ingrese el diámetro del cilindro (en metros): "))
altura = float(input("Ingrese la altura del cilindro (en metros): "))
numeroHabitantes = int(input("Ingrese el número de habitantes: "))
    
volumenCilindro = calcularVolumenCilindro(diametro, altura)
litrosPorHabitante = calcularLitrosPorHabitante(volumenCilindro * 1000, numeroHabitantes)  # Convertimos metros cúbicos a litros
    
print(f"El volumen del cilindro es: {volumenCilindro:.2f} metros cúbicos")
print(f"Cada habitante podrá disponer de: {litrosPorHabitante:.2f} litros de agua")
