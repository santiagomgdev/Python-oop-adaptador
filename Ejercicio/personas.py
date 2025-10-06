class Personas:
    asociados = []

    def agregar_asociado(self, asociado):
        self.asociados.append(asociado)

    def activar_asociados(self):
        for asociado in self.asociados:
            if not asociado.estado:
                asociado.activar_asociado()

personas = Personas()