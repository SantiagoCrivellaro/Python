print("Antes de la condicion")

my_condicional = True

if my_condicional:
    print("Se ejecuta")


mi_otra_condicion = 10


if mi_otra_condicion == 11:
    print("Se ejecuta el 2do IF.")
# No se ejecuta.


if mi_otra_condicion > 5 and mi_otra_condicion < 11:
    print("Se ejecuta el 3er IF.")


edad =  int(input("ingresa tu edad:"))

if edad > 18:
    print("Podes pasar")
elif edad > 16:
    print("Te dejo pasar")
else:
    print("No podes pasar")