## Bucles 

# Sirve para iterar, pasar por el mismo codigo varias veces.

condicion = 0
"""
while condicion < 10:
    print(condicion)
    condicion +=1
#0,1,2,3,4,5,6,7,8,9"""
"""
while condicion < 5:
    print(condicion)
    condicion +=1
    if condicion == 5:
        break
print("El programa se detuvo.")
"""




# Ejercicio : hacer un contador del 1 al 20, pero que se detenga en el 17.
"""
contador = 0 

while contador < 20:
    print(contador)
    contador +=1
    if contador == 17:
        break
"""

# For

# Nos Sirve para iterar un listador de elementos.

lista = [1,2,3,4,5,6,7,8,9,10]
"""
for element in lista: 
    print(element)"""
    
# Por cada elemento en lista, imprimir el elemento, para representar el elemento se suele usar la I.


# Ejercicio = iterar una lista con un bucle for y cuando llegue al 7 parar.
"""
for element in lista:
    print(element)
    if element == 7:
        break"""


# Ejercicio : Imprimir todoos los datos de la lista, pero obviando el 3

for element in lista:
    if element == 3:
        continue
    print(element)
   