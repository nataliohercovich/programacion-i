class Texto:

    def contar_palabras(t): '''
Un procesador de texto es una aplicación informática que permite crear y editar documentos de texto en una computadora. 
Se trata de un software de múltiples funcionalidades para la redacción, 
con diferentes tipografías, tamaños de letra, colores, tipos de párrafos, efectos artísticos y otras opciones.
Los procesadores de texto cumplen con una función similar a la que cumplían las máquinas de escribir hace algunas décadas, aunque mucho más completa y compleja.
En la máquina de escribir, por ejemplo, cada letra tipeada por el usuario era impresa de forma inmediata en el papel, lo que imposibilitaba la posibilidad de borrar.
Con un procesador de texto, en cambio, es posible borrar y editar el contenido en todo momento ya que su funcionalidad básica se realiza sobre la pantalla. 
Una vez que la tarea de redacción ya está completada, el usuario tiene la opción de guardar el documento en un soporte informático
(ya sea en el disco rígido de su computadora, en Internet o en CD) o de imprimir el material.
Pero este tipo de programas informáticos presentan además otro importante número de posibilidades
que son las que han hecho que pasen a ser piezas imprescindibles tanto en nuestra vida personal como en el ámbito laboral.
n concreto, nos permiten editar por completo un texto y hacerlo lo más atractivo posible.
Eso supone, entre otras, el dotarle de una tipografía concreta, un tamaño de letra determinado 
así como proceder a utilizar herramientas para resaltar determinadas palabras o frases. 
Es decir, nos da la oportunidad de usar recursos tales como la negrita, la cursiva o el subrayado.
Tampoco hay que olvidarse del conjunto de posibilidades que nos da en cuanto a alineación del texto
a espaciado entre párrafos, a las sangrías, al color de las letras e incluso a la inclusión de listas numeradas.
Más herramientas puestas a disposición de los usuarios de los procesadores de texto 
son la creación de tablas o la incorporación de elementos tales como cuadros de texto, hipervínculos, saltos de página, encabezados y pies de página.
Con todo ello, y haciendo empleo también de las diferencias herramientas de diseño de página se consiguen unos resultados espectaculares y unos documentos muy atractivos.
Otra opción que brindan los procesadores de texto es la utilización de un corrector ortográfico 
(una aplicación que detecta las faltas ortográficas y sugiere las correcciones necesarias) 
o de un diccionario de sinónimos (que recomienda palabras alternativas a las escritas sin que se altere el significado del texto).
Los procesadores de texto también permiten intercalar imágenes y distintos tipos de gráficos dentro del texto, 
lo que permite crear documentos más avanzados al no limitarse a las palabras escritas.'''
    
d = dict()
t = t.replace(',' '').replace('.' '').lower()
palabras = t.split()
for palabra in palabras:
    if palabra not in d:
        d[palabra] = 0
    d[palabra] += 1
return d
        
contador = Texto()
contador.contar_palabras()

