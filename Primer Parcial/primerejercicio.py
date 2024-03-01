"""Escribe una función en Python que reciba una lista como parámetro y
devuelva la suma de todos los
elementos de la lista."""
def suma_lista(lista):##Definimos La Función
    suma = sum(lista)##Establecemos parámetro
    return suma
mi_lista = [1, 2, 3, 4, 5]##Recibimos la lista
resultado = suma_lista(mi_lista)##Sumamos la lista
print("La suma de los números  es: ", resultado)