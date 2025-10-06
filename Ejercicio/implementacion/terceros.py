import random

class Tercero:
    contador_terceros = 0

    def __init__(self, nombre_completo, edad, identificacion):
        Tercero.contador_terceros += 1
        self.codigo_t = self.contador_terceros
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.identificacion = identificacion
        self.digito_v = None
        self.activo = False

    def activar_tercero(self):
        self.activo = True

    def anadir_digito(self):
        digito = random.randint(0, 9)
        self.digito_v = digito