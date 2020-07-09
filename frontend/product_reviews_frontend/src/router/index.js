import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes: [
		{
			path: "/",
			name: "",
			component: Home,
			children: [
				{
					path: "productsdata",
					name: "productsdata",
					component: () =>
						import(
						"../pages/ProductsData/ProductsData.vue"
						)
				},
				{
					path: "adminpanel",
					name: "adminpanel",
					component: () =>
						import(
						"../components/AdminPanel/AdminPanel.vue"
						)
				},
			]
		}
	]
});

export default router
