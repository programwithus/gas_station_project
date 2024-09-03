from dash import Dash, html   # Importing required functions
import dash_bootstrap_components as dbc
from util import get_data
from components import year_dropdown
from layout import create_layout

PATH = 'gas_sale.csv'
data = get_data(PATH)
print(data)
app = Dash(external_stylesheets=[dbc.themes.LUX])
app.layout = create_layout(app,data)
app.run_server(debug=True)