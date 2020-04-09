class Persona():
    def __init__(self):
        self.diccionario = {'nombre' : None,'edad':None,'direccion':None,'telefono':None}

    def cargarDatos (self,nom,edad,dir,tel):
        self.diccionario['nombre'] = nom
        self.diccionario['edad'] = edad
        self.diccionario['direccion'] = dir
        self.diccionario['telefono'] = tel


def main():
    persona = Persona()
    nom = str(input("Ingrese un nombre: "))
    edad = (input("Ingrese la edad: "))
    dir = str(input("Ingrese una direccion: "))
    tel = (input("Ingrese un telefono: "))
    persona.cargarDatos(nom,edad,dir,tel)
    print(persona.diccionario['nombre']+" tiene "+persona.diccionario['edad']+" años, vive en "+persona.diccionario['direccion']+" y su telefono es "+persona.diccionario['telefono'])

main()