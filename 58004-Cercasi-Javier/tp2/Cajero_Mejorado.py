from Cajero import (Cajero, ExcesoError, MultipoError)


class CajeroMejorado(Cajero):

    def extraer_dinero_cambio(self, pedido, porcentaje):

        self.transaccion = True
        n = 0

        try:
            if self.suma < pedido:
                raise ExcesoError

        except ExcesoError:
            self.transaccion = False
            return("Error: Fondos del banco insuficientes")

        try:
            if pedido % 100 != 0:
                raise MultipoError

        except MultipoError:
            self.transaccion = False
            return("Error: El monto no es multiplo de 100")

        redondeo = a = int((porcentaje/100) * pedido)

        if (a % 100) != 0:

            b = int(str(a)[-2] + str(a)[-1])
            c = (100 - b) + b
            redondeo = a - b + c

        try:
            resto = self.extraer(pedido - redondeo, redondeo)
            resto += redondeo
        except:
            resto = redondeo

        while (resto != 0) and (self.transaccion is True):

            if (len(self.cien) != 0) and (resto >= 100):

                self.cien.pop()      # Sacar el ultimo elemento de la lista
                resto -= 100
                self.entrega.append(100)

            if (len(self.cien) == 0):
                n += 1

                if n > 5:
                    return("No es posible realizar esa transaccion")
                    exit()

                if (len(self.doscien) != 0) and (resto >= 200):

                    self.doscien.pop()
                    resto -= 200
                    self.entrega.append(200)

                elif (resto >= 500) and ((len(self.quini) != 0) or
                                         ((len(self.doscien) == 0) and
                                         (len(self.quini) != 0))):
                    self.quini.pop()
                    resto -= 500
                    self.entrega.append(500)

                elif (resto >= 1000) and ((len(self.mil) != 0) or
                                          ((len(self.quini) == 0) and
                                          (len(self.mil) != 0))):

                    self.mil.pop()
                    resto -= 1000
                    self.entrega.append(1000)

        return(self.entrega.count(1000), self.entrega.count(500),
               self.entrega.count(200), self.entrega.count(100))
