from implementacion.terceros import Tercero
from adaptador.adaptador_asociado import AdaptadorAsociado
from personas import personas

def main():
    tercero_1 = Tercero("Santiago", 23, 1005)
    tercero_2 = Tercero("Jhon", 30, 1006)
    tercero_1.anadir_digito()
    tercero_2.anadir_digito()

    asociado_1 = AdaptadorAsociado(tercero_1, 123999, "Calle 69")
    asociado_2 = AdaptadorAsociado(tercero_2, 123888, "Calle 70")
    asociado_1.activar_asociado()
    asociado_2.activar_asociado()

    personas.agregar_asociado(asociado_1)
    personas.agregar_asociado(asociado_2)
    personas.activar_asociados()

    for asociado in personas.asociados:
        print(asociado)

if __name__ == "__main__":
    main()