class Texto():

    def __init__(self):
        self.texto="""
        Un ejemplo de esta competitividad por tener lo mejor del mercado son los teléfonos móviles,
        algo que no solo es en sí el propio teléfono, sino también todos los accesorios que mejoran,
        ya sea en rendimiento o en la estética, nuestro móvil. En este caso además de requerir una 
        actualización de conocimiento para comprender todas y cada una de las funciones que nuestro 
        nuevo teléfono contiene, es necesario tener un bolsillo bastante amplio para hacer frente a 
        los gastos que tener una tecnología de estas características. Pese a que el desarrollo y 
        expansión de esta tecnología continúa siendo desigual en diferentes países del mundo, 
        lo cierto es que ya existen más aparatos que personas en nuestro planeta. 
        Y lo que hace solo 5 años era un teléfono móvl inteligente (smartphone), 
        hoy día es un auténtico ordenador personal en el que la función de llamada se ha quedado en
        un ámbito absolutamente secundario.
        Algunos usuarios de Android y otros sistemas operativos 
        como Windows Phone, Blackberry o Iphone, montaron en cólera en 2014 al recibir una notificacion 
        por parte de la compañía propietaria de la aplicacion Whatsapp (actualmente propiedad de Facebook) 
        con un mensaje de alerta advirtiendo que su licencia gratuita expiraría y que para seguir utilizándolo 
        sería necesario realizar un desembolso económico, no muy alto, 0,99 céntimos, pero aquello genero 
        un auténtico terremoto que, afortunadamente, con el paso del tiempo ha quedado en una mera anécdota.
        Sin embargo, si fue la punta del iceberg de esa tecnología que llegaba para quedarse, en la que en muchos casos, 
        el producto era el usuario, sus datos concretamente. Coincidiendo con esa mentalización por parte de los usuarios, 
        en los últimos años las empresas tecnológicas más punteras han conseguido, en casos muy concretos, revertir la política 
        del 'gratis total en internet'. Spotify, AppleMusic, Amazon Prime, abrieron el camino para que los usuarios comenzaran 
        a darle valor a los 'micropagos' por servicios que podían conseguir gratis a través de descargas ilegales pero con mucho más esfuerzo. """


    def setTexto(self):
        self.texto = self.texto.replace("\n", " ")
        self.texto = self.texto.replace(",", "")
        self.texto = self.texto.replace(".", "")
        self.texto = self.texto.replace("(", "")
        self.texto = self.texto.replace(")", "")
        self.texto = self.texto.replace("'", "")
        self.texto = self.texto.lower()
        self.texto = self.texto.split(" ")
        [self.texto.remove("") for i in range(self.texto.count(""))]

    def getTexto(self):
        return self.texto

