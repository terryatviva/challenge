import { API } from '@/api';
import { mapState } from 'vuex';

export default {
	components: {
	},
	data() {
		return {
		};
	},
	async created() {
        this.getAllUsersList()
        this.getAllProductsReviewsList()
	},
	computed: {
		...mapState({
            userdata: state => state.userdata.userdata,
            productReviewData: state => state.productreview.productReviewData
		})
	},
	methods: {
        getAllUsersList() {
            this.$store.dispatch('userdata/getAllUsersList')
        },
        getAllProductsReviewsList() {
            this.$store.dispatch('productreview/getAllProductReviewsList')
        },
	}
};
