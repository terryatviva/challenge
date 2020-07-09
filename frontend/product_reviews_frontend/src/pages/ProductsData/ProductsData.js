import { API } from '@/api';
import { mapState } from 'vuex';
import AddProductReview from '@/components/AddProductReview/AddProductReview.vue';
export default {
	components: {
		AddProductReview
	},
	data() {
		return {
			closeInvent: false,
			reviewTypeDetail: '',
			productPropData: '',
		};
	},
	async created() {
	},
	computed: {
		...mapState({
			productsData: state => state.productdata.productsData,
		})
	},
	methods: {
		closeInventories() {
			this.closeInvent = false;
		},
	}
};