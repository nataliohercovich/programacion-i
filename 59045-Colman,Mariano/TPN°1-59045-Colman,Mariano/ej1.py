class Alumnos():
    def __init__(self,nombre,sexo):
        self.nombre = nombre
        self.sexo = sexo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

class SelectGroup ():
    def grupo (self,alumno):
        l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","w","x","y","z"]
    
        if(alumno.sexo.lower() == "f" and l.index(alumno.nombre[0].lower())<12):
            return "Pertenece al grupo A"
        elif(alumno.sexo.lower() == "m" and l.index(alumno.nombre[0].lower())>13):
            return "Pertenece al grupo A"
        else:
            return "Pertenece al grupo B"


main = SelectGroup()

nombre=input("Ingrese un nombre:")
sexo=input("Ingrese su sexo:")

alum_1 = Alumnos(nombre,sexo)

print(main.grupo(alum_1))
