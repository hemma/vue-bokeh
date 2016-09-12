## Simple wrapper for embedding Bokehplot in a vue-component.

### Installation
npm i vue-bokeh --save-dev

Include:
```html
<link href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.2.min.css" rel="stylesheet" type="text/css">
<script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.2.min.js"></script>
```

Might be easier to just copy the code from BokehPlot.vue.
Its very small and then you will have one less dependency.

### Usage

```javascript
<template>
  <bokeh-plot :plot="plot"></bokeh-plot>
</template>

<script>
import { fetchPlot } from '../vuex/actions'
import BokehPlot from './BokehPlot'

export default {
  components: {
    'bokeh-plot': BokehPlot
  },
  vuex: {
    getters: {
      plot: ({ plot }) => plot
    },
    actions: {
      fetchPlot
    }
  },
  ready () {
    this.fetchPlot()
  }
}
</script>

<style>
  
</style>
```

```python
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
```