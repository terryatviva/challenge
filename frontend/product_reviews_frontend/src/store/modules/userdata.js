import { API } from '@/api';

const state = {	
	userdata: {},
};
const mutations = {
	getAllUserData(state, data) {
		state.userdata = data.results;
	}
};
const actions = {
	async getAllUsersList(context) {
		let { data } = await API.UserData.getUserList();
		context.commit('getAllUserData', data);	
	},
};


export default {
	namespaced: true,
	state,
	mutations,
	actions
}
