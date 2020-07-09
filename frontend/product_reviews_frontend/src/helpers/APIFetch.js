import axios from 'axios';

const instance = axios.create({
	baseURL: process.env.VUE_APP_BASE_URL,
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
	}
});
instance.interceptors.request.use(function (config) {

	config.headers = {
		...config.headers,
	}

	return config;
});

instance.interceptors.response.use(function (response) {
	// Return the response
	return response;
}, function (error) {
	return Promise.reject(error);
});
export default instance;