'''Implementar una pila utilizando una lista en Python.
Crear funciones para realizar las operaciones básicas de una pila: push (añadir elemento), pop (eliminar
elemento) y peek (ver el elemento superior sin eliminarlo).
Escribir un programa que utilice esta pila para invertir el orden de una lista dada.
Implementación de una Cola (Queue)'''
class Pila:
    def __init__(self):
        self.lista=[]
    def papelera(self):
        return len(self.lista)==0
    def push (self,elemento):
        self.lista.append(elemento)
    def pop (self):
        if not self.papelera():#si la papelera esta vacía, pop se encarga de eliminar y devolver el elemento en la parte superior de la pila
            return self.lista.pop()
        else:
            return None
    def peek(self):
        if not self.papelera(): #Devuelve el último elemento de la lista sin eliminarlo
            return self.lista[-1]
        else:
            return None

def Invertir(lista):
    nuevapila=Pila()
    for elemento in lista:
        nuevapila.push(elemento)
    listainvertida= []
    while not nuevapila.papelera():
        listainvertida.append(nuevapila.pop())
    return listainvertida

listaoriginal=[22,8,79,21,80]
print(listaoriginal)
listainvertida=Invertir(listaoriginal)
print(listainvertida)

       
        
    
        

          
    

