## Clases

class coche:
    def __init__(self, marca, matricula):
        self.marca = marca
        self.matricula = matricula 
        self.arrancado = False
        
Ford = coche("Ford","Fiesta")

print (type(Ford))

print(Ford.marca)



# Ejercicio : Uno igual pero con personas


class persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
Santiago = persona("Santiago", 15)

print(type(Santiago))
print(Santiago.edad)


# Ejercicio 2 : hacer un animal

class animal:
    def __init__(self,raza,edad):
        self.raza = raza
        self.edad = edad
        

Bauti = animal("Galgo", 3)

print(type(Bauti))
print(Bauti.raza, Bauti.edad)