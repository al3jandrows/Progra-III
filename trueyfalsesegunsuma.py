def par(num1,num2):
    suma=num1+num2
    if suma%2==0:
        return True
    else:
        return False
try:
    num1 = int(input("Introduzca el numero uno: "))
    num2 = int(input("Introduzca el numero dos: "))
    respuesta= par(num1,num2)
    print(respuesta)
except ValueError:
    print("Ingrese un numero válido")