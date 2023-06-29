from Usuarios import Usuario
from Usuario_dao import UsuarioDAO


class Pantalla:

    def __init__(self, intentos=3, usuario=None, contrasenia=None, validacion=False):
        self._intentos = intentos
        self._usuario = usuario
        self._contrasenia = contrasenia
        self._validacion = validacion

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, intentos):
        self._intentos = intentos

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, contrasenia):
        self._contrasenia = contrasenia

    @property
    def validacion(self):
        self._ingresousuario()
        return self._validacion

    def titulo():
        print("")
        print("                                                 *=====================================*")
        print("                                                 *  E N T R A D A S   V E N D I D A S  *")
        print("                                                 *=====================================*")
        print(
            "                             ______   _____   ______    ______    _   __    ___     ____     ____   ____ ")
        print(
            "                            / ____/  / ___/  / ____/   / ____/   / | / /   /   |   / __\\   /  _/  / __ \\")
        print(
            "                           / __/     \\__\\ / /       / __/     /  |/ /   / /| |  / /_/ /   / /   / / / /")
        print(
            "                          / /___    ___/ / / /___    / /___    / /|  /   / ___ | / _, _/  _/ /   / /_/ / ")
        print(
            "                         /_____/   /____/  \\____/   /_____/  /_/ |_/   /_/  |_|/_/ |_|  /___/  \\____/  ")
        print(
            "           --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print(
            "           __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print(
            " ||----*----  PALCO IZQUIERDO  ----*----||   || * RESERVADO * || " + "     ||*--*--*--* ZONA   V I P *--*--*--*|| " + "      ||  ---**---   PALCO   DERECHO    ---**---  ||")
        print("")

    def _ingresousuario(self):
        print("")
        print(
            "        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print(
            "        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print(
            "               :::        :::        :::::::::::        :::::::::           :::        :::::::::           ::: ")
        print(
            "             :+: :+:      :+:            :+:            :+:    :+:        :+: :+:      :+:    :+:        :+: :+:")
        print(
            "            +:+   +:+     +:+            +:+            +:+    +:+       +:+   +:+     +:+    +:+       +:+   +:+ ")
        print(
            "           +#++:++#++:    +#+            +#+            +#++:++#+       +#++:++#++:    +#++:++#+       +#++:++#++:")
        print(
            "           +#+     +#+    +#+            +#+            +#+    +#+      +#+     +#+    +#+    +#+      +#+     +#+   ")
        print(
            "           #+#     #+#    #+#            #+#            #+#    #+#      #+#     #+#    #+#    #+#      #+#     #+#   ")
        print(
            "           ###     ###    ########## ###########        #########       ###     ###    #########       ###     ###     ")
        print("")
        print(
            "        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print(
            "        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print(
            "                        |     __   __       __   __   __     __   __    __   __ __  __    __    __    __  __   __")
        print(
            "                        |   /  \\ ( _      |__) |__) /  \\  / _  |__)   /\\  |\\/|  /\\  |  \\ /  \\ |__) |_  (_  ")
        print(
            "                   \\/  |__ \\__/  __)     |    | \\ \\__/ \\__) | \\  /--\\ |   | /--\\ |__// \\__/ | \\ |__ __) ")
        print(
            "                    /                                                                                     ")
        print("")
        print("")

        '''Este bucle nos mantiene en la pantalla principal hasta que se ingrese el usuario y contraseña correctos.'''
        while True:
            # ingUsuario = input("                                     Escriba un Usuario: ")
            # ingContrasenia = input("                                     Escriba una Contraseña: ")
            dbUsuario = UsuarioDAO.seleccionarOne()

            self._intentos = self._intentos - 1
            if dbUsuario:
                try:
                    print("")
                    print("                                       B I E N V E N I D O  A  S U  C A M P U S ")
                    self._validacion = True
                except Exception as ex:
                    print("Error: ", ex)
            else:
                print("")
                print("                                     Usuario o contraseña INCORRECTA, ¡VERIFIQUE SUS DATOS! ")
                print("")
                print("                                     Le restan " + str(self._intentos) + " intentos")
                print("")

            if self._validacion == True or self._intentos == 0:
                break

    def diseniomenu(self):
        # limpiar.limpiarPantalla()
        print("")
        print("")
        print("")
        print(
            "_________________________________________________________________________________________________________")
        print("     B i e n v e n i d o  a l  P r o g r a m a  d e  C h e c k i n g  y  V e n t a Ali Baba V2.0.0 ")
        print(
            "=========================================================================================================")
        print("")
        print("")
        print("                                     Elija una de las siguientes opciones:")
        print("")
        print("                                     1.- Verificacion de tickets.")
        print("                                     2.- Venta de tickets. ")
        print("                                     3.- Salir.")

    def mensajesalida(self):
        print("")
        print(
            "        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print(
            "        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print(
            "               :::        :::        :::::::::::        :::::::::           :::        :::::::::           ::: ")
        print(
            "             :+: :+:      :+:            :+:            :+:    :+:        :+: :+:      :+:    :+:        :+: :+:")
        print(
            "            +:+   +:+     +:+            +:+            +:+    +:+       +:+   +:+     +:+    +:+       +:+   +:+ ")
        print(
            "           +#++:++#++:    +#+            +#+            +#++:++#+       +#++:++#++:    +#++:++#+       +#++:++#++:")
        print(
            "           +#+     +#+    +#+            +#+            +#+    +#+      +#+     +#+    +#+    +#+      +#+     +#+   ")
        print(
            "           #+#     #+#    #+#            #+#            #+#    #+#      #+#     #+#    #+#    #+#      #+#     #+#   ")
        print(
            "           ###     ###    ########## ###########        #########       ###     ###    #########       ###     ###     ")
        print("")
        print(
            "        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print(
            "        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print(
            "                        |    __   __       __   __   __    __   __    __   __ __  __    __    __    __  __   __")
        print(
            "                        |   /  \\ ( _      |__) |__) /  \\  / _  |__)   /\\  |\\/|  /\\  |  \\ /  \\ |__) |_  (_  ")
        print(
            "                    \\/  |__ \\__/  __)     |    | \\  \\__/  \\__) |  \\  /--\\ |  | /--\\ |__//\\__/ |  \\ |__ __) ")
        print(
            "                    /                                                                                     ")
        print("")
        print("                                                               [N]")
        print("                                                [G]      [J][U][A][N] ")
        print("                                             [P][A][B][L][O]   [T] ")
        print("                                                [B]      [R]    ")
        print("                                                [R]      [G] ")
        print("                                                [I]   [D][E][N][I][S][E]   ")
        print("                                          [A][N][G][E][L]         [E] ")
        print("                                                [L]               [B]  ")
        print("                                                               [M][A][T][I]")
        print("                                                                  [S]   ")
        print("")
        print("")

