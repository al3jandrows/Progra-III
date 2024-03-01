"""Escribe un programa que pida al usuario una lista de números y luego
imprima la suma de los números
pares en la lista"""
def suma_numeros_pares(lista): ##Definir la función para sumarla
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma


numeros = input("Ingresa una lista de números separados por espacios: ") # Solicitar la lista
lista_numeros = [int(num) for num in numeros.split()]


suma_pares = suma_numeros_pares(lista_numeros) # Calcular la suma de los números pares en la lista

# Imprimir la suma de los números pares
print("La suma de los números pares en la lista es:", suma_pares)