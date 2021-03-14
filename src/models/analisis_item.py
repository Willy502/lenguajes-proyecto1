class AnalisisItem:

    def __init__(self, lexema, fila, columna, token):
        self.__lexema = lexema
        self.__fila = fila
        self.__columna = columna
        self.__token = token

    def get_lexema(self):
        return self.__lexema

    def get_fila(self):
        return self.__fila

    def get_columna(self):
        return self.__columna

    def get_token(self):
        return self.__token
