# esta clase se encarga de generar y almacenar todos los codigos alfanumericos de las entradas
import random

class EntradasTotales:

    def __init__(self):
        self._letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._numeros = "0123456789"
        self._matriz = []  # Matriz para almacenar los códigos generados
        self._codigosGenerados = set()  # Conjunto auxiliar para evitar la repetición de códigos

    def generar_codigo(self):
        codigo = ""
        while codigo == "" or codigo in self._codigosGenerados:
            # Generamos un nuevo código aleatorio combinando letras y números
            codigo = random.choice(self._letras) + random.choice(self._letras) + random.choice(self._letras) + \
                     random.choice(self._numeros) + random.choice(self._numeros) + random.choice(self._numeros)
        self._codigosGenerados.add(codigo)  # Agregamos el código generado al conjunto de códigos
        codigoConSeparador = "-".join([codigo[:3], codigo[3:]])  # Agregamos el guion como separador
        return codigoConSeparador

    def generar_matriz(self):
        for _ in range(15):
            fila = []
            for _ in range(15):
                codigo = self.generar_codigo()
                fila.append(codigo)
            self._matriz.append(fila)
        return self._matriz

    def imprimir_matriz(self):
        for fila in self._matriz:
            print(fila)

if __name__ == '__main__':
    # Crear una instancia de la clase EntradasTotales
    entradas = EntradasTotales()
    # Generar y mostrar la matriz de códigos
    lista = entradas.generar_matriz()
    print(lista[12][2])
    entradas.imprimir_matriz()
