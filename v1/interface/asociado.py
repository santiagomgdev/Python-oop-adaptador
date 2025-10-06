class Asociado:
    
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.activo = False
    
    def __repr__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"Asociado: {self.nombre}, {self.edad} años - {estado}"
    
    def activar(self):
        self.activo = True
