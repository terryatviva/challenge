<template>
  <div id="app">
    <top-nav-bar/>
    <router-view/>
  </div>
</template>

<script>
import TopNavBar from './components/TopNavBar.vue'

export default {
  name: "App",
  components: {
    TopNavBar
  }
}
</script>
