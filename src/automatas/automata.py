class Automata:

    def read_file(self, file_to_read):

        charcodes = [39, 91, 93, 58, 59, 61, 44, 37, 46, 95]
        charcodes_main = [91, 93, 58, 59, 61, 44, 37]
        charcodes_continue = [39, 91, 93, 58, 59, 61, 44, 37, 10, 32]

        with open(file_to_read, 'r') as file:
            data = file.read()
            
            state = 0
            line = 1
            column = 0
            column_tk = 0
            temp = ""
            i = 0

            while i < len(data):

                if state == 0:
                    ## Caracteres individuales aceptados por el lenguaje
                    ## Lectura plana hasta encontrar otros estados

                    if ord(data[i]) == 10:
                        line += 1 ## Nueva línea
                        column = 0 ## Reiniciamos la columna
                        column_tk = 0
                        i += 1

                    elif ord(data[i]) in charcodes_main:
                        column += 1
                        column_tk = column - 1
                        temp = data[i]
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        i += 1

                    elif ord(data[i]) == 32:
                        ## whitespace
                        column += 1
                        column_tk = column - 1
                        i += 1

                    elif ord(data[i]) == 39:
                        ## '
                        column += 1
                        column_tk = column - 1
                        state = 1
                        temp = data[i]
                        i += 1

                    elif (ord(data[i]) >= 97 and ord(data[i]) <= 122) or ord(data[i]) == 241:
                        ## a-z ñ included
                        column += 1
                        column_tk = column - 1
                        state = 3
                        temp = data[i]
                        i += 1

                    elif ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## 0-9
                        column += 1
                        column_tk = column - 1
                        state = 4
                        temp = data[i]
                        i += 1

                    else:
                        ## estado de error
                        state = 0
                        column += 1
                        i += 1

                elif state == 1:
                    ## CADENA

                    if ord(data[i]) == 39:
                        ## '
                        column += 1
                        state = 2
                        temp += data[i]
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))
                        i += 1
                    
                    elif ord(data[i]) == 10:
                        ## ESTADO DE ERROR POR SALTO DE LÍNEA
                        state = 0
                        column = 0
                        line += 1
                        i += 1

                    else:
                        ## CUALQUIER CARACTER
                        column += 1
                        temp += data[i]
                        i += 1

                elif state == 2:
                    ## ESTADO DE ACEPTACIÓN DE LA CADENA
                    state = 0

                elif state == 3:
                    ## IDENTIFICADOR Y ESTADO DE ACEPTACIÓN DEL IDENTIFICADOR

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        temp += data[i]
                        i += 1

                    elif (ord(data[i]) >= 97 and ord(data[i]) <= 122) or ord(data[i]) == 241:
                        ## a-z ñ included
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
                        print(temp + ": " + str(ord(data[i])))
                        state = 0
                        column += 1
                        column_tk = column
                        i += 1

                    else:
                        ## CAMBIO DE ESTADO POR DELIMITADOR ACEPTADO
                        state = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

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
                        state = 0
                        column += 1
                        column_tk = column
                        i += 1

                    else:
                        ## CAMBIO DE ESTADO POR DELIMITADOR ACEPTADO
                        state = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

                elif state == 5:
                    ## .

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        state = 6
                        temp += data[i]
                        i += 1

                    else:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column
                        i += 1

                elif state == 6:

                    if ord(data[i]) >= 48 and ord(data[i]) <= 57:
                        ## DIGITO
                        column += 1
                        temp += data[i]
                        i += 1

                    elif ord(data[i]) not in charcodes_continue:
                        ## ESTADO DE ERROR
                        state = 0
                        column += 1
                        column_tk = column
                        i += 1

                    else:
                        ## CAMBIO DE ESTADO POR DELIMITADOR ACEPTADO
                        state = 0
                        print(temp + " linea: " + str(line) + ", columna: " + str(column_tk))

                else:
                    ## ESTADO DE ERROR
                    state = 0
                    column += 1
                    column_tk = column - 1
                    i += 1
