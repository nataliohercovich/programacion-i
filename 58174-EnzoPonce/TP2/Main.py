from Cajero import billete,billete_100,billete_200,billete_500,billete_1000
from cajeroautomatico import Cajero_automatico

class Main():
    c = Cajero_automatico()
    cien = billete_100(100,'pesos','$100')
    doscientos = billete_200(200,'pesos','$200')
    quinientos = billete_500(500,'pesos','$500')
    mil = billete_1000(1000,'pesos','$1000') 
    
    c.agregar_dinero([cien,cien,cien,cien,cien,cien,cien,cien,cien,cien,cien,doscientos,doscientos,quinientos,quinientos,mil,mil,mil,mil,mil,mil])
    c.contar_dinero()
    c.extraer_dinero(5000,20)
    c.extraer_dinero_cambio()
    c.imprimir()
    
