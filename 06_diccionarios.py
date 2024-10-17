# Diccionarios

# Clave-Valor

# 2 Elementos x Posicion ( clave y valor )

diccionario = {}

print(type(diccionario))

dict = { "nombre" : "Santiago" }

# print(dict["nombre"])

# Agregar/ Modificar


dict["nombre"] = "Mateo"

print(dict["nombre"])

dict["Apellido"] = "Crivellaro"

print(dict["Apellido"])


del(diccionario["Apellido"])

print(dict["Apellido"])