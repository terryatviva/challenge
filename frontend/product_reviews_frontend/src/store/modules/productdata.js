import { API } from '@/api';

const state = {	
	productsData: {},
};
const mutations = {
	getAllProductData(state, data) {
		state.productsData = data.results;
	}
};
const actions = {
	async getAllProductsList(context) {
		let { data } = await API.ProductsData.getProductData();
		context.commit('getAllProductData', data);	
	},
};


export default {
	namespaced: true,
	state,
	mutations,
	actions
}
