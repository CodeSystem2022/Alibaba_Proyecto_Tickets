from MostrarNoVendidas import MostrarNoVendidas


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

    def getVentas(self, vendidas, noVendidas):
        self.ventas(vendidas, noVendidas)

    def ventas(self, vendidas, noVendidas):
        mVendidas = MostrarVendidas()   # Instancia de la clase MostrarVendidas
        mNoVendidas = MostrarNoVendidas()   # Instancia de la clase MostrarNoVendidas
        cobro = Cobro()   # Instancia de la clase Cobro
        ticketsventa = [None] * 225   # Lista para almacenar los tickets de venta
        condicion = True

        while condicion:
            opcion = 0
            limpiar = LimpiarPantalla()   # Instancia de la clase LimpiarPantalla
            mNoVendidas.getMostrarNoVendidas(noVendidas)   # Llama al método getMostrarNoVendidas de la instancia mNoVendidas
            contadorpalcoizquierdo = 0
            contadorreservados = 0
            contadorvip = 0
            contadorpalcoderecho = 0

            for i in range(15):
                for j in range(15):
                    if noVendidas[i][j] != "      ":
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
            print("                                                 4.- Palco derecho          : " + str(contadorpalcoderecho))
            print("                                                5.- Salir.")
            print("")
            zona = int(input("                                                Ingrese la zona donde desea vender: "))
            cantcompra = 0   # La variable "cantcompra" representa la cantidad de tickets que desea comprar.
