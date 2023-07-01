# esta clase se encarga de generar y almacenar todos los codigos alfanumericos de las entradas
import random
from Database.Tickets import Tickets
from Database.Tickets_dao import TicketsDAO


class EntradasTotales:

    def __init__(self):
        self._letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._numeros = "0123456789"
        self._matriz = []               # Matriz para almacenar los códigos generados
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
        existe = TicketsDAO.seleccionar()
        lista = []
        if not existe:
            for _ in range(15):
                fila = []
                for _ in range(15):
                    codigo = self.generar_codigo()
                    fila.append(codigo)
                self._matriz.append(fila)
            tickets = self._matriz
            for i in range(15):
                for j in range(15):
                    ticketN = Tickets(ticket=tickets[i][j], vendido=True, verificado=False)
                    TicketsDAO.insertar(ticketN)
        else:
            tickets = TicketsDAO.seleccionarAll()
            for ticket in tickets:
                lista.append(ticket[1])
            self._matriz = [lista[i:i + 15] for i in range(0, len(lista), 15)]
        return self._matriz

    def imprimir_matriz(self):
        for fila in self._matriz:
            print(fila)

