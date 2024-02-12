'''
Desarrollar una clase ColaConPilas que utilice dos pilas para simular el comportamiento de una cola.
Implementar las operaciones enqueue y dequeue utilizando las operaciones de pilas.
'''
from collections import deque #libreria

class ColaConPilas:
    
    def __init__(self):
        self.pilaEntrada = [] #pila para encolar elementos
        self.pilaSalida = [] #pila para desencolar elementos

    def enqueue (self, elemento):
        self.pilaEntrada.append(elemento) 
    
    def dequeue(self):
        if not self.pilaSalida: 
            while self.pilaEntrada:
                self.pilaSalida.append(self.pilaEntrada.pop()) 
        if self.pilaSalida: # Si la pila de salida tiene elementos, desencolar el elemento superior
            return self.pilaSalida.pop()
        else: # Si ambas pilas están vacías, la cola está vacía
            return None

cola = ColaConPilas() #
cola.enqueue(8)
cola.enqueue(10)
cola.enqueue(79)
cola.enqueue(11)

print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 