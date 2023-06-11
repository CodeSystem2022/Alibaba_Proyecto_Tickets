def menu(vendidas, novendidas):
    opcion = ""
    salir = False
    while not salir:
        disenio_menu()
        print("")
        opcion = input("                                        Elija una opción:")
        print("")
        if opcion == "1":
            print("")  # No hay forma directa de borrar la consola en Python
            # Se invoca a la función mostrar_vendidas y se muestra la matriz con las entradas vendidas
            mostrar_vendidas(vendidas)
            # Se invoca a la función de registro y se realiza el checking de entradas
            registro(vendidas, novendidas)
        if opcion == "2":
            # Se invoca a la función de ventas
            ventas(novendidas, vendidas)
        if opcion == "3":
            print("                                        3.- Salir.")
            salir = True
            mensaje_salida()

def disenio_menu():
    # Implementa el diseño del menú aquí
    pass

def mostrar_vendidas(vendidas):
    # Implementa la lógica para mostrar las entradas vendidas aquí
    pass

def registro(vendidas, novendidas):
    # Implementa la lógica para el registro de entradas aquí
    pass

def ventas(novendidas, vendidas):
    # Implementa la lógica para las ventas aquí
    pass

def mensaje_salida():
    # Implementa el mensaje de salida aquí
    pass
