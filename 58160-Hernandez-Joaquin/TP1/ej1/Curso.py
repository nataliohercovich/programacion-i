from Alumno import Alumno


class Curso():

    def obtener_valores(self,nombre,sexo):
        if sexo=='F' and ord(nombre[0])<=77 and ord(nombre[0])>64:
            print("La alumna {} pertenece al grupo A\n" .format(nombre))
        elif sexo=='F' and ord(nombre[0])<=90 and ord(nombre[0])>77:
            print("La alumna {} pertenece al grupo B\n" .format(nombre))
        elif sexo=='M' and ord(nombre[0])<=77 and ord(nombre[0])>64:
            print("El alumno {} pertenece al grupo B\n" .format(nombre))
        elif sexo=='M' and ord(nombre[0])<=90 and ord(nombre[0])>77:
            print("El alumno {} pertenece al grupo A\n" .format(nombre))
        else:
            print("\n**ERROR--El nombre introducido es invalido**") #excepcion nombre
        print()


