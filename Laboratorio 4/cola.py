'''Definir funciones para las operaciones básicas de una cola: enqueue (añadir elemento), dequeue (eliminar
elemento) y front (ver el primer elemento sin eliminarlo).
Escribir un programa que simule el proceso de atención en una fila, donde los elementos son atendidos en
el orden en que llegan'''

from collections import deque 
class Cola:
 
    def __init__(self):
        self.listaVacia = []
    
  
    def enqueue(self, elemento):
        self.listaVacia.append(elemento)
    
   
    def dequeue(self):
        if not self.colaVacia():
            return self.listaVacia.pop(0) 
        else:
            return None 

  
    def front(self):
        if not self.colaVacia():
            return self.listaVacia[0] 
        else:
            return None 
    
    def colaVacia(self):
        return len(self.listaVacia) == 0 

def atencionFila(elementos):
    fila = Cola() 

    for elemento in elementos:
        fila.enqueue(elemento)

    print("Proceso de atencion en la fila: ")
    while not fila.colaVacia():
        #atender al proximo cliente
        siguienteElemento = fila.dequeue()
        print(f"Atendiendo: {siguienteElemento}")

    if fila.colaVacia():
        print("Todos las personas han sido atendidas")

#Clientes dentro de la lista
elementos = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]
atencionFila(elementos)