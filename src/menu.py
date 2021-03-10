from .options import *
from .proyecto_singleton import *

class Menu:

    def __init__(self):
        self.create_menu()

    def create_menu(self):
        print("Proyecto 1 - LFP")
        print("Lenguajes formales y de programación A+")
        print("Wilfred Alejandro Barrios Ola")
        print("201602734")
        print("")
        print("1. Cargar menú")
        print("2. Cargar orden")
        print("3. Generar menú")
        print("4. Generar factura")
        print("5. Generar árbol")
        print("6. Salir")
        print("> ", end='')
        answer = input()
        print("------------------------------------\n")
        self.select_menu_option(answer)

    def select_menu_option(self, option):
        if option in ["3", "5"]:
            if ProyectoSingleton().menu_file is None:
                print("Para acceder a estas opciones primero debes cargar un archivo de menu\n")
                self.create_menu()

        if option == "4" and ProyectoSingleton().orden_file is None:
            print("Para acceder a estas opciones primero debes cargar un archivo de orden\n")
            self.create_menu()

        if option == "1":
            open_file = Options().open_file(self, "menu")
        elif option == "2":
            open_file = Options().open_file(self, "orden")
        elif option == "3":
            Options().read_menu()
        elif option == "4":
            print("option 4")
        elif option == "5":
            print("option 5")
        elif option == "6":
            quit()
        else:
            print("Selecciona una opción válida\n")
        self.create_menu()