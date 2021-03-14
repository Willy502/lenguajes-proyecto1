from .menu_item import *

class Menu:

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_item(self, items):
        self.__items = items

    def get_items(self):
        return self.__items