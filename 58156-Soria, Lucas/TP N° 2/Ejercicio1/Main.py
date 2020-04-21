#!/usr/bin/python
import Billete
import Cajero_automatico


def main():
    caj = Cajero_automatico.Cajero_automatico()
    cien_pesos = Billete.Billete_de_100("pesos", "$")
    dos_pesos = Billete.Billete_de_200("pesos", "$")
    quin_pesos = Billete.Billete_de_500("pesos", "$")
    mil_pesos = Billete.Billete_de_1000("pesos", "$")
    caj.agregar_dinero([mil_pesos, mil_pesos, mil_pesos, quin_pesos, mil_pesos,
                        quin_pesos, dos_pesos, cien_pesos, quin_pesos])
    caj.contar_dinero()
    caj.extraer_dinero(3500)
    caj.extraer_dinero(1800)
    caj.extraer_dinero(4800)
    caj.extraer_dinero(468)
    caj.extraer_dinero(200)
    caj.contar_dinero()


if __name__ == "__main__":
    main()
