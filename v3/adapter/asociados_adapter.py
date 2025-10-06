from impl.asociados_atlantis import AsociadosAtlantis
from domain.asociado import Asociado

class AsociadoAdapter(Asociado, AsociadosAtlantis):
    
    def __init__(self, nombre: str, edad: int):
        Asociado.__init__(self, nombre, edad)
        AsociadosAtlantis.__init__(self, nombre, edad)
    
    def activar(self):
        super().activar()
        self.activar_asociado()

    def __repr__(self):
        return super().__repr__()