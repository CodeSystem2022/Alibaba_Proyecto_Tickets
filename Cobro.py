# Datos Curiosos: En python no existe la sentencia Switch por lo que lo reemplace por un elif, tampoco existe la sentencia Do While por lo que utilice un While True con Break's para finalizar
# Esta clase se encarga de verificar la disponibilidad de tickets para vender.
# Tambien se encarga de realizar la venta y mostrar la facturacion de la venta

class Cobro:
    def __init__(self, cantcompra, cantdisponible, ticketsventa, zona):
        self._cantcompra = cantcompra
        self._cantdisponible = cantdisponible
        self._ticketsventa = ticketsventa
        self._zona = zona

    def getCobroTicket(self, cantcompra, cantdisponible, ticketsventa, zona):
        self.cobroTicket(cantcompra, cantdisponible, ticketsventa, zona)

    def cobroTicket(cantcompra, cantdisponible, ticketsventa, zona):
        l = 0
        rta = False
        subtotal = 0.0
        totalcompra = 0.0
        totaldesc = 0.0
        valorentrada = 0
        print("")

        # si la cantidad requerida para la compra es mayor a los tickets disponibles no se procede a la venta.
        if cantcompra > cantdisponible:
            print("El número de entradas solicitadas supera al número de entradas disponibles.")
        else:
            # si la venta es correcta, se mostraria en pantalla los tickets vendidos para la zona correspondiente.
            if zona == 1:
                print("TICKETS VENDIDOS EN PALCO IZQUIERDO: ")
            elif zona == 2:
                print("TICKETS VENDIDOS EN ZONA DE RESERVADOS: ")
            elif zona == 3:
                print("TICKETS VENDIDOS EN ZONA VIP: ")
            elif zona == 4:
                print("TICKETS VENDIDOS EN PALCO DERECHO: ")

            # Este bucle muestra las entradas asignadas en la última venta listas para facturar.
            for l in range(cantcompra):
                print("[" + ticketsventa[l] + "] ")
            print("")

            # Valor pre definido de la entrada
            valorentrada = 2000

            # subtotal
            subtotal = valorentrada * cantcompra
            print("")
            print("                     *=============================*")
            print("                      *   F A C T U R A C I O N   *")
            print("                     *=============================*")
            print("                Facturar la siguiente cantidad: " + str(cantcompra) + " Entradas")
            while True:
                strDescuento = input("                Ingrese el % de descuento: ")
                if strDescuento.isnumeric():
                    descuento = float(strDescuento)
                    if descuento >= 0 and descuento <= 100:
                        break
                    else:
                        print("                Debe ingresar un valor entre 0 y 100!!! ")
                        print("")
                else:
                    print("                Debe ingresar un valor entre 0 y 100!!! ")
                    print("")

            # descuento a aplicar
            totaldesc = (subtotal * descuento) / 100
            totalcompra = subtotal - totaldesc
            print("                --------------------------------")
            print("                Importe  total               : " + str(subtotal))
            print("                Descuento realizado          : " + str(totaldesc))
            print("                Total a pagar                : " + str(totalcompra))
            print("")

