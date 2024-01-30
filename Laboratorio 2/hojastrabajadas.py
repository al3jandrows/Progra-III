def calcular_pago(horas_trabajadas, costo_por_hora):
    pago = horas_trabajadas * costo_por_hora
    return pago

try:
    horas = float(input("Por favor, introduce el número de horas trabajadas: "))
    costo = float(input("Por favor, introduce el costo por hora de trabajo: "))
    
    pago_total = calcular_pago(horas, costo)
    
    print("El pago correspondiente es: ", pago_total)
    
except ValueError:
    print("Por favor, introduce números válidos.")
