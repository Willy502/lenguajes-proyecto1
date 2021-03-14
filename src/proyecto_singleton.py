class ProyectoSingleton(object):

    __instance = None
    menu_file = None
    orden_file = None
    menu = None

    def __new__(cls):
        if ProyectoSingleton.__instance is None:
            ProyectoSingleton.__instance = object.__new__(cls)
        return ProyectoSingleton.__instance