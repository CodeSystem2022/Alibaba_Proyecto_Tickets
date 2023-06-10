class Ventas:
    def __init__(self):
        self.cantcompra = 0
        self.cantdisponible = 0
        self.condicion = True
        self.contadorpalcoderecho = 0
        self.contadorpalcoizquierdo = 0
        self.contadorreservados = 0
        self.contadorvip = 0
        self.opcion = 0
        self.ticketsventa = []
        self.venta = False
        self.zona = 0

    def getVentas(self, vendidas, noVendidas):
        self.ventas(vendidas, noVendidas)

    def ventas(self, vendidas, noVendidas):
        mVendidas = MostrarVendidas()
        mNoVendidas = MostrarNoVendidas()
        mnVendidas = MostrarNoVendidas()
        cobro = Cobro()
        ticketsventa = [None] * 225
        condicion = True

        while condicion:
            opcion = 0
            limpiar = LimpiarPantalla()
            mNoVendidas.getMostrarNoVendidas(noVendidas)
            contadorpalcoizquierdo = 0
            contadorreservados = 0
            contadorvip = 0
            contadorpalcoderecho = 0

            for i in range(15):
                for j in range(15):
                    if noVendidas[i][j] != "      ":
                        if j <= 3:
                            contadorpalcoizquierdo += 1
                        elif j >= 4 and j <= 5:
                            contadorreservados += 1
                        elif j >= 6 and j <= 9:
                            contadorvip += 1
                        else:
                            contadorpalcoderecho += 1

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
            cantcompra = 0