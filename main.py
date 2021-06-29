# to comment blocks ctrl + /
# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_table
from dash.dependencies import Input, Output, State

df = pd.read_csv(r"C:\Users\Javier\Documents\Pycharmtxt\cer.txt")

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H1(
        children='80 Cereal Brands',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
        dcc.Input(
            id='adding-rows-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}

        ),
        html.Button('Add Column', id='adding-rows-button', n_clicks=0)
    ], style={'height': 50}),

    html.Div([
        dcc.Input(
            id='editing-row-name',
            placeholder='Enter a row name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Row', id='editing-row-button', n_clicks=0)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        page_current=0,
        page_size=10,
    ),
    html.Div(id='datatable-interactivity-container')
])

#Not working
# @app.callback(
#     [Output('editing-columns', 'columns')],
#     [Input('editing-columns-button', 'n_clicks')],
#     [State('editing-columns-name', 'value'),
#     State('editing-columns', 'columns')])
# def update_columns(n_clicks, value, existing_columns):
#     if n_clicks > 0:
#         existing_columns.append({
#             'id': value, 'name': value,
#             'renamable': True, 'deletable': True
#         })
#     return existing_columns
# def display_output(rows, columns):
#     return {
#         'data': [{
#             'type': 'heatmap',
#             'z': [[row.get(c['id'], None) for c in columns] for row in rows],
#             'x': [c['name'] for c in columns]
#         }]
#     }


# @app.callback(
#     [Output('editing-columns', 'columns')],
#     [Input('editing-columns-button', 'n_clicks')],
#     [State('editing-columns-name', 'value'),
#      State('editing-columns', 'columns')])
# def display_output(rows, columns):
#     return {
#         'data': [{
#             'type': 'heatmap',
#             'z': [[row.get(c['id'], None) for c in columns] for row in rows],
#             'x': [c['name'] for c in columns]
#         }]
#     }


if __name__ == '__main__':
    app.run_server(debug=True)
