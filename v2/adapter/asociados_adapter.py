from impl.asociados_atlantis import AsociadosAtlantis

class AsociadoAdapter:
    def __init__(self, asociado: AsociadosAtlantis):
        self._asociado = asociado
        self.nombre = asociado.AsoNom
        self.edad = asociado.AsoEdad

    def __repr__(self):
        estado = "Activo" if self._asociado.AsoEstado else "Inactivo"
        return f"Asociado: {self.nombre}, {self.edad} años - {estado}"

    def activar(self):
        self._asociado.activar_asociado()

    def es_activo(self):
        return self._asociado.AsoEstado is True