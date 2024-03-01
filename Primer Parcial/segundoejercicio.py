"""Define una función llamada "inverso_palabra" que reciba una cadena
como parámetro y devuelva la
cadena invertida. Por ejemplo, si la entrada es "python", la salida
debería ser "nohtyp"""""""""

def inverso_palabra(palabra):##Definimos la funcion
    palabra_invertida = palabra[::-1] ##Elegimos el último carácter
    return palabra_invertida## Devolvemos

palabra = input("Ingresa una palabra: ")
palabra_invertida = inverso_palabra(palabra)
print("La palabra invertida es:", palabra_invertida)