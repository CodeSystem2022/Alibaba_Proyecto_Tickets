from cursor_del_pool import CursorDelPool
from Facturacion import Facturacion


class FacturacionDAO:
    '''
    DAO - Data Access Object para la tabla de facturacion
    CRUD - Create - Read - Update - Delete para la tabla de facturacion
    '''
    _SELECT_ALL = 'SELECT * FROM facturacion ORDER BY id_factura'
    _INSERTAR = 'INSERT INTO facturacion(total_venta, cant_vendidas, descuento) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE facturacion SET password=%s, rol=%s WHERE usuario=%s'
    _ELIMINAR = 'DELETE FROM facturacion WHERE usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT_ALL)
            registros = cursor.fetchall()
            facturas = []
            for registro in registros:
                factura = Facturacion(registro[0], registro[1], registro[2], registro[3])
                facturas.append(factura)
            return facturas

    @classmethod
    def insertar(cls, factura):
        with CursorDelPool() as cursor:
            valores = (factura.total_venta, factura.cant_vendidas, factura.descuento)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
