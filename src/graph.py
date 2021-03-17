from graphviz import Digraph
from .proyecto_singleton import *
from src.models.menu import *
from src.models.menu_item import *
from decimal import Decimal

class Graph:

    def __init__(self):
        self.generate_graph()

    def generate_graph(self):
        generated_menu = ProyectoSingleton().menu
        dot = Digraph(comment='Árbol de menú')

        dot.node('A', generated_menu.get_name().strip("'"))
        for key, values in generated_menu.get_items().items():
            dot.node(key.strip("'"), key.strip("'"))
            dot.edge('A', key.strip("'"))

            for value in values:
                description = value.get_name().strip("'") + " Q" + str(round(Decimal(value.get_price()), 2)) + "\n" + value.get_description().strip("'")

                dot.node(value.get_item_id(), description)
                dot.edge(key.strip("'"), value.get_item_id())

        dot.render('test-output/arbol.gv', view=True)