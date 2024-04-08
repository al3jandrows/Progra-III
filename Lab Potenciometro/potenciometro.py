import serial
import tkinter as tk

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM3', 9600)

# Función para actualizar la gráfica de barras
def update_bar_graph():
    try:
        # Leer dato del puerto serial
        data = ser.readline().decode().strip()
        print("Datos recibidos:", data)  # Debugging: Imprime los datos recibidos
        
        value = int(data)
        
        # Normalizar el valor para que esté en el rango de 0 a 100 (Tkinter no acepta valores fuera de este rango)
        normalized_value = int((value / 1023) * 100)
        
        # Actualizar la altura de la barra
        canvas.coords(bar, 5, 105 - normalized_value, 35, 105)

        # Actualizar la ventana
        root.update()
    except serial.SerialException:
        pass
    
    # Programar la próxima actualización después de 100 ms
    root.after(100, update_bar_graph)

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Arduino Data Plotter")
root.geometry("400x200")

# Configuración de la gráfica de barras
canvas = tk.Canvas(root, width=40, height=105, bg='white')
canvas.pack()
bar = canvas.create_rectangle(5, 105, 35, 105, fill='blue')

# Llamar a la función de actualización inicial
update_bar_graph()

# Ejecutar la aplicación Tkinter
root.mainloop()
