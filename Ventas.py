# from LimpiarPantalla import LimpiarPantalla
from MostrarNoVendidas import MostrarNoVendidas
from Cobro import Cobro

"""
Esta clase implementa un sistema de venta de tickets que permite al usuario seleccionar una zona
y la cantidad de tickets que desea comprar. Los tickets vendidos se mueven de la lista de tickets no vendidos 
a la lista de tickets vendidos, y se muestra el monto total de la venta. 
El proceso de venta continúa hasta que el usuario decida salir del programa.
"""

class Ventas:
    def __init__(self):
        self.cantcompra = 0   # Variable para almacenar la cantidad de tickets a comprar
        self.cantdisponible = 0   # Variable para almacenar la cantidad de tickets disponibles
        self.condicion = True   # Variable para controlar la condición del bucle
        self.contadorpalcoderecho = 0   # Contador de tickets en la zona de Palco derecho
        self.contadorpalcoizquierdo = 0   # Contador de tickets en la zona de Palco izquierdo
        self.contadorreservados = 0   # Contador de tickets en la zona reservada
        self.contadorvip = 0   # Contador de tickets en la zona VIP
        self.opcion = 0   # Opción seleccionada por el usuario
        self.ticketsventa = []   # Lista para almacenar los tickets de venta
        self.venta = False   # Variable para controlar si se realizó una venta
        self.zona = 0   # Variable para almacenar la zona seleccionada por el usuario

    def getVentas(vendidas, noVendidas):
        Ventas.ventas(vendidas, noVendidas)

    def ventas(vendidas, noVendidas):
        mNoVendidas = MostrarNoVendidas()   # Instancia de la clase MostrarNoVendidas
        # cobro = Cobro.getCobroTicket()   # Instancia de la clase Cobro
        ticketsventa = [None] * 225   # Lista para almacenar los tickets de venta
        condicion = True

        while condicion:
            opcion = 0
            # limpiar = LimpiarPantalla()   # Instancia de la clase LimpiarPantalla
            mNoVendidas.getMostrarNoVendidas(noVendidas)   # Llama al método getMostrarNoVendidas de la instancia mNoVendidas
            contadorpalcoizquierdo = 0
            contadorreservados = 0
            contadorvip = 0
            contadorpalcoderecho = 0

            for i in range(15):
                for j in range(15):
                    if noVendidas[i][j] != "       ":
                        if j <= 3:
                            contadorpalcoizquierdo += 1  # Incrementa el contador de tickets en la zona de Palco izquierdo
                        elif j >= 4 and j <= 5:
                            contadorreservados += 1  # Incrementa el contador de tickets en la zona reservada
                        elif j >= 6 and j <= 9:
                            contadorvip += 1  # Incrementa el contador de tickets en la zona VIP
                        else:
                            contadorpalcoderecho += 1  # Incrementa el contador de tickets en la zona de Palco derecho

            print("")
            print("")
            print("")
            print("                                              *=========================================*")
            print("                                               *   TICKETS DISPONIBLES PARA LA VENTA   *")
            print("                                              *=========================================*")
            print("                                                1.- Palco izquierdo        : " + str(contadorpalcoizquierdo))
            print("                                                2.- Zona reservada         : " + str(contadorreservados))
            print("                                                3.- Zona vip               : " + str(contadorvip))
            print("                                                4.- Palco derecho          : " + str(contadorpalcoderecho))
            print("                                                5.- Salir.")
            print("")
            zona = int(input("                                                Ingrese la zona donde desea vender: "))

            cantcompra = 0   # La variable "cantcompra" representa la cantidad de tickets que desea comprar.
            while True:
                # Condicional multiple para vender los tickets de acuerdo a la zona requerida
                if zona == 1:
                    cantcompra = int(input(
                        "                                                Ingrese la cantidad de tickets que desea vender: "))
                    # se almacena la cantidad de tickets disponibles de la zona requerida en la variable cantDisponible
                    cantdisponible = contadorpalcoizquierdo
                    # se verifica que la cantidad de entradas disponibles sea mayor a la requerida
                    if cantdisponible >= cantcompra:
                        # Este bucle permite la asignacion de entradas segun la cantidad requerida para venta.
                        for l in range(cantcompra):
                            venta = True
                            for i in range(15):
                                for j in range(4):
                                    if not noVendidas[i][j] == "       " and venta:
                                        # Cada vez que se vende una entrada se la mueva a la matriz de entradas vendidas
                                        vendidas[i][j] = noVendidas[i][j]
                                        ticketsventa[l] = noVendidas[i][j]
                                        # el ticket vendido autmaticamente es reescrito con caracteres vacios dentro de la matriz de entradas no Vendidas
                                        noVendidas[i][j] = "       "
                                        venta = False
                    Cobro.getCobroTicket(cantcompra, cantdisponible, ticketsventa, zona)
                elif zona == 2:
                    cantcompra = int(input(
                        "                                                Ingrese la cantidad de tickets que desea vender: "))
                    # se almacena la cantidad de tickets disponibles de la zona requerida en la variable cantDisponible
                    cantdisponible = contadorreservados
                    # se verifica que la cantidad de entradas disponibles sea mayor a la requerida
                    if cantdisponible >= cantcompra:
                        # Este bucle permite la asignacion de entradas segun la cantidad requerida para venta.
                        for l in range(cantcompra):
                            venta = True
                            for i in range(15):
                                for j in range(4, 6):
                                    if not noVendidas[i][j] == "       " and venta:
                                        # Cada vez que se vende una entrada se la mueva a la matriz de entradas vendidas
                                        vendidas[i][j] = noVendidas[i][j]
                                        ticketsventa[l] = noVendidas[i][j]
                                        # el ticket vendido automaticamente es reescrito con caracteres vacios dentro de la matriz de entradas no Vendidas
                                        noVendidas[i][j] = "       "
                                        venta = False
                    Cobro.getCobroTicket(cantcompra, cantdisponible, ticketsventa, zona)
                elif zona == 3:
                    cantcompra = int(input(
                        "                                                Ingrese la cantidad de tickets que desea vender: "))
                    # se almacena la cantidad de tickets disponibles de la zona requerida en la variable cantDisponible
                    cantdisponible = contadorvip
                    # se verifica que la cantidad de entradas disponibles sea mayor a la requerida
                    if cantdisponible >= cantcompra:
                        # Este bucle permite la asignacion de entradas segun la cantidad requerida para venta.
                        for l in range(cantcompra):
                            venta = True
                            for i in range(15):
                                for j in range(6, 10):
                                    if not noVendidas[i][j] == "       " and venta:
                                        # Cada vez que se vende una entrada se la mueva a la matriz de entradas vendidas
                                        vendidas[i][j] = noVendidas[i][j]
                                        ticketsventa[l] = noVendidas[i][j]
                                        # el ticket vendido autmaticamente es reescrito con caracteres vacios dentro de la matriz de entradas no Vendidas
                                        noVendidas[i][j] = "       "
                                        venta = False
                    Cobro.getCobroTicket(cantcompra, cantdisponible, ticketsventa, zona)
                elif zona == 4:
                    cantcompra = int(input(
                        "                                                Ingrese la cantidad de tickets que desea vender: "))
                    # se almacena la cantidad de tickets disponibles de la zona requerida en la variable cantDisponible
                    cantdisponible = contadorpalcoderecho
                    # se verifica que la cantidad de entradas disponibles sea mayor a la requerida
                    if cantdisponible >= cantcompra:
                        # Este bucle permite la asignacion de entradas segun la cantidad requerida para venta.
                        for l in range(cantcompra):
                            venta = True
                            for i in range(15):
                                for j in range(10, 15):
                                    if not noVendidas[i][j] == "       " and venta:
                                        # Cada vez que se vende una entrada se la mueva a la matriz de entradas vendidas
                                        vendidas[i][j] = noVendidas[i][j]
                                        ticketsventa[l] = noVendidas[i][j]
                                        # el ticket vendido autmaticamente es reescrito con caracteres vacios dentro de la matriz de entradas no Vendidas
                                        noVendidas[i][j] = "       "
                                        venta = False
                    Cobro.getCobroTicket(cantcompra, cantdisponible, ticketsventa, zona)
                elif zona == 5:
                    opcion = 2
                    condicion = False

                if zona == 1 or zona == 2 or zona == 3 or zona == 4 or zona == 5:
                    break
            opcion = 0
            while opcion != 1 and opcion != 2:
                print("")
                print("                                                      ¿Que desea hacer?")
                print("                                                      1. Seguir vendiendo.")
                print("                                                      2. Regresar al menu principal.")
                print("")
                opcion = int(input("                                                      Opcion: "))
                if opcion == 1:
                    condicion = True
                # Esta condicion permite regresar al menu principal
                if opcion == 2:
                    condicion = False
                    # limpiar.limpiarPantalla()