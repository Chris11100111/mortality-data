# app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialize the Dash app and specify the external CSS stylesheet from Dash Bootstrap Components
app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css'])
server = app.server  # This is important for deployment on Gunicorn

# Define the layout of the app
app.layout = html.Div([
    html.H1("Simple Dash App", className="text-center bg-primary text-white p-3"),
    dcc.Graph(id='graph'),
    dcc.Slider(
        id='year-slider',
        min=2010,
        max=2020,
        value=2015,
        marks={str(year): str(year) for year in range(2010, 2021)},
        step=1
    )
])

# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_year):
    # Generate a simple plot based on the slider value
    data = [dict(Year=year, Value=year*2) for year in range(2010, selected_year+1)]
    fig = px.line(data, x='Year', y='Value', title=f'Data up to the year {selected_year}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
