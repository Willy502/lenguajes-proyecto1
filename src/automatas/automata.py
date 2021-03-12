class Automata:

    def read_file(self, file_to_read):
        with open(file_to_read, 'r') as file:
            data = file.read()
            
            state = 0
            line = 1
            column = 0
            column_tk = 0
            for i in range(len(data)):

                if state == 0:
                    ## Caracteres individuales aceptados por el lenguaje
                    ## Lectura plana hasta encontrar otros estados

                    if ord(data[i]) == 10:
                        line += 1 ## Nueva línea
                        column = 0 ## Reiniciamos la columna
                        column_tk = 0

                    elif ord(data[i]) == 91:
                        ## [
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 93:
                        ## ]
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 58:
                        ## :
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 59:
                        ## ;
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 61:
                        ## =
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 44:
                        ## ,
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 37:
                        ## %
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 32:
                        ## whitespace
                        column += 1
                        column_tk += 1

                    elif ord(data[i]) == 39:
                        ## '
                        column += 1
                        state = 1

                    elif (ord(data[i]) >= 97 and ord(data[i]) <= 122) or ord(data[i]) == 241:
                        ## a-z ñ included
                        column += 1
                        state = 3

                    elif ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## 0-9
                        column += 1
                        state = 4

                    else:
                        ## estado de error
                        column += 1

                elif state == 1:
                    ## CADENA

                    if ord(data[i]) == 39:
                        ## '
                        column += 1
                        state = 2
                    
                    elif ord(data[i]) == 10:
                        ## Salto de línea
                        column = 0
                        line += 1

                    else:
                        ## CUALQUIER CARACTER
                        column += 1

                elif state == 2:
                    ## ESTADO DE ACEPTACIÓN DE LA CADENA
                    state = 0
                    column += 1
                    column_tk = column

                elif state == 3:
                    ## IDENTIFICADOR Y ESTADO DE ACEPTACIÓN DEL IDENTIFICADOR

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1

                    elif (ord(data[i]) >= 97 and ord(data[i]) <= 122) or ord(data[i]) == 241:
                        ## a-z ñ included
                        column += 1

                    elif ord(data[i]) == 95:
                        ## _
                        column += 1

                    elif ord(data[i]) == 32:
                        ## CAMBIO DE ESTADO CON ESPACIO
                        state = 0
                        column += 1
                        column_tk = column

                    elif ord(data[i]) == 10:
                        ## CAMBIO DE ESTADO Y SALTO DE LÍNEA
                        state = 0
                        line += 1
                        column = 0
                        column_tk = column

                    elif ord(data[i]) == 61:
                        ## CAMBIO DE ESTADO CON =
                        column += 1
                        column_tk = column
                        state = 0

                    elif ord(data[i]) == 59:
                        ## CAMBIO DE ESTADO CON ;
                        column += 1
                        column_tk = column
                        state = 0

                    elif ord(data[i]) == 58:
                        ## CAMBIO DE ESTADO CON :
                        column += 1
                        column_tk = column
                        state = 0

                    elif ord(data[i]) == 44:
                        ## CAMBIO DE ESTADO CON ,
                        column += 1
                        column_tk = column
                        state = 0  

                    else:
                        ## ESTADO DE ERROR
                        column += 1
                        column_tk = column

                elif state == 4:
                    ## DIGITO

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1

                    elif ord(data[i]) == 46:
                        ## .
                        column += 1
                        state = 5

                    elif ord(data[i]) == 32:
                        ## CAMBIO DE ESTADO CON ESPACIO
                        state = 0
                        column += 1
                        column_tk = column

                    elif ord(data[i]) == 10:
                        ## CAMBIO DE ESTADO Y SALTO DE LÍNEA
                        state = 0
                        line += 1
                        column = 0
                        column_tk = column

                    elif ord(data[i]) == 59:
                        ## CAMBIO DE ESTADO CON ;
                        column += 1
                        state = 0
                        column_tk = column

                    elif ord(data[i]) == 58:
                        ## CAMBIO DE ESTADO CON :
                        column += 1
                        state = 0
                        column_tk = column

                    elif ord(data[i]) == 44:
                        ## CAMBIO DE ESTADO CON ,
                        column += 1
                        state = 0
                        column_tk = column

                    elif ord(data[i]) == 37:
                        ## CAMBIO DE ESTADO CON %
                        column += 1
                        state = 0
                        column_tk = column

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                elif state == 5:
                    ## .

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        state = 6

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                elif state == 6:

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1

                    elif ord(data[i]) == 32:
                        ## CAMBIO DE ESTADO CON ESPACIO
                        state = 0
                        column += 1
                        column_tk = column

                    elif ord(data[i]) == 10:
                        ## CAMBIO DE ESTADO Y SALTO DE LÍNEA
                        state = 0
                        line += 1
                        column = 0
                        column_tk = column

                    elif ord(data[i]) == 59:
                        ## CAMBIO DE ESTADO CON ;
                        column += 1
                        state = 0
                        column_tk = column

                    elif ord(data[i]) == 58:
                        ## CAMBIO DE ESTADO CON :
                        column += 1
                        state = 0
                        column_tk = column

                    elif ord(data[i]) == 44:
                        ## CAMBIO DE ESTADO CON ,
                        column += 1
                        state = 0
                        column_tk = column

                    elif ord(data[i]) == 37:
                        ## CAMBIO DE ESTADO CON %
                        column += 1
                        state = 0
                        column_tk = column

                    else:
                        ## ESTADO DE ERROR
                        column += 1
                        column_tk = column

                else:
                    ## ESTADO DE ERROR
                    column += 1
                    column_tk += 1

                i += 1
