from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import csv

app = Dash()
sales = []
dates = []
regions = []

# Load data
df = pd.read_csv("processed_data.csv")

# Setup visuals.
fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children="Pink Morsel sales over time", style={
        "textAlign": "center",
    }),
    html.Div(children=[
        dcc.Graph(id="sales-graph", figure=fig, style={
            "flex-grow": "1",
        }),
        html.Div(children=[
            html.H2("Region"),
            dcc.RadioItems(["all", "north", "east", "south", "west"], id="region-select", value="all")
        ], style={
            "flex-grow": "1",
        })
    ], style={
        "display": "flex",
        "justify-content": "center",
        "flex-wrap": "wrap",
        "min-height": "50vh"
    }),
], style={
    "font-family": "sans-serif",
})

@callback(
    Output(component_id="sales-graph", component_property="figure"),
    Input(component_id="region-select", component_property="value")
)
def update_visuals(selected_region):
    if selected_region != "all":
        filtered_df = df[df.region == selected_region]
    else:
        filtered_df = df
    
    fig = px.line(filtered_df, x="date", y="sales")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == "__main__":
    app.run(debug=True)