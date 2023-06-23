'''
Esta clase es el Main
Desde esta clase se llaman a los metodos de otras clases
para crear la matriz a la cual despues a traves de otra clase se le van a habilitar tickets
Tambien va a ser la clase que llama y muestra el Log In y el Menu
'''
from EntradasVendidasNoVendidas import EntradasVendidasNoVendidas
from GeneradorDeCodigos import EntradasTotales
from Menu import Menu
from Pantalla import Pantalla

login = Pantalla(3, "alibaba", "alibaba123", False)
menu = Menu()
entradas = EntradasTotales()
matriz = entradas.generar_matriz()
escenario = EntradasVendidasNoVendidas()
vendidas = escenario.get_vendidas(matriz)
noVendidas = escenario.get_novendidas(matriz)


if login.validacion:
    menu.menu(vendidas, noVendidas)
else:
    print("")
    print("                                     Se vencieron los intentos de inicio de sesion!!!")
    print("")
    login.mensajesalida()
