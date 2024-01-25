import cmath

def formulacuadratica(a, b, c):
    discriminante = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminante) / (2*a)
    x2 = (-b - discriminante) / (2*a)
    return x1, x2

try:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    soluciones = formulacuadratica(a, b, c)
    print(f"Las dos respuestas son {soluciones}")
except ValueError:
    print("Error: Ingrese valores numéricos para a, b y c.")
