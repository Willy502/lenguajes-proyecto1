import tkinter as tk
from tkinter import filedialog as fd
from .menu import *
from .proyecto_singleton import *

class Options:

    def open_file(self, mn, f_type):
        root = tk.Tk()
        root.withdraw()
        file = fd.askopenfilename(title='Open files', filetypes=[('text files', '*.lfp')])

        if file != "":
            if f_type == "MENU": 
                ProyectoSingleton().menu_file = file
            else:
                ProyectoSingleton().orden_file = file
            print("Archivo cargado exitosamente\n")

        else:
            print("No se ha seleccionado ningun archivo\n")
        mn.create_menu()