'''
Esta clase es el Main
Desde esta clase se llaman a los metodos de otras clases
para crear la matriz a la cual despues a traves de otra clase se le van a habilitar tickets
Tambien va a ser la clase que llama y muestra el Log In y el Menu
'''

from Menu import Menu
from GeneradorDeCodigos import EntradasTotales


class ProyectoTickets:
    def __init__(self):
        self.validacion = False

    def main(self):
        
        # Instancio las clases para poder llamar a los métodos y funciones
        login = Pantallas()
        entradas = EntradasTotales()
        escenario = EntradasVendidasNoVendidas()
        menu = Menu()
        limpiar = LimpiarPantalla()

        # Creo la matriz general y le habilito tickets para poder vender en puerta
        matriz = entradas.getMatriz()
        vendidas = escenario.getVendidas(matriz)
        novendidas = escenario.getNovendidas(matriz)

        # Configuración de Login
        login.setUsuario("alibaba")
        login.setContrasenia("alibaba123")
        login.setIntentos(3)

        # Valido el Login del usuario
        if login.getValidacion():
            limpiar.limpiarPantalla()
            menu.getMenu(vendidas, novendidas)
        else:
            print("\n\nSe vencieron los intentos de inicio de sesión!!!\n\n")
            limpiar.limpiarPantalla()
            login.mensajesalida()

# Creo el objeto Proyecto Tickets
proyecto_tickets = ProyectoTickets()

# Invoco el metodo main() para ejecutar el programa
proyecto_tickets.main()
