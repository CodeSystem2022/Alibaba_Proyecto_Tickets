class Facturacion:
    def __init__(self, id_factura=None, total_venta=None, cant_vendidas=None, descuento=None):
        self._id_factura = id_factura
        self._total_venta = total_venta
        self._cant_vendidas = cant_vendidas
        self._descuento = descuento

    def __str__(self):
        return f'Factura: {self._id_factura} {self._total_venta} {self._cant_vendidas} {self._descuento}'

    @property
    def id_factura(self):
        return self._id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self._id_factura = id_factura

    @property
    def total_venta(self):
        return self._total_venta

    @total_venta.setter
    def total_venta(self, total_venta):
        self._total_venta = total_venta

    @property
    def cant_vendidas(self):
        return self._cant_vendidas

    @cant_vendidas.setter
    def cant_vendidas(self, cant_vendidas):
        self._cant_vendidas = cant_vendidas

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento
