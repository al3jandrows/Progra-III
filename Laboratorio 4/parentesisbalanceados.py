'''
Escribir una función en Python que tome una cadena de paréntesis y determine si están balanceados.
Utilizar una pila para rastrear la apertura y cierre de paréntesis.
'''
#funcion de parentesis balanceados
def parentesisBalanceados(cadena):

    Pila = [] 

    for caracter in cadena:
        if caracter == '(':
            Pila.append(caracter)
        elif caracter == ')':
            if not Pila or Pila.pop() != '(': 
                return False
    return not Pila #La cadena está balanceada si la pila está vacía al final


cadena1 = "()" 
cadena2 = ")([]{}" 
cadena3 = ")(" 
cadena4 = ")[()]" 
cadena5 = "{[]}" 

print(parentesisBalanceados(cadena1))
print(parentesisBalanceados(cadena2))
print(parentesisBalanceados(cadena3))
print(parentesisBalanceados(cadena4))
print(parentesisBalanceados(cadena5))