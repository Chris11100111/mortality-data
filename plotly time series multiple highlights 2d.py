import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div(["Hello World"])

# Explicitly define the server to help Gunicorn recognize it
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
