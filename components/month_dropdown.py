from dash import dcc, html, Input,Output

def render(app,data):
    all_months = data["month"].unique()
    @app.callback(
        Output("months_dropdown","value"),
        [
            Input("year_dropdown","value"),
            Input("select_all_button_months","n_clicks")
        ]
    )
    def select_all_months(years,n):
        filtered_data = data.query("year in @years")
        return sorted(filtered_data['month'].unique())
    return html.Div([
        html.H6("Month"),
        dcc.Dropdown(
            options  = [{"label":m, "value":m} for m in all_months],
            multi=True,
            id = "months_dropdown"
        ),
        html.Button(
            children = ["Select All"],
            id = "select_all_button_months",
            n_clicks=0
        )
    ])