"""
La clase MostrarNoVendidas es responsable de mostrar en pantalla los tickets disponibles
para la compra en la puerta de un evento. Su funcionalidad principal se encuentra en el método mostrarnovendidas,
el cual recibe una matriz novendidas que contiene la información de los tickets disponibles.
El método mostrarnovendidas itera sobre los elementos de la matriz y los imprime en pantalla de manera formateada.
Los tickets se muestran en filas y columnas, y se aplican ajustes en la cantidad de espacios en blanco dependiendo
de la longitud del contenido de cada ticket. Además, la clase hace uso de la clase Pantallas para mostrar un título
en la pantalla antes de mostrar los tickets.
"""

class MostrarNoVendidas:
    def __init__(self):
        pass

    def getMostrarNoVendidas(self, novendidas):
        self.mostrarnovendidas(novendidas)

    # muestra en pantalla los tickets disponibles para comprar en puerta
    def mostrarnovendidas(self, novendidas):
        pantallas = Pantallas()

        j = 0
        pantallas.titulo()  # Llama al método "titulo" de la clase "Pantallas"
        for i in range(15):
            if j <= 15:
                if len(novendidas[i][0]) <= 8:
                    print(" ", end="")  # Imprime un espacio en blanco
            for j in range(15):
                if len(novendidas[i][j]) == 8:
                    print("[" + novendidas[i][j] + "  ",
                          end="")  # Imprime el ticket con corchetes y dos espacios en blanco
                else:
                    if i <= 13 and j <= 13:
                        if len(novendidas[i][j + 1]) == 8:
                            print(novendidas[i][j] + "   ", end="")  # Imprime el ticket con tres espacios en blanco
                        else:
                            print(novendidas[i][j] + "    ", end="")  # Imprime el ticket con cuatro espacios en blanco
                    else:
                        print(novendidas[i][j] + "    ", end="")  # Imprime el ticket con cuatro espacios en blanco
            print("")
