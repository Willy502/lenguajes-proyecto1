from graphviz import Digraph
from .proyecto_singleton import *
from src.models.menu import *
from src.models.menu_item import *
from decimal import Decimal

class Graph:

    def __init__(self, max_quantity):
        self.generate_graph(max_quantity)

    def generate_graph(self, max_quantity):
        generated_menu = ProyectoSingleton().menu
        dot = Digraph(comment='Árbol de menú')

        dot.node('A', generated_menu.get_name().strip("'"))
        for key, values in generated_menu.get_items().items():
            dot.node(key.strip("'"), key.strip("'"))
            dot.edge('A', key.strip("'"))

            for value in values:
                if max_quantity != -1 and round(Decimal(value.get_price()), 2) > round(Decimal(max_quantity), 2):
                    continue
                description = value.get_name().strip("'") + " Q" + str(round(Decimal(value.get_price()), 2)) + "\n" + value.get_description().strip("'")
                dot.node(value.get_item_id(), description)
                dot.edge(key.strip("'"), value.get_item_id())

        dot.render('test-output/arbol.gv', view=True)
        print("Árbol generado exitosamente")