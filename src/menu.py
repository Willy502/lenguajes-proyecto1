from .options import *
from .proyecto_singleton import *
from .graph import *

class Menu:

    def __init__(self):
        print("")
        print("Proyecto 1 - LFP")
        print("Lenguajes formales y de programación A+")
        print("Wilfred Alejandro Barrios Ola")
        print("201602734")
        self.create_menu()

    def create_menu(self):
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

        if option == "1": ## Read Menu File
            open_file = Options().open_file(self, "menu")
        elif option == "2": ## Read Order File
            if ProyectoSingleton().menu_file is None:
                print("Para acceder a esta opcion primero debes cargar un archivo de menu\n")
            else:
                open_file = Options().open_file(self, "orden")
        elif option == "3": # Create Menu
            self.menu_options()
        elif option == "4": # Create Bill
            if ProyectoSingleton().menu_failed != True:
                if ProyectoSingleton().menu is None:
                    print("Debes generar primero el menú para acceder a esta opción")
                else:
                    Options().read_orden()
            else:
                print("El menú presenta errores, por lo tanto no se puede generar una orden")
                
        elif option == "5": # Generate Graph
            if ProyectoSingleton().menu is None:
                print("Debes generar primero el menú para acceder a esta opción")
            else:
                Graph()
        elif option == "6": # Exit
            quit()
        else:
            print("Selecciona una opción válida\n")
        self.create_menu()

    def menu_options(self):
        print("Desea poner límite en los precios? Si/No")
        print("> ", end='')
        answer = input()
        if answer.upper() == "SI":
            print("Valor máximo?")
            print("> ", end='')
            answer2 = input()
            if answer2.isnumeric():
                Options().read_menu(answer2)
            else:
                self.menu_options()
        elif answer.upper() == "NO":
            Options().read_menu(-1)
        else:
            self.menu_options()