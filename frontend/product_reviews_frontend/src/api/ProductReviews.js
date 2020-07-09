import APIFetch from '@/helpers/APIFetch';

const endpoint = '/api/productreviews/';

export class ProductReviews {
	static getProductReview() {
		  return APIFetch.get(`${endpoint}`);
    }
    static readProductReviewId(id) {
		  return APIFetch.get(`${endpoint}${id}/`);
    }
    static createProductReview(data) {
		return APIFetch.post(`${endpoint}`, data);
	}
	static updateProductReview(id, data) {
		return APIFetch.put(`${endpoint}${id}/`, data);
	}
	static deleteProductReview(id) {
		return APIFetch.delete(`${endpoint}${id}/`);
	}
}
