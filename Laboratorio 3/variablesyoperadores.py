def calcular_num(num1, num2):
    suma = float(num1) + float(num2)
    resta = float(num1) - float(num2)
    multi = float(num1) * float(num2)
    if float(num2) != 0:
        divi = float(num1) / float(num2)
    else:
        divi = "No se puede dividir por cero"
    return suma, resta, multi, divi

try:
    num1 = input("Introduzca el numero uno: ")
    num2 = input("Introduzca el numero dos: ")
    
    totales = calcular_num(num1, num2)
    
    print("Las respuestas son:", totales)
    
except ValueError:
    print("Por favor, introduce números válidos.")
