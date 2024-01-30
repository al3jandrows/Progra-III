def celsiusafh(celsius):
    return(celsius*9/5+32)
try:
    celsius=float(input("Ingrese su temperatura en grados Celsius para calcular su equivalente en Farenheit: "))
    fahrenheit=celsiusafh(celsius)
    print(f"{celsius} grados Celcius son {fahrenheit} grados Fahrenheit ")
except ValueError:
    print("error")