from interface.asociado import Asociado
from impl.asociados_atlantis import AsociadosAtlantis
from impl.asociados_nexus import AsociadosNexus


class AtlantisAdapter(Asociado):
    
    def __init__(self, asociado_atlantis: AsociadosAtlantis):
        super().__init__(
            nombre=asociado_atlantis.AsoNom,
            edad=asociado_atlantis.AsoEdad
        )
        self._asociado_original = asociado_atlantis
        self.activo = asociado_atlantis.AsoEstado == True
    
    def activar(self):
        self._asociado_original.activar_asociado()
        self.activo = True


class NexusAdapter(Asociado):
    
    def __init__(self, asociado_nexus: AsociadosNexus):
        super().__init__(
            nombre=asociado_nexus.nombre,
            edad=asociado_nexus.edad
        )
        self._asociado_original = asociado_nexus
        self.activo = asociado_nexus.estado == "Activo"
    
    def activar(self):
        self._asociado_original.activar_asociado()
        self.activo = True
