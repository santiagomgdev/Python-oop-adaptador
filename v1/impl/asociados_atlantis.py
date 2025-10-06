class AsociadosAtlantis:
    def __init__(self, nombre, edad):
        self.AsoNom = nombre
        self.AsoEdad = edad
        self.AsoEstado = False

    def __repr__(self):
        return f"Nombre: {self.AsoNom}, Edad: {self.AsoEdad}"
    
    def activar_asociado(self):
        self.AsoEstado = True
    