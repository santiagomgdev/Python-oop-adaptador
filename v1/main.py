from adapter.asociados_adapter import AtlantisAdapter, NexusAdapter
from impl.asociados_atlantis import AsociadosAtlantis
from impl.asociados_nexus import AsociadosNexus
from afiliaciones import Afiliaciones

def main():
    asociado_atlantis = AsociadosAtlantis("Juan", 30)
    asociado_nexus = AsociadosNexus("Maria", 25)

    asociado1 = AtlantisAdapter(asociado_atlantis)
    asociado2 = NexusAdapter(asociado_nexus)

    afiliaciones = Afiliaciones()
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