
from MostrarNoVendidas import MostrarNoVendidas
from MostrarVendidas import MostrarVendidas
from Pantalla import Pantalla
from Registro import Registro
from Ventas import Ventas

class Menu:

    def __init__(self):
        self._opcion = ""
        self._salir = False

    def menu(self, vendidas, novendidas):

        while not self._salir:
            Pantalla.diseniomenu(self)
            print("")
            self._opcion = input("                                        Elija una opción:")
            print("")
            if self._opcion == "1":
                print("")
                MostrarVendidas.getMostrarVendidas(vendidas)
                Registro.registro(self, vendidas, novendidas)
            elif self._opcion == "2":
                Ventas.getVentas(vendidas, novendidas)
            elif self._opcion == "3":
                Pantalla.mensajesalida(self)
                self._salir = True

    def disenio_menu(self):
        # Implementa el diseño del menú aquí
        pass

    def mostrar_vendidas(vendidas):
        # Implementa la lógica para mostrar las entradas vendidas aquí
        pass

    def registro(vendidas, novendidas):
        # Implementa la lógica para el registro de entradas aquí
        pass

    def ventas(novendidas, vendidas):
        # Implementa la lógica para las ventas aquí
        pass

    def mensaje_salida(self):
        # Implementa el mensaje de salida aquí
        pass
