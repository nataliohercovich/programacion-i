class Curso():
    def __init__(self):
        self.mat = {}
        self.cred = 0

    def agregar_mat(self, nombre, creditos):
        self.mat.update({nombre: creditos})
        self.cred += creditos

    def obtener_mat(self, mat):
        return self.cred[mat]

def main():
    curso = Curso()
    salida = ""
    while salida != "1":
        if input("Si desea salir ingrese 1, si no presione enter>>") == "1":
            salida = "1"
        else:
            m = input("Ingrese nombre de la materia >>")
            try:
                c = int(input("Ingrese credito de la materia>>"))
            except:
                print("Numero invalido")
                break

            curso.agregar_mat(m, c)

    print("Materia : creditos")
    for key in curso.mat:
        print(key, ":", curso.mat[key])

    print("Hay " + str(curso.cred) + " creditos totales")
main()


# print("Matematica tiene " + str(curso.obtener_mat("Mat")) + " creditos.")
#         print("Fisica tiene " + str(curso.obtener_mat("Fi")) + " creditos.")
#         print("Quimica tiene " + str(curso.obtener_mat("Qui")) + " creditos.")
# print("El curso tiene " + str(curso.obtener_mat("Qui") + curso.obtener_mat("Qui") + curso.obtener_mat("Qui")) + " creditos totales.")