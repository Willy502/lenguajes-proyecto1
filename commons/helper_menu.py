import webbrowser
import os
from src.models.menu import *
from src.models.menu_item import *
from src.models.analisis_item import *
from src.proyecto_singleton import *
from decimal import Decimal

class HelperMenu:

    def analize_items(self, items, maxim):
        menu = Menu()
        menu.set_name(self.get_menu_name(items))
        menu.set_item(self.get_menu_options(items))
        ProyectoSingleton().menu = menu
        self.build_html(menu, maxim)

    def get_menu_name(self, items):
        i = 0
        menu_name = ""
        while i < len(items):
            item = items[i]
            
            try:
                if item.get_token() == "tk_restaurant":
                    if items[i + 1].get_token() == "tk_asign":
                        if items[i + 2].get_token() == "tk_string":
                            menu_name = items[i + 2].get_lexema()
                            
            except Exception as e:
                if menu_name != "":
                    break
            i += 1

        return menu_name

    def get_menu_options(self, items):
        i = 0
        items_dict = {}
        item_name = ""
        while i < len(items):
            
            try:
                if items[i].get_token() == "tk_dp":
                    if items[i - 1].get_token() == "tk_string":
                        item_name = items[i - 1].get_lexema()
                        items_dict[item_name] = []
            
                elif items[i].get_token() == "tk_corC":
                    if items[i - 1].get_token() == "tk_string":
                        if items[i - 2].get_token() == "tk_pc":
                            if items[i - 3].get_token() == "tk_num":
                                if items[i - 4].get_token() == "tk_pc":
                                    if items[i - 5].get_token() == "tk_string":
                                        if items[i - 6].get_token() == "tk_pc":
                                            if items[i - 7].get_token() == "tk_id":
                                                if items[i - 8].get_token() == "tk_corA":
                                                    if item_name != "":
                                                        m_item = MenuItem()
                                                        m_item.set_item_id(items[i-7].get_lexema())
                                                        m_item.set_name(items[i-5].get_lexema())
                                                        m_item.set_price(items[i-3].get_lexema())
                                                        m_item.set_description(items[i-1].get_lexema())
                                                        items_dict[item_name].append(m_item)
            except Exception as e:
                i += 1
                continue

            i += 1
        return items_dict

    def build_html(self, data, maxim):
        generated = False

        m_name = data.get_name()

        item = ''''''
        for key, values in data.get_items().items():
            item += '''
            <div class="container">
            <h2>''' + key.strip("'") + '''</h2>'''
            for value in values:
                if maxim == -1:
                    item += '''<div class="container">
                                <h4 class="ml-5">''' + value.get_name().strip("'") + ''' - Q''' + str(round(Decimal(value.get_price()), 2)) + '''</h4>
                                <p class="ml-5">''' + value.get_description().strip("'") + '''</p>
                            </div>'''
                elif round(Decimal(value.get_price()), 2) <= Decimal(maxim):
                    item += '''<div class="container">
                                <h4 class="ml-5">''' + value.get_name().strip("'") + ''' - Q''' + str(round(Decimal(value.get_price()), 2)) + '''</h4>
                                <p class="ml-5">''' + value.get_description().strip("'") + '''</p>
                            </div>'''
            item += '''</div>'''

        html = '''<!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                <title>Menu</title>
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
                        <div class="mt-5 pb-5 bg-c rounded border border-success offset-3 col-6">
                            <div class="d-flex justify-content-center">
                                <h1 class="mt-5 mb-5">''' + m_name.strip("'") + '''</h1>
                            </div>
                            ''' + item + '''
                        </div>
                        
                    </div>
                </div>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
            </body>
            </html>'''

        file = open('menu.html', 'w')
        file.write(html)
        file.close()
        filename = 'file://' + os.path.realpath(file.name)
        webbrowser.open_new_tab(filename)
        generated = True
        return generated
