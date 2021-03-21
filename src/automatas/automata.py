from src.models.analisis_item import *
from commons.helper_report import *
from commons.helper_menu import *
from commons.helper_orden import *
from src.proyecto_singleton import *

class Automata:

    def read_file(self, file_to_read, type_file, maxim):
        palabras_reservadas = ['restaurante']
        charcodes_main = [91, 93, 58, 59, 61, 44, 37]
        charcodes_continue = [39, 91, 93, 58, 59, 61, 44, 37, 10, 32]
        message_to_report = ""
        accepted_items = []
        error_items = []
        errors = False
        menu = Menu()

        with open(file_to_read, 'r') as file:
            data = file.read()
            
            state = 0
            line = 1
            column = 1
            temp = ""
            i = 0

            while i < len(data):

                if state == 0:
                    ## CARACTERES INDIVIDUALES ACEPTADOS POR EL LENGUAJE
                    ## LECTURA PLANA HASTA ENCONTRAR OTROS ESTADOS

                    if ord(data[i]) == 10:
                        line += 1 ## NUEVA LÍNEA
                        column = 1 ## REINICIAMOS LA COLUMNA
                        i += 1

                    elif ord(data[i]) in charcodes_main:
                        temp = data[i]
                        accepted_items.append(AnalisisItem(temp, line, column, self.create_token(data[i])))
                        column += 1
                        i += 1

                    elif ord(data[i]) == 32:
                        ## WHITESPACE
                        column += 1
                        i += 1

                    elif ord(data[i]) == 39:
                        ## '
                        column += 1
                        state = 1
                        temp = data[i]
                        i += 1

                    elif (ord(data[i]) >= 97 and ord(data[i]) <= 122) or ord(data[i]) == 241:
                        ## a-z ñ INCLUÍDO
                        column += 1
                        state = 3
                        temp = data[i]
                        i += 1

                    elif ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## 0-9
                        column += 1
                        state = 4
                        temp = data[i]
                        i += 1

                    else:
                        ## ESTADO DE ERROR
                        errors = True
                        temp = data[i]
                        error_items.append(AnalisisItem(temp, line, column, "Caracter Desconocido"))
                        state = 0
                        column += 1
                        i += 1

                elif state == 1:
                    ## CADENA

                    if ord(data[i]) == 39:
                        ## '
                        temp += data[i]
                        column += 1
                        state = 2
                        i += 1
                    
                    elif ord(data[i]) == 10:
                        ## ESTADO DE ERROR POR SALTO DE LÍNEA
                        error_items.append(AnalisisItem(temp, line, column - len(temp), "Cadena no válida"))
                        errors = True
                        state = 0
                        column = 1
                        line += 1
                        i += 1

                    else:
                        ## CUALQUIER CARACTER
                        column += 1
                        temp += data[i]
                        i += 1

                elif state == 2:
                    ## ESTADO DE ACEPTACIÓN DE LA CADENA
                    accepted_items.append(AnalisisItem(temp, line, column - len(temp), "tk_string"))
                    state = 0

                elif state == 3:
                    ## IDENTIFICADOR Y ESTADO DE ACEPTACIÓN DEL IDENTIFICADOR

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        temp += data[i]
                        i += 1

                    elif (ord(data[i]) >= 97 and ord(data[i]) <= 122) or ord(data[i]) == 241:
                        ## a-z ñ INCLUÍDO
                        column += 1
                        temp += data[i]
                        i += 1

                    elif ord(data[i]) == 95:
                        ## _
                        column += 1
                        temp += data[i]
                        i += 1

                    elif ord(data[i]) not in charcodes_continue:
                        ## ESTADO DE ERROR
                        errors = True
                        temp += data[i]
                        message_to_report = "Identificador no válido"
                        state = 6
                        column += 1
                        i += 1

                    else:
                        ## CAMBIO DE ESTADO POR DELIMITADOR ACEPTADO
                        state = 0
                        if temp in palabras_reservadas:
                            accepted_items.append(AnalisisItem(temp, line, column - len(temp), "tk_restaurant"))
                        else:
                            accepted_items.append(AnalisisItem(temp, line, column - len(temp), "tk_id"))

                elif state == 4:
                    ## DIGITO

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        temp += data[i]
                        i += 1

                    elif ord(data[i]) == 46:
                        ## .
                        column += 1
                        state = 5
                        temp += data[i]
                        i += 1

                    elif ord(data[i]) not in charcodes_continue:
                        ## ESTADO DE ERROR
                        errors = True
                        temp += data[i]
                        message_to_report = "Dígito no válido"
                        state = 6
                        column += 1
                        i += 1

                    else:
                        ## CAMBIO DE ESTADO POR DELIMITADOR ACEPTADO
                        state = 0
                        accepted_items.append(AnalisisItem(temp, line, column - len(temp), "tk_num"))

                elif state == 5:
                    ## .

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        temp += data[i]
                        i += 1

                    elif ord(data[i]) not in charcodes_continue:
                        ## ESTADO DE ERROR
                        errors = True
                        temp += data[i]
                        message_to_report = "Dígito no válido"
                        state = 6
                        column += 1
                        i += 1

                    else:
                        ## CAMBIO DE ESTADO POR DELIMITADOR ACEPTADO
                        state = 0
                        accepted_items.append(AnalisisItem(temp, line, column - len(temp), "tk_num"))

                elif state == 6:
                    if ord(data[i]) not in charcodes_continue:
                        temp += data[i]
                        i += 1
                        column += 1
                    else:
                        state = 0
                        error_items.append(AnalisisItem(temp, line, column - len(temp), message_to_report))
            
            HelperReport().reporte_analisis_correcto(accepted_items)
            if errors:
                HelperReport().reporte_errores(error_items)
                if type_file == "menu":
                    ProyectoSingleton().menu_failed = True
            else:
                if type_file == "menu":
                    ProyectoSingleton().menu_failed = False
                    HelperMenu().analize_items(accepted_items, maxim)
                else:
                    HelperOrden().analize_items(accepted_items)

    def create_token(self, data):

        token_name = ""
        
        if ord(data) == 91:
            token_name = "tk_corA"
        elif ord(data) == 93:
            token_name = "tk_corC"
        elif ord(data) == 58:
            token_name = "tk_dp"
        elif ord(data) == 59:
            token_name = "tk_pc"
        elif ord(data) == 61:
            token_name = "tk_asign"
        elif ord(data) == 44:
            token_name = "tk_coma"
        elif ord(data) == 37:
            token_name = "tk_porc"


        return token_name

