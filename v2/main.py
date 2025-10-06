from adapter.asociados_adapter import AsociadoAdapter
from impl.asociados_atlantis import AsociadosAtlantis
from afiliaciones import Afiliaciones

def main():
    afiliaciones = Afiliaciones()

    asociado1 = AsociadosAtlantis("Juan Perez", 30)
    asociado2 = AsociadosAtlantis("Maria Gomez", 25)

    asociado_adaptado1 = AsociadoAdapter(asociado1)
    asociado_adaptado2 = AsociadoAdapter(asociado2)

    afiliaciones.agregar_asociado(asociado_adaptado1)
    afiliaciones.agregar_asociado(asociado_adaptado2)

    afiliaciones.activar_asociados()

    for asociado in afiliaciones.asociados:
        print(asociado)

if __name__ == "__main__":
    main()