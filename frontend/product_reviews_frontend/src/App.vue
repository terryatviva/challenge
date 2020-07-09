<template>
  <div id="app">
	<router-view></router-view>
  </div>
</template>
<script>
import { mapState } from 'vuex';
export default {
	data() {
		return {
    	msg: 'App',
		};
	},
	data() {
		return {
			base: 'I am a Base Component',
			validateUser: false
		};
	},
	methods: {
	}
};
</script>
<style>
</style>
