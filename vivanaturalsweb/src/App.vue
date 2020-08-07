<template>
  <div id="app" class="container-fluid">
    <Feedback/>
  </div>
</template>

<script>
import Feedback from './components/Feedback.vue'

export default {
  name: 'App',
  components: {
    Feedback
  }
}
</script>

<style scoped>

#app {
	margin-top: 5px;
 	font-family: Avenir, Helvetica, Arial, sans-serif;
  	-webkit-font-smoothing: antialiased;
  	-moz-osx-font-smoothing: grayscale;
}

</style>
