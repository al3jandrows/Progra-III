def dolaraq(dolar):
    return(dolar*7.82) ##Valor del dólar el día 24 de enero de 2024 a las 5 PM
try:
    dolar= float(input("Ingrese el valor de dólar que desea pasar a quetzal: "))
    quetzal=dolaraq(dolar)
    print(f"{dolar} dólares son {quetzal} quetzales")
except ValueError:
    print("error")
   