class Informacion:

    def __init__(self):
        self.diccionario = {}

    def getNombre(self):
        return self.diccionario["nombre"]

    def setNombre(self, nombre):
        self.diccionario["nombre"] = nombre

    def getEdad(self):
        return self.diccionario["edad"]

    def setEdad(self, edad):
        self.diccionario["edad"] = edad

    def getDireccion(self):
        return self.diccionario["direccion"]

    def setDireccion(self, direccion):
        self.diccionario["direccion"] = direccion

    def getTelefono(self):
        return self.diccionario["telefono"]

    def setTelefono(self, telefono):
        self.diccionario["telefono"] = telefono


def main():
    per = Informacion()
    per.setNombre(input("Ingresar Nombre: "))
    per.setEdad(input("Ingresar Edad: "))
    per.setDireccion(input("Ingresar Direccion: "))
    per.setTelefono(input("Ingresar Telefono: "))
    print(per.getNombre() + " tiene " + per.getEdad() + " años, vive en " +
          per.getDireccion() + " y su numero de telefono es: " +
          per.getTelefono())


if __name__ == "__main__":
    main()
