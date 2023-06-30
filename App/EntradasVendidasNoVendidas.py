import random
from Database.Tickets import Tickets
from Database.Tickets_dao import TicketsDAO


class EntradasVendidasNoVendidas:

    def __init__(self):
        self.novendidas = None
        self.vendidas = None

    def get_novendidas(self, novendidas):
        return self.entradas_no_vendidas(novendidas)

    def get_vendidas(self, vendidas):
        return self.entradas_vendidas(vendidas)

    def set_novendidas(self, novendidas):
        self.novendidas = novendidas

    def set_vendidas(self, vendidas):
        self.vendidas = vendidas

    def entradas_vendidas(self, matriz):
        vendidas = [['       ' for _ in range(15)] for _ in range(15)]
        self.set_vendidas(vendidas)
        todasVendidas = True
        registros = TicketsDAO.seleccionarAll()
        for ticket in registros:
            if not ticket[2]:
                todasVendidas = False
        if todasVendidas:
            for i in range(15):
                for j in range(15):
                    simulador = random.randint(0, 30)

                    if simulador < 29:
                        vendidas[i][j] = matriz[i][j]
                    else:
                        vendidas[i][j] = '       '
                        ticketAct = Tickets(ticket=matriz[i][j], vendido=False)
                        TicketsDAO.actualizar(ticketAct)
        else:
            for i in range(15):
                for j in range(15):
                    ticketNum = Tickets(ticket=matriz[i][j])
                    ticketBus = TicketsDAO.seleccionarOne(ticketNum)
                    if ticketBus[2]:
                        vendidas[i][j] = matriz[i][j]
                    else:
                        vendidas[i][j] = '       '
        return vendidas

    def entradas_no_vendidas(self, matriz):
        novendidas = [['       ' for _ in range(15)] for _ in range(15)]
        self.set_novendidas(novendidas)
        for i in range(15):
            for j in range(15):
                if self.vendidas[i][j] == '       ':
                    novendidas[i][j] = matriz[i][j]
                else:
                    novendidas[i][j] = '       '
        return novendidas
