class Calendario():

    def __init__(self):
        self.calendario = {1 : 'Enero',2 : 'Febrero', 3 : 'Marzo', 4 : 'Abril', 
        5 : 'Mayo', 6 : 'Junio', 7 :'Julio', 8: 'Agosto', 9 : 'Septiembre', 10 : 'Octubre',
        11 : 'Noviembre', 12 : 'Diciembre'}
        
    def conversor (self, mes):
        return self.calendario[mes]


def main ():
    print("Ingrese la fecha en formato dd/mm/aaaa")
    calendario = Calendario()
    dia = input("Ingrese el dia: ")
    mes = calendario.conversor(int(input("Ingrese el mes: ")))
    año = input("Ingrese el año: ")

    print(dia+" de "+mes+" de "+año)

main()