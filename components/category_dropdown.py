from dash import dcc,html,Input,Output
def render(app,data):
    all_cats = data["category"].unique()
    options = [{'label':category, "value":category} for category in all_cats]
    @app.callback(
        Output("category_dropdown","value"),
        [
        Input("year_dropdown", "value"),
        Input("months_dropdown", "value"),
        Input("select_all_categories_button", "n_clicks")
        ]
    )
    def select_all_categories(years, months,n):
        filtered_data = data.query("year in @years and month in @months")
        return sorted(filtered_data["category"].unique())
    return html.Div([
            html.H6("Category"),
            dcc.Dropdown(
                options = options,
                multi=True,
                id = "category_dropdown"
            ),
            html.Button(
                children=['Select All'],
                n_clicks=0,
                id="select_all_categories_button"
            )
    ])