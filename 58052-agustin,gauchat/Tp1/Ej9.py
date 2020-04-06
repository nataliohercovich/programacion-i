class Datos():
    def __init__(self):
        self.dato = {'nombre' : None, 'edad' : None, 'direccion' : None, 'telefono' : None}

    def agregar_datos(self, n, e, d, t):
        self.dato['nombre'] = n
        self.dato['edad'] = d
        self.dato['direccion'] = e
        self.dato['telefono'] = t

def main():
    datos = Datos()
    n = input("Ingrese su nombre: ")
    d = input("Ingrese su edad: ")
    e = input("Ingrese su direccion: ")
    t = input("Ingrese su telefono: ")

    datos.agregar_datos(n, e, d, t)

    print(datos.dato['nombre'] + " tiene " + datos.dato['edad'] + " años, vive en " + datos.dato['direccion'] + " y su numero de telefono es " + datos.dato['telefono'])
main()