'''
Esta clase es el Main
Desde esta clase se llaman a los metodos de otras clases
para crear la matriz a la cual despues a traves de otra clase se le van a habilitar tickets
Tambien va a ser la clase que llama y muestra el Log In y el Menu
'''
from App.EntradasVendidasNoVendidas import EntradasVendidasNoVendidas
from App.GeneradorDeCodigos import EntradasTotales
from App.Menu import Menu
from App.Pantalla import Pantalla
import time

login = Pantalla()
menu = Menu()
entradas = EntradasTotales()
matriz = entradas.generar_matriz()
escenario = EntradasVendidasNoVendidas()
vendidas = escenario.get_vendidas(matriz)
noVendidas = escenario.get_novendidas(matriz)

if login.validacion:
    Pantalla.LimpiarPantalla()
    menu.menu(vendidas, noVendidas)
else:
    print("")
    print("                                     Se vencieron los intentos de inicio de sesion!!!")
    print("")
    time.sleep(3)
    login.mensajesalida()
