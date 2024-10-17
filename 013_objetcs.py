# Objetos

class coche:
    def __init__(self,marca,matricula):
        self.marca = marca
        self.matricula = matricula
        

renault = coche("Renault", 1256)

print(type(renault))

print(renault.matricula)