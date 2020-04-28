class Usuario():

    def __init__(self):
        self.nombre=""
        self.edad=0
        self.direccion=""
        self.tel=""
    
    def setNombre(self):
        self.nombre=input("\nIngrese su nombre: ")
        self.nombre=self.nombre.upper()
    
    def getNombre(self):
        return self.nombre
    
    def setEdad(self):
        while True:
            try:
                self.edad=int(input("\nIngrese la edad: "))
                if self.edad<0 and self.edad>110:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nLa edad ingresada es invalida. Intente nuevamente")
    
    def getEdad(self):
        return self.edad
    
    def setDireccion(self):
        self.direccion=input("\nIngrese su direccion: ")
        self.direccion=self.direccion.upper()
    
    def getDireccion(self):
        return self.direccion
    
    def setTelefono(self):
         while True:
            try:
                self.tel=(input("\nIngrese su numero de telefono: "))
                if len(self.tel)!=10:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\n El numero de telefono es invalido. Intente nuevamente")

    def getTelefono(self):
        return self.tel


