import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM3', 9600)

# Función para leer datos del puerto serie en un hilo separado
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

# Función para encender un círculo
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

# Función para apagar un círculo
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="white")

def paint_white():
    canvas.create_rectangle(200, 215, 225, 230, fill='white')
def paint_white2():
    canvas.create_rectangle(200, 235, 225, 250, fill='white')
    
def paint_white3():
    canvas.create_rectangle(200, 255, 225, 270, fill='white')


# Función para manejar los datos recibidos del puerto serie
def handle_code(code):
    try:
        digit = int(code)
        print("Código recibido:", digit)
        # Apagar todos los círculos primero
        for circle in circles:
            turn_off_circle(circle)

        # Encender el círculo correspondiente al código recibido
        if digit == 1:
            turn_on_circle(circles[0], "yellow")    
        elif digit == 2:
            turn_on_circle(circles[1], "green")     
        elif digit == 3:
            turn_on_circle(circles[2], "red")    

        if digit==5:    
            canvas.create_rectangle(200, 215, 225, 230, fill='green')    
        elif digit==6:
             canvas.create_rectangle(200, 255, 225, 270, fill='green')    
        elif digit==7:
            canvas.create_rectangle(200, 235, 225, 250, fill='green')      
        elif digit==8:
            canvas.create_rectangle(200, 215, 225, 230, fill='white')
            canvas.create_rectangle(200, 235, 225, 250, fill='white')
            canvas.create_rectangle(200, 255, 225, 270, fill='white')
        # Actualizar el valor de la barra de potenciómetro
        update_bar_graph(digit)
    except ValueError:
        print("Mensaje desde Arduino:", code)
        

# Función para actualizar la barra de potenciómetro
def update_bar_graph(value):
    # Normalizar el valor para que esté en el rango de 0 a 1 (Tkinter no acepta valores fuera de este rango)
    normalized_value = value / 1023
    # Calcular las coordenadas de la barra
    x0 = 50
    y0 = 450 - normalized_value * 300  # Reducir la altura de la barra
    x1 = 100
    y1 = 450
    # Actualizar las coordenadas y el color de la barra
    canvas.coords(bar, x0, y0, x1, y1)

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Segundo Parcial Progra")
root.geometry("1000x500")  # Ajustar el tamaño de la ventana

# Configuración de la gráfica de barras
canvas = tk.Canvas(root, width=300, height=350, bg='white')  # Ajustar el tamaño del lienzo
canvas.pack()
bar = canvas.create_rectangle(50, 450, 100, 450, fill='orange')  # Rectángulo que representa la barra de potenciómetro
canvas.create_text(75, 130, text="Potenciómetro", font=("Arial", 10), anchor=tk.CENTER)  # Nombre del potenciómetro

circles = []
for i in range(3):
    circle = canvas.create_oval(25 + i * 100, 50, 75 + i * 100, 100, outline="black", width=2)  # Ajustar la posición de los círculos
    canvas.create_text(50 + i * 100, 75, text=str(i+1), font=("Arial", 12))  # Ajustar la posición del texto
    circles.append(circle)
    
# Cuadro pequeño a la derecha de la barra
small_rectangle = canvas.create_rectangle(200, 215, 225, 230, fill='white')
small_rectangle2 = canvas.create_rectangle(200, 235, 225, 250, fill='white')
small_rectangle3 = canvas.create_rectangle(200, 255, 225, 270, fill='white')

canvas.create_text(265, 223, text="InOrden", font=("Arial", 10), anchor=tk.CENTER)
canvas.create_text(265, 243, text="PostOrden", font=("Arial", 10), anchor=tk.CENTER)
canvas.create_text(265, 263, text="PreOrden", font=("Arial", 10), anchor=tk.CENTER)

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Ejecutar la aplicación Tkinter
root.mainloop()
