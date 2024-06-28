import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, dash_table
from datetime import datetime
import plotly.express as px

# Load data from CSV into a DataFrame
df = pd.read_csv('m.csv')

# Convert 'year' and 'week' to datetime index
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['week'].astype(str) + '-1', format='%Y-%U-%w')

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define app layout
app.layout = html.Div([
    html.H1("Mortality Data Table and Plot", className='my-4'),

    html.Div([
        html.Label("Select Date Range:"),
        dcc.DatePickerRange(
            id='date-range-filter',
            min_date_allowed=df['date'].min(),
            max_date_allowed=df['date'].max(),
            start_date=df['date'].min(),
            end_date=df['date'].max(),
            display_format='YYYY-MM-DD',
            className='form-control bg-dark text-white'
        ),
        html.Div(id='selected-time-period', className='mt-4')
    ], className='row'),

    html.Div([
        dash_table.DataTable(
            id='mortality-table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records'),
            filter_action='native',  # Enable filtering
            sort_action='native',  # Enable sorting
            sort_mode='multi',  # Allow multiple columns to be sorted
            style_table={'overflowX': 'scroll', 'backgroundColor': 'rgb(30, 30, 30)', 'height': '70vh'},
            style_cell={
                'minWidth': '100px', 'width': '150px', 'maxWidth': '300px',
                'whiteSpace': 'normal',
                'textAlign': 'center',
                'backgroundColor': 'black',
                'color': 'white'
            },
            style_header={
                'backgroundColor': 'rgb(30, 30, 30)',
                'fontWeight': 'bold'
            }
        )
    ], className='row mt-4'),

    dcc.Graph(
        id='selected-period-graph'
    )
])

# Callback to update table and selected time period plot
@app.callback(
    Output('mortality-table', 'data'),
    Output('selected-time-period', 'children'),
    Output('selected-period-graph', 'figure'),
    Input('date-range-filter', 'start_date'),
    Input('date-range-filter', 'end_date')
)
def update_data(start_date, end_date):
    if not start_date or not end_date:
        return dash.no_update, dash.no_update, dash.no_update

    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    fig = px.scatter(x=range(10), y=range(10))  # Example figure, replace with your actual plot

    selected_period_plot = html.Div([
        html.H2(f"Selected Time Period: {start_date} to {end_date}"),
        dcc.Graph(
            id='selected-period-graph',
            figure=fig
        )
    ])

    return filtered_df.to_dict('records'), selected_period_plot, fig

# Save the dynamic plot as a standalone HTML file
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    fig.write_html("file222.html", auto_open=True)
