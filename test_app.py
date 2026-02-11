import dash
from dash_app import app

def test_001_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1")

def test_002_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-graph")

def test_003_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-select")