"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Misiones:
    def __init__(self, direcc, traba, secre):
        self.direcctora = direcc
        self.trabajadores = traba
        self.secretaria = secre

    def __str__(self):
        return (f"La directora de misiones universitaria es  {self.direcctora} y trabaja con {self.trabajadores} y su secretaria {self.secretaria}")


# clase 02
class Camarografo:

    def __init__(self, cam, mem, luz):
        self.camara = cam
        self.memoria = mem
        self.luces = luz

    def __str__(self):
        return (f"El camararografo usa una camara  {self.camara} con una memoria  {self.memoria } y luces {self.luces}")