from flask import Flask, jsonify
from flask_cors import cross_origin
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)


@app.route("/get-plot")
@cross_origin()
def get_plot():

    plot = figure(plot_height=250, responsive = True)
    plot.circle([1, 2], [3, 4])
    script, div = components(plot, wrap_script=False)
    return jsonify({'div': div, 'script': script})

app.run(debug=True)





