import webbrowser
import os
from src.models.menu import *
from src.models.menu_item import *
from src.models.analisis_item import *
from src.proyecto_singleton import *
from src.models.orden import *
from src.models.orden_item import *
from decimal import Decimal

class HelperOrden:

    def analize_items(self, items):
        menu = ProyectoSingleton().menu
        orden = self.get_client_data(items)
        items = self.get_orden_items(items)
        orden.set_item(items)
        self.build_html(menu, orden)

    def get_client_data(self, items):
        i = 0
        my_orden = Orden()
        while i < len(items):

            try:
                if items[i].get_token() == "tk_string":
                    if items[i + 1].get_token() == "tk_coma":
                        if items[i + 2].get_token() == "tk_string":
                            if items[i + 3].get_token() == "tk_coma":
                                if items[i + 4].get_token() == "tk_string":
                                    if items[i + 5].get_token() == "tk_coma":
                                        if items[i + 6].get_token() == "tk_num":
                                            if items[i + 7].get_token() == "tk_porc":
                                                my_orden.set_name(items[i].get_lexema())
                                                my_orden.set_nit(items[i + 2].get_lexema())
                                                my_orden.set_address(items[i + 4].get_lexema())
                                                my_orden.set_tip(items[i + 6].get_lexema())
                                                break
            except Exception as e:
                i += 1
                continue

            i += 1
        return my_orden

    def get_orden_items(self, items):
        i = 0
        item_array = []
        while i < len(items):

            try:
                if items[i].get_token() == "tk_num":
                    if items[i + 1].get_token() == "tk_coma":
                        if items[i + 2].get_token() == "tk_id":
                            orden_item = OrdenItem()
                            orden_item.set_quantity(items[i].get_lexema())
                            orden_item.set_item_id(items[i + 2].get_lexema())
                            item_array.append(orden_item)
            except Exception as e:
                i += 1
                continue

            i += 1
        return item_array


    def build_html(self, data_menu, data_orden):
        generated = False
        id_missing = False
        m_name = data_menu.get_name()
        subtotal = Decimal()
        items = ''''''
        for item in data_orden.get_items():
            id_missing = True
            for key, values in data_menu.get_items().items():
                for value in values:
                    if item.get_item_id() == value.get_item_id():
                        id_missing = False
                        subtotal += Decimal(item.get_quantity())*round(Decimal(value.get_price()), 2)
                        items += '''
                        <tr>
                            <td>''' + str(item.get_quantity()) + '''</td>
                            <td>''' + str(item.get_item_id()) + '''</td>
                            <td>Q''' + str(round(Decimal(value.get_price()), 2)) + '''</td>
                            <td>Q''' + str(Decimal(item.get_quantity())*round(Decimal(value.get_price()), 2)) + '''</td>
                        </tr>
                        '''

        html = '''<!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                        <title>Factura</title>
                        <style>
                            .bg-c {
                                background-color: #fff;
                            }
                            body {
                                background-color: #303E73;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="row">
                            <div class="container">
                                <div class="mt-5 pb-5 bg-c rounded border border-success offset-4 col-4">
                                    <div class="d-flex justify-content-center">
                                        <h1 class="mt-5 mb-5">''' + m_name.strip("'") + '''</h1>
                                    </div>
                                                
                                    <div class="container">
                                        <h2>Datos del cliente</h2>
                                        <h4 class="ml-5">Nombre: ''' + data_orden.get_name().strip("'") + '''</h4>
                                        <h4 class="ml-5">Nit: ''' + data_orden.get_nit().strip("'") + '''</h4>
                                        <h4 class="ml-5">Dirección: ''' + data_orden.get_address().strip("'") + '''</h4>
                                        <br>
                                        <h4 class="ml-5">Descripción</h4>
                                        <table class="table">
                                            <thead>
                                            <tr>
                                                <th scope="col">Cantidad</th>
                                                <th scope="col">Concepto</th>
                                                <th scope="col">Precio</th>
                                                <th scope="col">Total</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            ''' + items + '''
                                            </tbody>
                                        </table>
                                        <div class="row">
                                            <div class="col-6">
                                                <p>Sub total</p>
                                            </div>
                                            <div class="col-6 d-flex justify-content-end">
                                                <p>Q''' + str(subtotal) + '''</p>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col-6">
                                                <p>Propina</p>
                                            </div>
                                            <div class="col-6 d-flex justify-content-end">
                                                <p>''' + str(round(Decimal(data_orden.get_tip()), 2)) + '''%</p>
                                            </div>
                                        </div>
                                        <hr>
                                        <div class="row">
                                            <div class="col-6">
                                                <strong>Total</strong>
                                            </div>
                                            <div class="col-6 d-flex justify-content-end">
                                                <strong>Q''' + str(subtotal + (subtotal*round(Decimal(data_orden.get_tip())/100, 2))) + '''</strong>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                            
                            </div>
                        </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                    </body>
                    </html>'''
        if id_missing:
            print("")
            print("Uno o más ids no han sido encontrados")
            return False
        else:
            file = open('factura.html', 'w')
            file.write(html)
            file.close()
            filename = 'file://' + os.path.realpath(file.name)
            webbrowser.open_new_tab(filename)
            generated = True
            return generated
