import cmath

def calcular_raices_cuadraticas(a, b, c):
    # Calcula el discriminante
    discriminante = cmath.sqrt(b**2 - 4*a*c)

    # Calcula las dos soluciones
    raiz1 = (-b + discriminante) / (2*a)
    raiz2 = (-b - discriminante) / (2*a)

    return raiz1, raiz2

# Ingresa los coeficientes de la ecuación cuadrática
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
raiz1, raiz2 = calcular_raices_cuadraticas(a, b, c)
print(f"Las raíces son: {raiz1} y {raiz2}")