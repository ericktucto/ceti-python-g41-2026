from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print("pagando monto de", monto)

class PagoYape(MetodoPago):
    def pagar(self, monto):
        print("pagando con yape, monto de", monto)


pago = PagoTarjeta()
pago.pagar(2000)