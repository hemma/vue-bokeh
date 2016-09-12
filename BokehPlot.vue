<template>
  {{{plot.div}}}
  <script>
    {{{plot.script}}}
  </script>
</template>

<script>

export default {
  props: {
    plot: Object
  },
  ready () {
    eval(this.plot.script)
  }
}
</script>
