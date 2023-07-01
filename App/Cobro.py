# Datos Curiosos: En python no existe la sentencia Switch por lo que lo reemplace por un elif, tampoco existe la sentencia Do While por lo que utilice un While True con Break's para finalizar


from Database.Facturacion import Facturacion
from Database.Facturacion_dao import FacturacionDAO
from Database.Tickets import Tickets
from Database.Tickets_dao import TicketsDAO


class Cobro:

    def __init__(self, cantcompra=None, cantdisponible=None, ticketsventa=None, zona=None):
        self._cantcompra = cantcompra
        self._cantdisponible = cantdisponible
        self._ticketsventa = ticketsventa
        self._zona = zona

    def getCobroTicket(cantcompra, cantdisponible, ticketsventa, zona):
        Cobro.cobroTicket(cantcompra, cantdisponible, ticketsventa, zona)

    def cobroTicket(cantcompra, cantdisponible, ticketsventa, zona):

        print("")

        # si la cantidad requerida para la compra es mayor a los tickets disponibles no se procede a la venta.
        if cantcompra > cantdisponible:
            print(
                "                                                El número de entradas solicitadas supera al número de entradas disponibles.")
        else:
            # si la venta es correcta, se mostraria en pantalla los tickets vendidos para la zona correspondiente.
            if zona == 1:
                print("                                                TICKETS VENDIDOS EN PALCO IZQUIERDO: ", end="")
            elif zona == 2:
                print("                                                TICKETS VENDIDOS EN ZONA DE RESERVADOS: ",
                      end="")
            elif zona == 3:
                print("                                                TICKETS VENDIDOS EN ZONA VIP: ", end="")
            elif zona == 4:
                print("                                                TICKETS VENDIDOS EN PALCO DERECHO: ", end="")

            # Este bucle muestra las entradas asignadas en la última venta listas para facturar.
            for l in range(cantcompra):
                print("[" + ticketsventa[l] + "] ", end="")
            print("")

            # Valor pre definido de la entrada
            valorentrada = 2000

            # subtotal
            subtotal = valorentrada * cantcompra
            print("")
            print("                                                *=============================*")
            print("                                                 *   F A C T U R A C I O N   *")
            print("                                                *=============================*")
            print("                                                Facturar la siguiente cantidad: " + str(
                cantcompra) + " Entradas")
            while True:
                strDescuento = input("                                                Ingrese el % de descuento: ")
                if strDescuento.isnumeric():
                    descuento = float(strDescuento)
                    if descuento >= 0 and descuento <= 100:
                        break
                    else:
                        print(
                            "                                                Debe ingresar un valor entre 0 y 100!!! ")
                        print("")
                else:
                    print("                                                Debe ingresar un valor entre 0 y 100!!! ")
                    print("")

            # descuento a aplicar
            totaldesc = (subtotal * descuento) / 100
            totalcompra = subtotal - totaldesc
            factura1 = Facturacion(total_venta=totalcompra, cant_vendidas=cantcompra, descuento=descuento)
            FacturacionDAO.insertar(factura1)
            for i in range(cantcompra):
                ticketAct = Tickets(ticket=ticketsventa[i], vendido=True)
                TicketsDAO.actualizar(ticketAct)
            print("                                                --------------------------------")
            print("                                                Importe  total               : " + str(subtotal))
            print("                                                Descuento realizado          : " + str(totaldesc))
            print("                                                Total a pagar                : " + str(totalcompra))
            print("")
