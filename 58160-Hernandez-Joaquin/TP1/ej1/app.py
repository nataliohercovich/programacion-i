from Alumno import Alumno
from Curso import Curso

class App():

    def main(self):
        curso1=Curso()
        alumno1= Alumno()
        alumno1.setNombre()
        alumno1.setSexo()
        curso1.obtener_valores(alumno1.getNombre(),alumno1.getSexo())

if __name__ == '__main__':
    app=App()
    app.main()