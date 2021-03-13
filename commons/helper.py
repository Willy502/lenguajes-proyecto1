import webbrowser
import os
from src.models.analisis_item import *

class Helper:

    def reporte_analisis_correcto(self, data):
        generated = False
        lines = ''
        contador = 1
        for item in data:
            lines += "<tr>"
            lines += "<th scope='row'>" + str(contador) + "</th>"
            lines += "<td scope='col'>" + str(item.get_lexema()) + "</td>"
            lines += "<td scope='col'>" + str(item.get_fila()) + "</td>"
            lines += "<td scope='col'>" + str(item.get_columna()) + "</td>"
            lines += "<td scope='col'>" + str(item.get_token()) + "</td>"
            lines += "</tr>"
            contador += 1
            

        html = '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

            <title>Resultado del análisis</title>
        </head>
        <body>

            <div class="container">
                <div class="row">
                    <br>
                    <br>
                    <h1>Resultado del análisis</h1>
                    <hr>
                    <table class="table">
                        <thead>
                            <tr>
                            <th scope="col">No.</th>
                            <th scope="col">Lexema</th>
                            <th scope="col">Fila</th>
                            <th scope="col">Columna</th>
                            <th scope="col">Token</th>
                            </tr>
                        </thead>
                        <tbody>'''
        html += lines
        html += '''
                        </tbody>
                    </table>
                </div>
            </div>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

        </body>
        </html>
        '''
        file = open('analisis.html', 'w')
        file.write(html)
        file.close()
        filename = 'file://' + os.path.realpath(file.name)
        webbrowser.open_new_tab(filename)
        generated = True
        return generated

    def reporte_errores(self, data):
        generated = False
        lines = ''
        contador = 1
        for item in data:
            lines += "<tr>"
            lines += "<th scope='row'>" + str(contador) + "</th>"
            lines += "<td scope='col'>" + str(item.get_fila()) + "</td>"
            lines += "<td scope='col'>" + str(item.get_columna()) + "</td>"
            lines += "<td scope='col'>" + str(item.get_lexema()) + "</td>"
            lines += "<td scope='col'>" + str(item.get_token()) + "</td>"
            lines += "</tr>"
            contador += 1
            

        html = '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

            <title>Errores encontrados</title>
        </head>
        <body>

            <div class="container">
                <div class="row">
                    <br>
                    <h1>Errores encontrados</h1>
                    <hr>
                    <table class="table">
                        <thead>
                            <tr>
                            <th scope="col">No.</th>
                            <th scope="col">Fila</th>
                            <th scope="col">Columna</th>
                            <th scope="col">Insidencia</th>
                            <th scope="col">Descripción</th>
                            </tr>
                        </thead>
                        <tbody>'''
        html += lines
        html += '''
                        </tbody>
                    </table>
                </div>
            </div>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

        </body>
        </html>
        '''
        file = open('errores.html', 'w')
        file.write(html)
        file.close()
        filename = 'file://' + os.path.realpath(file.name)
        webbrowser.open_new_tab(filename)
        generated = True
        return generated