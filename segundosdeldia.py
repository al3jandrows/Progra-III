def calcular_segundos(horas,minutos,segundos):
    return horas*3600+minutos*60+segundos
try:
    horas=int(input("Ingrese las horas que han transcurrido: "))
    minutos=int(input("Ingrese los minutos que han transcurrido: "))
    segundos=int(input("Ingrese los segundos que han transcurrido: "))
    total= calcular_segundos(horas,minutos,segundos)
    print(f"Han pasado un total de {total} segundos")
except ValueError:
    print("error")