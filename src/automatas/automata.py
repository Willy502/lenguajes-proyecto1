class Automata:

    def read_file(self, file_to_read):

        charcodes = [39, 91, 93, 58, 59, 61, 44, 37, 46, 95]
        charcodes_main = [91, 93, 58, 59, 61, 44, 37]
        charcodes_after_string = [93, 58, 59, 44]
        charcodes_after_id = [61, 59, 58, 44]
        charcodes_after_digit = [59, 58, 44, 37]

        with open(file_to_read, 'r') as file:
            data = file.read()
            
            state = 0
            line = 1
            column = 0
            column_tk = 0
            temp = ""
            for char in data:

                if state == 0:
                    ## Caracteres individuales aceptados por el lenguaje
                    ## Lectura plana hasta encontrar otros estados

                    if ord(char) == 10:
                        line += 1 ## Nueva línea
                        column = 0 ## Reiniciamos la columna
                        column_tk = 0

                    elif ord(char) in charcodes_main:
                        column += 1
                        column_tk = column - 1
                        temp = char
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

                    elif ord(char) == 32:
                        ## whitespace
                        column += 1
                        column_tk = column - 1

                    elif ord(char) == 39:
                        ## '
                        column += 1
                        column_tk = column - 1
                        state = 1
                        temp = char

                    elif (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 241:
                        ## a-z ñ included
                        column += 1
                        column_tk = column - 1
                        state = 3
                        temp = char

                    elif ord(char) >= 48 and ord(char) <= 57:
                        ## 0-9
                        column += 1
                        column_tk = column - 1
                        state = 4
                        temp = char

                    else:
                        ## estado de error
                        state = 0
                        column += 1

                elif state == 1:
                    ## CADENA

                    if ord(char) == 39:
                        ## '
                        column += 1
                        state = 2
                        temp += char
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                    
                    elif ord(char) == 10:
                        ## Salto de línea
                        column = 0
                        line += 1
                        temp += char

                    else:
                        ## CUALQUIER CARACTER
                        column += 1
                        temp += char

                elif state == 2:
                    ## ESTADO DE ACEPTACIÓN DE LA CADENA

                    if ord(char) == 10:
                        ## Salto de línea
                        state = 0
                        column = 0
                        line += 1

                    elif ord(char) == 32:
                        ## whitespace
                        state = 0
                        column += 1
                        column_tk = column - 1

                    elif ord(char) in charcodes_after_string:
                        state = 0
                        column += 1
                        column_tk = column - 1
                        temp = char
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                elif state == 3:
                    ## IDENTIFICADOR Y ESTADO DE ACEPTACIÓN DEL IDENTIFICADOR

                    if ord(char) >= 48 and ord(char) <= 57:
                        ## DIGITO
                        column += 1
                        temp += char

                    elif (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 241:
                        ## a-z ñ included
                        column += 1
                        temp += char

                    elif ord(char) == 95:
                        ## _
                        column += 1
                        temp += char

                    elif ord(char) == 32:
                        ## CAMBIO DE ESTADO CON ESPACIO
                        state = 0
                        column += 1
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column

                    elif ord(char) == 10:
                        ## CAMBIO DE ESTADO Y SALTO DE LÍNEA
                        state = 0
                        line += 1
                        column = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column

                    elif ord(char) in charcodes_after_id:
                        column += 1
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column - 1
                        temp = char
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        state = 0

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                elif state == 4:
                    ## DIGITO

                    if ord(char) >= 48 and ord(char) <= 57:
                        ## DIGITO
                        column += 1
                        temp += char

                    elif ord(char) == 46:
                        ## .
                        column += 1
                        state = 5
                        temp += char

                    elif ord(char) == 32:
                        ## CAMBIO DE ESTADO CON ESPACIO
                        state = 0
                        column += 1
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column

                    elif ord(char) == 10:
                        ## CAMBIO DE ESTADO Y SALTO DE LÍNEA
                        state = 0
                        line += 1
                        column = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column

                    elif ord(char) in charcodes_after_digit:
                        column += 1
                        state = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column - 1
                        temp = char
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                elif state == 5:
                    ## .

                    if ord(char) >= 48 and ord(char) <= 57:
                        ## DIGITO
                        column += 1
                        state = 6
                        temp += char

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                elif state == 6:

                    if ord(char) >= 48 and ord(char) <= 57:
                        ## DIGITO
                        column += 1
                        temp += char

                    elif ord(char) == 32:
                        ## CAMBIO DE ESTADO CON ESPACIO
                        state = 0
                        column += 1
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column

                    elif ord(char) == 10:
                        ## CAMBIO DE ESTADO Y SALTO DE LÍNEA
                        state = 0
                        line += 1
                        column = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column

                    elif ord(char) in charcodes_after_digit:
                        column += 1
                        state = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        column_tk = column - 1
                        temp = char
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column

                else:
                    ## ESTADO DE ERROR
                    state = 0
                    column += 1
                    column_tk = column - 1
