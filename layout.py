from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components import (
            category_dropdown, 
            year_dropdown, 
            month_dropdown, 
            pie_chart
)

def create_layout(app,data):
    return dbc.Container([
        dbc.Row([
            dbc.Col(year_dropdown.render(app, data), width = 4),
            dbc.Col(month_dropdown.render(app,data), width = 4),
            dbc.Col(category_dropdown.render(app,data), width = 4),
            ]),
        dbc.Row([pie_chart.render(app,data)])
        ])