<template>
  <bokeh-plot :plot="plot"></bokeh-plot>
</template>

<script>
import { fetchPlot } from '../vuex/actions'
import BokehPlot from 'vue-bokeh'

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
