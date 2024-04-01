import serial, time

arduino = serial.Serial('COM3', 9600)

while True:
    ingresoNum = input("Ingrese el valor que desea enviar al arduino (ingresar 's o S' para salir): ")

    if ingresoNum.lower() == 's':
        print("Saliendo del programa...")
        break

    arduino.write(str.encode(ingresoNum))

    print("Valor enviado correctamente ;)")

arduino.close()