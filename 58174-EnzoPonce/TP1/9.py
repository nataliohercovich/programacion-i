class persona():

    def __init__(self):
        self.nombre = ""
        self.edad = ""
        self.direccion = ""
        self.telefono = ""
        

    def ingresar(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = input("Ingrese su edad: ")
        self.direccion = input("Ingrese su direccion: ")
        self.telefono = input("Ingrese su numero de telefono: ")
        
    def diccionario(self):
        diccionario = {self.nombre, self.edad, self.direccion, self.telefono}
        print("La pesona llamada",self.nombre,"tiene",self.edad,"años, vive en",self.direccion,"y su numero de telefono es",self.telefono)

gente = persona()
gente.ingresar()
gente.diccionario()