<template>
	<div>
		<div>
			<navigation></navigation>
			<router-view></router-view>
		</div>
	</div>
</template>
<script>
import Navigation from './Navigation';
import { mapState } from 'vuex';
import { API } from '@/api';
export default {
	components: {
    	Navigation
	},
	data() {
		return {
			msg: 'I am a Base Component',
		};
	},
	async created() {
		await API.ProductsData.getProductData().then(res => {
			this.$store.dispatch('productdata/getAllProductsList')
			this.$Notice.success({
				title: 'Products List',
				desc: "Products data Loaded Successfully."
			});
			this.$router.push('/productsdata').catch(e => {})
		}).catch(err => {
			console.log(err)
			this.$Notice.error({
				title: 'Products List',
				desc: "Products data Initiation Failed."
			});
		})
	},
	methods: {
	}
};
</script>
<style lang="stylus" scoped>
</style>
