'''import logging'''


class Pantallas:
    def __init__(self):
        self.intentos = 0
        self.usuario = ""
        self.contrasenia = ""
        self.validacion = False
        self.entrada = input

    def setIntentos(self, intentos):
        self.intentos = intentos

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContrasenia(self, contrasenia):
        self.contrasenia = contrasenia

    def getValidacion(self):
        self.ingresousuario()
        return self.validacion

    def titulo(self):
        print("")
        print("                                                 *=====================================*")
        print("                                                 *  E N T R A D A S   V E N D I D A S  *")
        print("                                                 *=====================================*")
        print("                             ______   _____   ______    ______    _   __    ___     ____     ____   ____ ")
        print("                            / ____/  / ___/  / ____/   / ____/   / | / /   /   |   / __\\   /  _/  / __ \\")
        print("                           / __/     \\__\\ / /       / __/     /  |/ /   / /| |  / /_/ /   / /   / / / /")
        print("                          / /___    ___/ / / /___    / /___    / /|  /   / ___ | / _, _/  _/ /   / /_/ / ")
        print("                         /_____/   /____/  \\____/   /_____/  /_/ |_/   /_/  |_|/_/ |_|  /___/  \\____/  ")
        print("           --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print("           __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print(" ||---*--- PALCO IZQUIERDO ---*---||       * RESERVADO *  " + " ||*--*--*--* ZONA   V I P *--*--*--*|| " + "  ||  ---**---   PALCO   DERECHO    ---**---  ||")
        print("")

    def ingresousuario(self):
        print("")
        print("        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print("        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print("               :::        :::        :::::::::::        :::::::::           :::        :::::::::           ::: ")
        print("             :+: :+:      :+:            :+:            :+:    :+:        :+: :+:      :+:    :+:        :+: :+:")
        print("            +:+   +:+     +:+            +:+            +:+    +:+       +:+   +:+     +:+    +:+       +:+   +:+ ")
        print("           +#++:++#++:    +#+            +#+            +#++:++#+       +#++:++#++:    +#++:++#+       +#++:++#++:")
        print("           +#+     +#+    +#+            +#+            +#+    +#+      +#+     +#+    +#+    +#+      +#+     +#+   ")
        print("           #+#     #+#    #+#            #+#            #+#    #+#      #+#     #+#    #+#    #+#      #+#     #+#   ")
        print("           ###     ###    ########## ###########        #########       ###     ###    #########       ###     ###     ")
        print("")
        print("        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print("        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print("                        |     __   __       __   __   __     __   __    __   __ __  __    __    __    __  __   __")
        print("                        |   /  \\ ( _      |__) |__) /  \\  / _  |__)   /\\  |\\/|  /\\  |  \\ /  \\ |__) |_  (_  ")
        print("                   \\/  |__ \\__/  __)     |    | \\ \\__/ \\__) | \\  /--\\ |   | /--\\ |__// \\__/ | \\ |__ __) ")
        print("                    /                                                                                     ")
        print("")
        print("")

        intentos = Pantallas.setIntentos(intentos)

        '''Este bucle nos mantiene en la pantalla principal hasta que se ingrese el usuario y contraseña correctos.'''
        while True:
            print(" Escriba un Usuario: ")
            ingUsuario = input()
            print(" Escriba una Contraseña: ")
            ingContrasenia = input()
            intentos = intentos - 1
            if ingUsuario == Pantallas.usuario and ingContrasenia == Pantallas.contrasenia:
            
                try:
                    print("")
                    print(" B I E N V E N I D O  A  S U  C A M P U S ")
                    validacion = True
                except Exception as ex:
                    print("Error: ", ex)
                else:
                    print("")
                    print(" Usuario o contraseña INCORRECTA, ¡VERIFIQUE SUS DATOS! ")
                    print("")
                    print(" Le restan " + str(intentos) + " intentos")
                    print("")
    
            if validacion or intentos == 0:
                break


    def diseniomenu():
        # limpiar.limpiarPantalla()
        print("")
        print("")
        print("")
        print("_________________________________________________________________________________________________________")
        print("     B i e n v e n i d o  a l  P r o g r a m a  d e  C h e c k i n g  y  V e n t a Ali Baba V2.0.0 ")
        print("=========================================================================================================")
        print("")
        print("")
        print("                                     Elija una de las siguientes opciones:")
        print("")
        print("                                     1.- Verificacion de tickets.")
        print("                                     2.- Venta de tickets. ")
        print("                                     3.- Salir.")


    def mensajesalida():
        print("")
        print("        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print("        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print("               :::        :::        :::::::::::        :::::::::           :::        :::::::::           ::: ")
        print("             :+: :+:      :+:            :+:            :+:    :+:        :+: :+:      :+:    :+:        :+: :+:")
        print("            +:+   +:+     +:+            +:+            +:+    +:+       +:+   +:+     +:+    +:+       +:+   +:+ ")
        print("           +#++:++#++:    +#+            +#+            +#++:++#+       +#++:++#++:    +#++:++#+       +#++:++#++:")
        print("           +#+     +#+    +#+            +#+            +#+    +#+      +#+     +#+    +#+    +#+      +#+     +#+   ")
        print("           #+#     #+#    #+#            #+#            #+#    #+#      #+#     #+#    #+#    #+#      #+#     #+#   ")
        print("           ###     ###    ########## ###########        #########       ###     ###    #########       ###     ###     ")
        print("")
        print("        --__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--")
        print("        __--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__")
        print("")
        print("                        |     __   __       __   __   __     __   __    __   __ __  __    __    __    __  __   __")
        print("                        |   /  \\ ( _      |__) |__) /  \\  / _  |__)   /\\  |\\/|  /\\  |  \\ /  \\ |__) |_  (_  ")
        print("                   \\/  |__ \\__/  __)     |    | \\ \\__/ \\__) | \\  /--\\ |   | /--\\ |__// \\__/ | \\ |__ __) ")
        print("                    /                                                                                     ")
        print("")
        print("                                                               [N]")
        print("                                                [G]      [J][U][A][N] ")
        print("                                             [P][A][B][L][O]   [T] ")
        print("                                                [B]      [R]    ")
        print("                                                [R]      [G] ")
        print("                                                [I]   [D][E][N][I][S][E]   ")
        print("                                          [A][L][E][X]            [E] ")
        print("                                          [N]   [L]               [B]  ")
        print("                                          [G]                  [M][A][T][I]")
        print("                                          [E]                     [S]   ")
        print("                                          [L]")
        print("")
        print("")
