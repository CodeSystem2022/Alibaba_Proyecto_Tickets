from Database.cursor_del_pool import CursorDelPool
from Database.Tickets import Tickets


class TicketsDAO:
    '''
    DAO - Data Access Object para la tabla de ticket
    CRUD - Create - Read - Update - Delete para la tabla de ticket
    '''
    _SELECT_ALL = 'SELECT * FROM tickets ORDER BY id_ticket'
    _SELECT_ALL_TKT = 'SELECT * FROM tickets WHERE id_ticket!=0 ORDER BY id_ticket ASC'
    _SELECT_ONE = 'SELECT * FROM tickets WHERE ticket=%s'
    _INSERTAR = 'INSERT INTO tickets(ticket, vendido, verificado) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE tickets SET vendido=%s WHERE ticket=%s'
    _ACTUALIZAR_VER = 'UPDATE tickets SET verificado=%s WHERE ticket=%s'
    _ELIMINAR = 'DELETE FROM tickets WHERE usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT_ALL)
            registros = cursor.fetchall()
            tickets = []
            for registro in registros:
                ticket = Tickets(registro[0], registro[1], registro[2], registro[3])
                tickets.append(ticket)
            return tickets

    @classmethod
    def seleccionarAll(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT_ALL_TKT)
            registros = cursor.fetchall()
            return registros

    @classmethod
    def seleccionarOne(cls, ticket):
        with CursorDelPool() as cursor:
            valor = (ticket.ticket,)
            cursor.execute(cls._SELECT_ONE, valor)
            registro = cursor.fetchone()
            return registro

    @classmethod
    def insertar(cls, ticket):
        with CursorDelPool() as cursor:
            valores = (ticket.ticket, ticket.vendido, ticket.verificado)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, ticket):
        with CursorDelPool() as cursor:
            valores = (ticket.vendido, ticket.ticket)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizarVer(cls, ticket):
        with CursorDelPool() as cursor:
            valores = (ticket.verificado, ticket.ticket)
            cursor.execute(cls._ACTUALIZAR_VER, valores)
            return cursor.rowcount
