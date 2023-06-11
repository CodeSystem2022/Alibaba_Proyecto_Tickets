'''
Este código es una clase llamada MostrarVendidas que muestra una matriz de datos.
El objetivo principal del código es presentar de manera organizada los datos almacenados en la matriz vendidas en la consola.
Utiliza un bucle for para iterar sobre los elementos de la matriz
y realiza comprobaciones de longitud para determinar la impresión.
También utiliza la clase Pantallas para mostrar un título antes de imprimir la matriz.
'''


class MostrarVendidas:
    def __init__(self):
        pass

    def getMostrarVendidas(self, vendidas):
        self.mostrarvendidas(vendidas)

    def mostrarvendidas(self, vendidas):
        pantallas = Pantallas()
        j = 0
        pantallas.titulo()

        for i in range(15):
            if j <= 15 and len(vendidas[i][0]) <= 8:
                print(" ", end="")

            for j in range(15):
                if len(vendidas[i][j]) == 8:
                    print("[", end="")
                    print(vendidas[i][j] + "  ", end="")
                elif i <= 13 and j <= 13:
                    if len(vendidas[i][j + 1]) == 8:
                        print(vendidas[i][j] + "   ", end="")
                    else:
                        print(vendidas[i][j] + "    ", end="")
                else:
                    print(vendidas[i][j] + "    ", end="")

            print("")
