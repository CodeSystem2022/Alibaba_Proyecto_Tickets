import random
class EntradasTotales: #esta clase se encarga de generar y almacenar todos los codigos alfanumericos de las entradas
    def __init__(self):
        self.letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numeros = "0123456789"
        self.matriz = []  # Matriz para almacenar los códigos generados
        self.codigos_generados = set()  # Conjunto auxiliar para evitar la repetición de códigos

    def generar_codigo(self):
        codigo = ""
        while codigo == "" or codigo in self.codigos_generados:
            # Generamos un nuevo código aleatorio combinando letras y números
            codigo = random.choice(self.letras) + random.choice(self.letras) + random.choice(self.letras) + \
                     random.choice(self.numeros) + random.choice(self.numeros) + random.choice(self.numeros)
        self.codigos_generados.add(codigo)  # Agregamos el código generado al conjunto de códigos
        codigo_con_separador = "-".join([codigo[:3], codigo[3:]])  # Agregamos el guion como separador
        return codigo_con_separador

    def generar_matriz(self):
        for _ in range(15):
            fila = []
            for _ in range(15):
                codigo = self.generar_codigo()
                fila.append(codigo)
            self.matriz.append(fila)

    def imprimir_matriz(self):
        for fila in self.matriz:
            print(fila)

# Crear una instancia de la clase EntradasTotales
entradas = EntradasTotales()

# Generar y mostrar la matriz de códigos
entradas.generar_matriz()

# entradas.imprimir_matriz()
