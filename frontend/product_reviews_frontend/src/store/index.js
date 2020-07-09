import Vue from 'vue'
import Vuex from 'vuex'

import productdata from './modules/productdata'
import userdata from './modules/userdata'
import productreview from './modules/productreview'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		productdata,
		userdata,
		productreview
	},
})
