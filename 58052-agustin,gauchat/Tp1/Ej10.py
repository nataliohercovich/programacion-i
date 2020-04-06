class Fecha():
    
    def __init__(self):
        self. mes = {1 : "Enero", 2 : "Febrero", 3 : "Marzo", 4 : "Abril", 
        5 : "Mayo", 6 : "Junio", 7 : "Julio", 8 : "Agosto", 9 : "Septiembre",
        10 : "Octubre", 11 : "Noviembre", 12 : "Diciembre"}

    def volver_mes(self, m):
        return self.mes[m]

def main():
    fecha = Fecha()
    print("Fecha dd/mm/aaaa\n")

    d = input("Ingrese numero dia >>")
    m = fecha.volver_mes(int(input("Ingrese numero mes >>")))
    a = input("Ingrese numero año >>")

    print(d + " de " + m + " de " + a)
main()