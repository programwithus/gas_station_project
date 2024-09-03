from dash import dcc,html,Input,Output

def render(app,data):
    all_years = data["year"].unique()
    options = [{'label':year, "value":year} for year in all_years]
    @app.callback(
        Output("year_dropdown","value"),
        Input("select_all_years_button", "n_clicks")
    )
    def select_all_years(n):
        return  all_years
    return html.Div([
            html.H6("Year"),
            dcc.Dropdown(
                options = options,
                multi=True,
                id = "year_dropdown" 
            ),
            html.Button(
                children=['Select All'],
                n_clicks=0,
                id="select_all_years_button"
            )
    ])