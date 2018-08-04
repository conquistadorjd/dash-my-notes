import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

import numpy as np
trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])
trace2 = go.Heatmap(z=[[10, 10, 10, 10, 50], [10, 10, 10, 10, 50], [10, 10, 10, 10, 50]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [ trace              
            ],
            # 'layout': go.Layout(
            #     xaxis={'title': 'This is random data'},
            #     yaxis={'title': 'This is random data'},
            #     margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            #     legend={'x': 0, 'y': 1},
            #     hovermode='closest'
            # )            
        }
    ),
    dcc.Graph(
        id='life-exp-vs-gdp2',
        figure={
            'data': [ trace2              
            ],
            # 'layout': go.Layout(
            #     xaxis={'title': 'This is random data'},
            #     yaxis={'title': 'This is random data'},
            #     margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            #     legend={'x': 0, 'y': 1},
            #     hovermode='closest'
            # )            
        }
    )    
])

if __name__ == '__main__':
    app.run_server()