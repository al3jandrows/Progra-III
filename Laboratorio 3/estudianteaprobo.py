class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota
    def aprobacion(self):
        return self.nota>=60    

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
nota=int(input("Ingrese su nota: "))
estudiante=Estudiante(nombre, edad, nota)
if estudiante.aprobacion():
    print(f"{estudiante.nombre} ha aprobado")
else:
    print (f"{estudiante.nombre} ha reprobado")