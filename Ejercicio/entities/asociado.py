class Asociado:
    contador_asociados = 0

    def __init__(self, nombre, edad, identificacion, telefono, direccion):
        Asociado.contador_asociados += 1
        self.asocod = self.contador_asociados
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.telefono = telefono
        self.direccion = direccion
        self.estado = None

    def activar_asociado(self):
        self.estado = "Afiliado"