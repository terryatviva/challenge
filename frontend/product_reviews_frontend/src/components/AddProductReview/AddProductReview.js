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
            reviewType: '',
            emailExists: '',
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
        this.reviewType = this.reviewTypeDetail
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
        this.getAllProductsReviewsList()
        console.log(this.userdata)
        console.log(this.productReviewData)
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
        checkEmailExists() {
            console.log(this.userdata.length)
            let email = this.email
            let emailExists = ''
            let review_type = 'add'
            let product_data = this.productData
            let product_reviews_data = this.productReviewData
            var res = this.userdata.map(function(el) {
                var o = Object.assign({}, el);
                if (o.email.toLowerCase() === email.toLowerCase()) {
                    emailExists = o.id
                    var result = product_reviews_data.map(function(review_data) {
                        var obj = Object.assign({}, review_data);
                        if (obj.user_id === o.id && obj.product_id_id === product_data.id) {
                            review_type = 'update'
                        }
                        return obj
                    })
                }
                return o;
            })
            this.reviewType = review_type
            this.emailExists = emailExists
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
        nonEditableData() {
            let error = true
            if (this.emailExists) {
                for (var i = 0; i < this.userdata.length; i++) {
                    if (this.emailExists === this.userdata[i].id) {
                        if (this.name !== this.userdata[i].name) {
                            this.errorpayload.name = "Name can't be editable as Email already exists."
                            error = false
                        }
                        if (this.dob !== this.userdata[i].date_of_birth) {
                            this.errorpayload.date_of_birth = "Date of Birth can't be editable as Email already exists."
                            error = false
                        }
                        if (this.email !== this.userdata[i].email) {
                            this.errorpayload.email = "Email can't be editable as Email already exists."
                            error = false
                        }
                        if (this.country !== this.userdata[i].country) {
                            this.errorpayload.country = "Country can't be editable as Email already exists."
                            error = false
                        }
                        if (this.city !== this.userdata[i].city) {
                            this.errorpayload.city = "City can't be editable as Email already exists."
                            error = false
                        }
                        break
                    }
                }
            }
            return error
        },
        formatDate() {
            if (this.date_of_birth) {
                let day = this.date_of_birth.getDate()
                let month = this.date_of_birth.getMonth() + 1
                let year = this.date_of_birth.getFullYear()
                this.dob = `${year}-${month}-${day}`
            }
        },
        async productReviewCreate(payload) {
            console.log('-----creating starts')
            await API.ProductReviews.createProductReview(payload).then(res => {
                console.log(res.data)
				if(res.status === 201) {
                    this.getAllUsersList();
                    this.getAllProductsReviewsList();
                    this.$Notice.success({
                        title: 'Thank You.',
                        desc: "Successfully added comments for the product."
                    });
                    this.close();
				}
			}).catch(err => {
                console.log(err.response.data)
                this.$Notice.error({
                    title: 'Product Review Failed',
                    desc: "Failed adding comments for the product."
                });
            })
        },
        async productReviewUpdate(id, payload) {
            console.log('----updataing starts')
            await API.ProductReviews.updateProductReview(id, payload).then(res => {
                console.log(res.data)
				if(res.status === 200) {
                    this.getAllUsersList();
                    this.getAllProductsReviewsList();
                    this.$Notice.success({
                        title: 'Thank You.',
                        desc: "Updated comments for the product."
                    });
                    this.close();
				}
			}).catch(err => {
                console.log(err.response.data)
                this.$Notice.error({
                    title: 'Product Review Failed',
                    desc: "Failed updating comments for the product."
                });
            })
        },
        updateProductReview() {
            console.log("---update")
            this.formatDate();
            this.cleanErrorPayload();
            this.checkEmailExists();
            if (this.formValidation() && this.nonEditableData()) {
                console.log("all set for update")
                let prod_id = this.productData.id
                let usr_id = this.emailExists
                let id = ''
                var res = this.productReviewData.map(function(el) {
                    var o = Object.assign({}, el);
                    if (o.user_id === usr_id && o.product_id_id === prod_id) {
                        id = o.id
                    }
                    return o;
                })
                let payload = {
                    name: this.name,
                    date_of_birth: this.dob,
                    email: this.email,
                    country: this.country,
                    city: this.city,
                    likes: this.likes,
                    dislikes: this.dislikes,
                    product_id: this.productData.id,
                }
                console.log(id)
                console.log(payload)
                this.productReviewUpdate(id, payload);
            }
        },
        createProductReview() {
            console.log("-----create")
            this.formatDate();
            this.cleanErrorPayload();
            this.checkEmailExists();
            if (this.formValidation() && this.nonEditableData()) {
                console.log("all set for create")
                let payload = {
                    name: this.name,
                    date_of_birth: this.dob,
                    email: this.email,
                    country: this.country,
                    city: this.city,
                    likes: this.likes,
                    dislikes: this.dislikes,
                    product_id: this.productData.id,
                }
                console.log(payload)
                if (this.reviewType === 'add') {
                    this.productReviewCreate(payload)
                } else if (this.reviewType === 'update') {
                    this.updateProductReview()
                }
            }
        },
        close() {
            this.$emit('closeInventories');
        },
	}
}