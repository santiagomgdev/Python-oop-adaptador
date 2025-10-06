class AsociadosNexus:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = None

    def __repr__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def activar_asociado(self):
        self.estado = "Activo"