import { API } from '@/api';

const state = {	
	productReviewData: {},
};
const mutations = {
	getAllProductReviews(state, data) {
        state.productReviewData = data.results;
	}
};
const actions = {
	async getAllProductReviewsList(context) {
		let { data } = await API.ProductReviews.getProductReview();
		context.commit('getAllProductReviews', data);	
	},
};


export default {
	namespaced: true,
	state,
	mutations,
	actions
}
