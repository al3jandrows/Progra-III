def determinar_tipo_variable(valor):

    tipo = type(valor).__name__
    return tipo

entrada_usuario = input("Ingrese una variable: ")


try:
    entrada_usuario = eval(entrada_usuario)
except:
    pass


tipo_variable = determinar_tipo_variable(entrada_usuario)
print(f"El tipo de la variable es: {tipo_variable}")
