from usuario import Usuario

class App():

    def main(self):
        usuario=Usuario()
        diccionario={}

        usuario.setNombre()
        usuario.setEdad()
        usuario.setDireccion()
        usuario.setTelefono()
        diccionario["Nombre"]=usuario.getNombre()
        diccionario["Edad"]=usuario.getEdad()
        diccionario["Direccion"]=usuario.getDireccion()
        diccionario["Telefono"]=usuario.getTelefono()
        self.imprimir(diccionario)

    def imprimir(self,diccionario):

        print("Su nombre es {}, su edad es {}, vive en {} y su numero de telefono es {}\n"
        .format(diccionario["Nombre"],diccionario["Edad"],diccionario["Direccion"],diccionario["Telefono"]))
        print()
    
if __name__ == "__main__":
    app=App()
    app.main()