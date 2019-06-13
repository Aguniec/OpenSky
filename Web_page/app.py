from flask import Flask

from Web_page import data_from_api

from bokeh.plotting import figure, output_file, show, ColumnDataSource
import pandas

app = Flask(__name__)


@app.route("/")
def plot():
    data = data_from_api.Flights()
    flight_frequency_dict = data.make_flight_frequency_dict()
    data_string = pandas.DataFrame(flight_frequency_dict)

    source = ColumnDataSource(data_string)
    country = flight_frequency_dict.keys()
    times = flight_frequency_dict.values()

    output_file("index.html")

    p = figure(plot_width=400, plot_height=400)
    p.vbar(x=data_string, width=0.5, bottom=0,
           color="firebrick", source=source)

    show(p)
