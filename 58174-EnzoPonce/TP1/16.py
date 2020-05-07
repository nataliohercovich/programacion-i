class lectura():
    
    def leer(self):
        archivo = open('15.txt', 'r')
        texto = archivo.readlines()
        print(texto)
        num = 0
        archivo.seek(0)
        for i in texto:
            num = num+1
            print("venta numero", str(num),":")
            r=i.split(",")
            print(('Nombre:{c}, Monto:{m}, Descripcion:{d}, Forma de pago:{p}'). format(
                c=r[0],
                m=r[1],
                d=r[2],
                p=r[3]))
        
tex = lectura()
tex.leer()
