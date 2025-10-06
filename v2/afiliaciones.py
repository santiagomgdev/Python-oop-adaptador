class Afiliaciones:
    def __init__(self):
        self.asociados = []

    def agregar_asociado(self, asociado):
        self.asociados.append(asociado)

    def activar_asociados(self):
        for asociado in self.asociados:
            if not asociado.es_activo():
                asociado.activar()