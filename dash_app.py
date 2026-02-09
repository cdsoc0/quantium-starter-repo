import dash as d
import plotly.express as px
import pandas as pd
import csv

app = d.Dash()
sales = []
dates = []
regions = []

# Load data
with open("processed_data.csv" , 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sales.append(row["sales"])
        dates.append(row["date"])
        regions.append(row["region"])

df = pd.DataFrame({
    "Sales": sales,
    "Date": dates,
    "Region": regions
})

# Setup visuals.
fig = px.line(df, x="Date", y="Sales", color="Region")

app.layout = d.html.Div(children=[
    d.html.H1(children="Pink Morsel sales over time"),
    d.dcc.Graph(id="sales-graph", figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)