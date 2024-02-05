def definir_num(num):
    if num<0:
        return "Su numero es negativo"
    elif num >0:
        return "Su numero es positivo"
    else:
        return "Su numero es cero"

try:
    num=float(input("Ingrese un número: "))
    signo=definir_num(num)
    print ("EL Número ingresado es: ", signo)
except ValueError:
    print("Ingrese un numero valido")




