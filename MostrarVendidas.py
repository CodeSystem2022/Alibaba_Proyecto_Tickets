'''
Este código es una clase llamada MostrarVendidas que muestra una matriz de datos.
El objetivo principal del código es presentar de manera organizada los datos almacenados en la matriz vendidas en la consola.
Utiliza un bucle for para iterar sobre los elementos de la matriz
y realiza comprobaciones de longitud para determinar la impresión.
También utiliza la clase Pantallas para mostrar un título antes de imprimir la matriz.
'''
from Pantalla import Pantalla
from Tickets import Tickets
from Tickets_dao import TicketsDAO

class MostrarVendidas:

    def __init__(self):
        pass

    def getMostrarVendidas(vendidas):
        MostrarVendidas.mostrarvendidas(vendidas)

    def mostrarvendidas(vendidas):
        j = 0
        Pantalla.titulo()

        for i in range(15):
            if j <= 15 and len(vendidas[i][0]) <= 8:
                print(" ", end=" ")

            for j in range(15):
                existe = Tickets(ticket=vendidas[i][j])
                if existe:
                    ticketBus = TicketsDAO.seleccionarOne(existe)
                    if ticketBus:
                        if ticketBus[3]:
                            vendidas[i][j] = vendidas[i][j] + "]"
                if len(vendidas[i][j]) == 8:
                    print("[", end="")
                    print(vendidas[i][j] + "  ", end=" ")
                elif i <= 13 and j <= 13:
                    if len(vendidas[i][j + 1]) == 8:
                        print(vendidas[i][j] + "   ", end="")
                    else:
                        print(vendidas[i][j] + "    ", end="")
                else:
                    print(vendidas[i][j] + "    ", end="")

            print("")
