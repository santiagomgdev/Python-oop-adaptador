from entities.asociado import Asociado
from implementacion.terceros import Tercero

class AdaptadorAsociado(Asociado):

    def __init__(self, tercero: Tercero, telefono, direccion):
        super().__init__(
            nombre=tercero.nombre_completo,
            edad=tercero.edad,
            identificacion=tercero.identificacion,
            telefono=telefono,
            direccion=direccion
        )
        self._tercero = tercero
        self.estado = "Afiliado" if tercero.activo else "Retirado"

    def activar_asociado(self):
        self._tercero.activar_tercero()
        self.estado = "Afiliado"

    def devolver_tercero(self):
        return self._tercero
    
    def __repr__(self):
        return f"AdaptadorAsociado(nombre={self.nombre}, edad={self.edad}, identificacion={self.identificacion}, estado={self.estado}, id={self.asocod})"