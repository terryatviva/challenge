import { API } from '@/api';
import { mapState } from 'vuex';
import json_data from '@/assets/countries_cities.json';

export default {
    name: 'AddProductReview',
    props: ['createBoolean', 'reviewTypeDetail', 'productData'],
    data() {
		return {
            name: '',
            date_of_birth: '',
            dob: '',
            email: '',
            country: '',
            city: '',
            likes: '',
            dislikes: '',
            product_id: '',
            countryList: [],
            cityList: [],
            errorpayload: {
                name: '',
                date_of_birth: '',
                email: '',
                country: '',
                city: '',
                likes: '',
                dislikes: '',
                product_id: '',
            }
		};
	},
	async created() {
        let cities_list = []
        for (var key in json_data) {
            let country_obj, city_obj = {}
            country_obj = {
                value: key.toLowerCase(),
                label: key.toLocaleUpperCase()
            }
            this.countryList.push(country_obj)
            json_data[key].forEach(function (item, index) {
                city_obj = {
                    value: item.toLowerCase(),
                    label: item.toLocaleUpperCase()
                }
                cities_list.push(city_obj)
            });
        }
        this.cityList = cities_list
        this.getAllUsersList()
        console.log(this.userdata)
	},
	computed: {
        ...mapState({
			userdata: state => state.userdata.userdata,
		})
	},
	methods: {
        getAllUsersList() {
            this.$store.dispatch('userdata/getAllUsersList')
        },
        cleanErrorPayload() {
            this.errorpayload.name = ''
            this.errorpayload.date_of_birth = ''
            this.errorpayload.email = ''
            this.errorpayload.country = ''
            this.errorpayload.city = ''
            this.errorpayload.likes = ''
            this.errorpayload.dislikes = ''
            this.errorpayload.product_id = ''
        },
        formValidation() {
            let msg = "This field may not be blank"
            let error = true
            if(!this.name) {
                this.errorpayload.name = msg
                error = false
            } else {
                let name_reg = /[a-zA-Z]/;
                if(this.name.search(name_reg) == -1) {
                    this.errorpayload.name = "Name must contain atleast one letter"
					error = false
                }
                if(this.name.length < 3) {
					this.errorpayload.name = "Ensure this field has at least 3 characters."
					error = false
				}
            }
            if(!this.date_of_birth) {
                this.errorpayload.date_of_birth = msg
                error = false
            } else {
                var currentTime = new Date()
                var month = currentTime.getMonth() + 1
                var day = currentTime.getDate()
                var year = currentTime.getFullYear()
                var currentDate = `${year}-${month}-${day}`
                console.log(currentDate, this.date_of_birth)
                if (currentDate < this.dob) {
                    this.errorpayload.date_of_birth = "Date of Birth exceeds current date"
                    error = false
                }
            }
            if(!this.email) {
                this.errorpayload.email = msg
                error = false
            } else if(this.email.length > 100) {
                this.errorpayload.email = 'Ensure this field has not more than 100 character.'
                error = false
            } else {
                var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
                if (reg.test(this.email) == false) {
                    this.errorpayload.email = 'Enter Valid Email Address.'
                    error = false
                }
            }
            if(!this.country) {
                this.errorpayload.country = msg
                error = false
            }
            if(!this.city) {
                this.errorpayload.city = msg
                error = false
            }
            if (this.country && this.city) {
                var city = this.city
                var flag = false
                for (var key in json_data) {
                    if ((key.toLowerCase() === this.country.toLowerCase())) {
                        json_data[key].forEach(function (item, index) {
                            if (item.toLowerCase() === city.toLowerCase()) {
                                flag = true
                            }
                        });
                    }
                    if (flag) {
                        break
                    }
                }
                if (!flag) {
                    this.errorpayload.city = "City not exists in Selected Country"
                    error = false
                }
            }
            if(!this.likes) {
                this.errorpayload.likes = msg
                error = false
            } else if(this.likes.length < 3) {
                this.errorpayload.likes = "Ensure this field has at least 3 characters."
                error = false
            }
            if(!this.dislikes) {
                this.errorpayload.dislikes = msg
                error = false
            } else if(this.dislikes.length < 3) {
                this.errorpayload.dislikes = "Ensure this field has at least 3 characters."
                error = false
            }
            return error
        },
        createProductReview() {
            console.log("camee")
            if (this.date_of_birth) {
                let day = this.date_of_birth.getDate()
                let month = this.date_of_birth.getMonth() + 1
                let year = this.date_of_birth.getFullYear()
                this.dob = `${year}-${month}-${day}`
            }
            console.log(this.date_of_birth)
            this.cleanErrorPayload();
            if (this.formValidation()) {
                console.log("all set")
            }
        },
        close() {
            this.$emit('closeInventories');
        },
	}
}