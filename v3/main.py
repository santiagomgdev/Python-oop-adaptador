from domain.asociado import Asociado
from impl.asociados_atlantis import AsociadosAtlantis
from adapter.asociados_adapter import AsociadoAdapter
from afiliaciones import Afiliaciones

def main():
    afiliaciones = Afiliaciones()

    asociado1 = AsociadoAdapter("Juan Perez", 30)
    asociado2 = AsociadoAdapter("Maria Gomez", 25)

    afiliaciones.agregar_asociado(asociado1)
    afiliaciones.agregar_asociado(asociado2)

    print("Antes de activar:")
    for asociado in afiliaciones.asociados:
        print(asociado)

    afiliaciones.activar_asociados()

    print("\nDespués de activar:")
    for asociado in afiliaciones.asociados:
        print(asociado)

if __name__ == "__main__":
    main()