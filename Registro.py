#Este subproceso sirve para realizar el checking 
#Se pide el ingreso manual del codigo a verificar, Si existe el codigo, 
#aparecería una leyenda con codigo valido. Se sobreescribe dicha posicion con [].

class Registro:
    def __init__(self, boletoregistrado=None, codigodet=False, codigodev=None, columna=0, condicion=False, condicionvendido=False, fila=0, opcion=None):
        self.boletoregistrado = boletoregistrado
        self.codigodet = codigodet
        self.codigodev = codigodev
        self.columna = columna
        self.condicion = condicion
        self.condicionvendido = condicionvendido
        self.fila = fila
        self.opcion = opcion
        self.entrada = input

    def getRegistro(self, vendidas, novendidas):
        self.registro(vendidas, novendidas)

    def getColumna(self):
        return self.columna

    def getFila(self):
        return self.fila
    
    def registro(self, vendidas, novendidas):
        limpiar = LimpiarPantalla()
        mostrarVendidas = MostrarVendidas()
        #Se le pedira que ingrese el codigo a verificar.Debe ser ingresado manualmente. Si existe el codigo, apareceria una leyenda con codigo valido. Se sobreescribe dicha posicion con ].
        print("")
        self.condicion = True
        while self.condicion:
            print("                                        - Ingrese el código del ticket: ", end="")
            #Esta variable almacena el codigo de ticket que el agente verificador ingrese manualmente.
            self.codigodev = self.entrada().upper()
            self.codigodet = False
            self.condicionvendido = False
            for i in range(15):
                for j in range(15):
                    self.boletoregistrado = self.codigodev + "] "
                    #Esta condicion compara el ticket ingresado con cada elemento de la matriz de tickets vendidos
                    if vendidas[i][j] == self.codigodev:
                        self.condicion = False
                        self.fila = i
                        self.columna = j
                        #uando el ticket ingresado coincide con un elemento de la matriz, la variable codigoDet pasa a ser verdadera
                        self.codigodet = True
                        vendidas[i][j] = vendidas[i][j] + "] "
                    if vendidas[i][j] == self.boletoregistrado:
                        #Esta condicion evalua si un ticket ya fue ingresado anteriormente. 
                        self.condicionvendido = True

        limpiar.limpiarPantalla()
        mostrarVendidas.getMostrarVendidas(vendidas)
        # Las siguientes condiciones evaluan si el ticket ingresado es valido, si no es valido o si ya fue registrado. 
        if self.codigodet:
            print("")
            print("                                      *==========================================*")
            print("                                       * El Ticket ingresado  E S   V A L I D O *")
            print("                                      *==========================================*")
            print("")
        else:
            if self.condicionvendido:
                print("")
                print("                                      *========================================================*")
                print("                                       * El Ticket ingresado  Y A  F U E  R E G I S T R A D O *")
                print("                                      *=========================================================*")
                print("")
            else:
                print("")
                print("                                      *================================================*")
                print("                                       * El Ticket ingresado  N O   E S   V A L I D O *")
                print("                                      *================================================*")
                print("")

        # Este bucle permite la opción de registrar más tickets o regresar al menú principal.
        while True:
            print("                                        ¿Desea seguir registrando boletos?")
            print("                                        1.- Si.")
            print("                                        2.- No.")
            print("")
            opcion = input("                                        Opcion: ")
            if opcion == "2":
                self.condicion = False
                break
            elif opcion == "1":
                self.condicion = True
                break
            else:
                print("")
                print("                                      *================================================*")
                print("                                          * Ingrese una opcion  N O   V A L I D A *")
                print("                                      *================================================*")
                print("")