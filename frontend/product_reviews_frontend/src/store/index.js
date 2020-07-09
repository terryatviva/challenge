import Vue from 'vue'
import Vuex from 'vuex'

import productdata from './modules/productdata'
import userdata from './modules/userdata'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		productdata,
		userdata
	},
})
