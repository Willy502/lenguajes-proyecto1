class AnalisisItem:

    def __init__(self, lexema, fila, columna, token):
        self.__lexema = lexema
        self.__fila = fila
        self.__columna = columna
        self.__token = token

    def set_lexema(self, lexema):
        self.__lexema = lexema

    def get_lexema(self):
        return self.__lexema

    def set_fila(self, fila):
        self.__fila = fila

    def get_fila(self):
        return self.__fila

    def set_columna(self, columna):
        self.__columna = columna

    def get_columna(self):
        return self.__columna

    def set_token(self, token):
        self.__token = token

    def get_token(self):
        return self.__token
