# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    html.Div(children='''
        This is simplest "Hello World" by using Dash
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)
