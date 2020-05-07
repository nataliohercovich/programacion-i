from tarjetaCredito import TarjetadeCredito

class Venta():

    def __init__(self,linea):
        self.linea_venta=linea
        self.lista_venta=[]
        self.monto=linea[4]
        self.descripcion=linea[5]
        self.tarjeta=TarjetadeCredito(self.linea_venta[0],self.linea_venta[1],self.linea_venta[2],self.linea_venta[3])
        
    def getMonto(self):
        return self.monto
    
    def getDescripcion(self):
        return self.descripcion


    def setValores(self):
        self.lista_venta.append(self.tarjeta.getNombre())
        self.lista_venta.append(self.tarjeta.getNumero_Tarjeta())
        self.lista_venta.append(self.tarjeta.getCodigo_Tarjeta())
        self.lista_venta.append(self.tarjeta.getTipo_Tarjeta())
        self.lista_venta.append(self.monto)
        self.lista_venta.append(self.descripcion)

    def getValores(self):
        return self.lista_venta