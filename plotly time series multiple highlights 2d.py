import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # This line is crucial for Gunicorn to serve the app correctly

app.layout = html.Div([
    html.H1("Hello, Render!"),
])

if __name__ == "__main__":
    app.run_server(debug=True)
