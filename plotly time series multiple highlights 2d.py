import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output, dash_table

# Create some sample data
data = {
    "Date": pd.date_range(start="2021-01-01", periods=100),
    "Value": pd.np.random.randn(100).cumsum()
}
df = pd.DataFrame(data)

# Initialize the Dash app (no external stylesheets for simplicity)
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Simple Dash App"),
    dcc.Graph(id='my-graph'),
    dash_table.DataTable(
        id='my-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_cell={'textAlign': 'left'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        }
    ),
    dcc.Slider(
        id='year-slider',
        min=df['Date'].dt.year.min(),
        max=df['Date'].dt.year.max(),
        value=df['Date'].dt.year.max(),
        marks={str(year): str(year) for year in df['Date'].dt.year.unique()},
        step=None
    )
])

# Define callback to update graph dynamically based on the slider's value
@app.callback(
    Output('my-graph', 'figure'),
    [Input('year-slider', 'value')]
)
def update_graph(selected_year):
    filtered_df = df[df['Date'].dt.year == selected_year]
    fig = px.line(filtered_df, x='Date', y='Value', title=f'Stock Prices in {selected_year}')
    return fig

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
