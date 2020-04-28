class TarjetadeCredito():

    def __init__(self,nombre,numero_tarjeta,codigo_tarjeta,tipo_tarjeta):
        self.nombre=nombre
        self.numero_tarjeta=numero_tarjeta
        self.codigo_tarjeta=codigo_tarjeta
        self.tipo_tarjeta=tipo_tarjeta
    
    def getNombre(self):
        return self.nombre
    
    def getNumero_Tarjeta(self):
        return self.numero_tarjeta
    
    def getCodigo_Tarjeta(self):
        return self.codigo_tarjeta
    
    def getTipo_Tarjeta(self):
        return self.tipo_tarjeta