# PROGRAMA PARA CALCULAR EL AREA DE UN CUADRADO-RECTANGULO

#variable estilo snake_case solicitando un dato de tipo texto (string)
tipo_de_figura = str(input("Su figura geometrica será un cuadrado o un rectangulo: "))

#variable estilo snake_case solicitando un dato de tipo entero (integer)
longitud_base = int(input("Ingrese la longitud de la base de su figura: "))

#variable estilo snake_case solicitando un dato de tipo flotante (float)
longitud_altura = float(input("Ingrese la longitud de la altura de su figura: "))

#estilo snake_case en funciones
def calcular_area():
    area = longitud_base * longitud_altura
    print(f"El area del {tipo_de_figura} es: {area}")

calcular_area()

#variable estilo snake_case para obtener un dato de tipo boleano (boolean)
confirmar_figura = longitud_base == longitud_altura
print(f"Su figura es un cuadrado: {confirmar_figura}")

#variable estilo snake_case para obtener un dato de tipo boleano (boolean)
confirmar_figura = longitud_base != longitud_altura
print(f"Su figura es un rectangulo: {confirmar_figura}")
    

