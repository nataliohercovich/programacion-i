
class Texto:

    def __init__(self):
        self.texto = '''
    La Programación Orientada a Objetos (POO u OOP según sus siglas en inglés) es un paradigma 
    de programación que usa objetos y sus interacciones para diseñar aplicaciones y programas 
    de computadora. Está basado en varias técnicas, incluyendo herencia, modularidad, 
    polimorfismo, y encapsulamiento. Su uso se popularizó a principios de la década de 1990. 
    Actualmente son muchos los lenguajes de programación que soportan la orientación a objetos.
    La programación Orientada a objetos (POO) es una forma especial de programar, más cercana a 
    como se expresan las cosas en la vida real que otros tipos de programación.
    La POO es un paradigma de la programación de computadores; esto hace referencia al 
    conjunto de teorías, estándares, modelos y métodos que permiten organizar el conocimiento, 
    proporcionando un medio bien definido para visualizar el dominio del problema e implementar 
    en un lenguaje de programación la solución a ese problema.
    La POO se basa en el modelo objeto, donde el elemento principal es le objeto, el cual es 
    una unidad que contiene todas sus características y comportamientos en sí misma, lo cual 
    lo hace como un todo independiente, pero que se interrelaciona con objetos de su misma clase 
    o de otras clase, como sucede en el mundo real.
    En python la POO se expresa de manera simple y fácil de escribir pero debes tener en cuenta 
    que para programar debes entender cómo funciona la teoría de la POO y llevarla a código.
    La teoría de la POO nos dice que todos los objetos deben pertenecer a una clase, ya que esta 
    es la base para diferenciarse unos de otros teniendo atributos y comportamientos que los distingan 
    de otros objetos que pertenezcan a otras clases, para crear clases en python lo hacemos de la 
    siguiente manera: class Coche(): Como puedes ver para crear una clase lo hacemos escribiendo 
    la palabra class seguida del nombre de la clase y un par de paréntesis, debes tener en cuenta que 
    el nombre de la clase que hayas creado debe empezar por mayúsculas y si tiene más de una palabra 
    debes usar la notación de camello.'''
        self.ps = {}
        self.p = {}

    def contar(self):
        for i in self.texto.lower().replace("," or "." or "\n").split(" "):
            if i not in self.ps.keys():
                self.ps[i] = 1
            else:
                self.ps[i] += 1
        j= 0
        for i in sorted(self.ps.items(), key=lambda x: x[1], reverse=True):
            if j == 20:
                break
            self.p[i[0]] = i[1]
            j += 1
        return self.p


def main():
    info = Texto()
    p = info.contar()
    for i in sorted(p.items()):
        print("'{}' se repitio {} veces".format(i[0], i[1]))


if __name__ == "__main__":
    main()
