
from App.MostrarVendidas import MostrarVendidas
from App.Pantalla import Pantalla
from App.Registro import Registro
from App.Ventas import Ventas


class Menu:

    def __init__(self):
        self._opcion = ""
        self._salir = False

    def menu(self, vendidas, novendidas):

        while not self._salir:
            Pantalla.diseniomenu()
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

