import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)
random_x2 = np.random.randn(N)
random_y2 = np.random.randn(N)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x = random_x,
                    y = random_y,
                    mode = 'markers',
                   
                )                
            ],
        }
    )
])

if __name__ == '__main__':
    app.run_server()