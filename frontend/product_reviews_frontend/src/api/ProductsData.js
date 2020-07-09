import APIFetch from '@/helpers/APIFetch';

const endpoint = '/api/productsdata/';

export class ProductsData {
	static getProductData() {
		  return APIFetch.get(`${endpoint}`);
    }
    static readProductId(id) {
		  return APIFetch.get(`${endpoint}${id}/`);
    }
}