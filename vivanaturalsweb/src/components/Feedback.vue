<template>
  <div id="feedback">
  	<div class="row">
  		<div class="col-md-10">
  			<img src="/img/viva.png" height="100px"/>
  		</div> 
  		<div class="col-md-2" v-if="!adminPage">
  			<label @click="admin" class="icon-user" title="Admin Account"><img src="/img/user.png" height="25px" width="25px"/> <span>Login</span></label>
  		</div> 
  		<div class="col-md-2" v-if="logoutdata">
			<label @click="logout" class="icon-user" title="Admin Account"><img src="/img/user.png" height="25px" width="25px"/> <span>Logout</span></label>
		</div> 
  	</div><hr/>
  	<div class="row" v-if="thanks">
  		<div class="col-md-12">
  			<Thanks></Thanks>
  		</div>  		
  	</div>
  	<div class="row" v-if="!thanks">
  		<div class="col-md-2">
  		</div>
  		<div class="col-md-8" v-if="adminPage">
  			<Admin ref="adminref"></Admin>
  		</div>
  		<div class="col-md-8" v-if="!adminPage">
  			<div class="row ">
  				<div class="col-md-12">
  					<h1>User's Feedback</h1><hr/>
  				</div>  			
  			</div> 
  			<div class="row">
  				<div class="col-md-6">
   					<label class="label">Name<span class="red">*</span></label>
  				</div>	
  				<div class="col-md-6">
   					<label class="label">Date of Birth<span class="red">*</span></label>
  				</div>  		
  			</div>
  			<div class="row">
  				<div class="col-md-6">
   					<input class="inputbox" v-model="name"/>
  				</div>  		
  				<div class="col-md-6">
   					<datepicker v-model="dob"></datepicker>
  				</div>
  			</div>
  			<div class="row">
  				<div class="col-md-6">
   					<label class="label" for="country">Country<span class="red">*</span></label>
  				</div>
  				<div class="col-md-6">
   					<label class="label" for="city">City<span class="red">*</span></label>
  				</div>
  			</div>
  			<div class="row">
  				<div class="col-md-6">
					<vue-select v-model="country" id="country" label="name" :options="countryArray" @input="setCityData"></vue-select>
  				</div>
  				<div class="col-md-6">
   					<vue-select v-model="city" id="city" label="name" :options="cityArray" :disabled="!country"></vue-select>
  				</div>
  			</div> 
  			<div class="row">
  				<div class="col-md-6">
   					<label class="label">Things you Like<span class="red">*</span></label>
  				</div>
  				<div class="col-md-6">
  					<label class="label">Things you Dislike</label>   					
  				</div>
  			</div>
  			<div class="row">
  				<div class="col-md-6">
   					<textarea class=" inputbox" v-model="like"/>
  				</div>
  				<div class="col-md-6">
   					<textarea class=" inputbox" v-model="dislike"/>
  				</div>
  			</div>
  			<div class="row">
  				<div class="col-md-6">
   					<label class="label">Email<span class="red">*</span></label>
  				</div>  		
  			</div>
  			<div class="row">
  				<div class="col-md-6" >
   					<input class="inputbox" :class="emailClass" v-model="email" @input="isEmailValid"/>
  				</div>
  			</div>
  			<div class="row col-md-12">
  				<button class="button" @click="submit">Submit</button>
  			</div>
  		</div>
  		<div class="col-md-2">
  		</div>
  	</div>	
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker'
import Thanks from './Thankyou.vue'
import Admin from './AdminAccount.vue'
import ajax from '../utils/http-common'
import vueSelect from 'vue-select'

export default {
  name: 'Feedback',
  components:{
  	Datepicker,Thanks,Admin,vueSelect
  },  
  data(){
  	return{
  		name:'',
  		dob:'',
  		email:'',
  		country:'',
  		city:'',
  		like:'',
  		dislike:'',
  		emailClass:'inputbox',
  		reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/,
  		thanks: false,
  		adminPage: false,
		countryArray:[],
		cityArray:[],
		logoutdata:false
  	}
  },
  mounted(){
	  this.getCountry();
  },
  methods:{
	getCountry: function(){
		ajax.get(`/data/Country.json`).then(res=>(this.countryArray=res.data));
	},
  	isEmailValid: function() {
  		this.emailClass = (this.reg.test(this.email)) ? 'inputbox' : 'email-error';
    },
    submit: function(){
    	if(this.formValidation()){
    		var data = {
    				name:this.name,
    				email:this.email,
    				dob:this.dob,
    				city:this.city.name,
    				country:this.country.name,
    				like:this.like,
    				dislike:this.dislike,
    				dateIns: new Date()
    		}
    		ajax.post('http://localhost:8085/feedback',data).then(res=> 
    			this.thanks = true
    		);    		
    	}    	
    },
    admin: function(){
    	this.adminPage = true;
    	this.thanks = false;
    },
	setCityData: function(){
		if(this.country){
			ajax.get(`/data/City.json`).then(res=> (res.data.filter(item=>{return item.country_id==this.country.id}))).then(res=>this.cityArray=res);
		}
	},
	formValidation: function(){
		var flag = true;
		if(!this.name){
			flag=false;
		}else if(!this.dob){
			flag=false;
		}else if(!this.country){
			flag=false;
		}else if(!this.city){
			flag=false;
		}else if(!this.like){
			flag=false;
		}else if(!this.email){
			flag=false;
		}
		return flag;
	},
	logout: function(){
		this.logoutdata=false;
		this.thanks = false;
		this.adminPage = false;
	}	
  }
}
</script>


<style scoped>
@import "~vue-select/dist/vue-select.css";
#feedback .feedback{
	background-color: #b1a9a9;
	font-size: 25px;
    font-family: initial;
    font-weight: 700;
    text-align: center;
    margin-bottom: 40px;
}
#feedback >>> .label{
	display: block;
    color: #5E5C58;
    font-weight: 500;
    font-size: 13px;
    text-align: left;
    margin-bottom: 5px;
    text-transform: uppercase;
}
#feedback >>> .button{
	display: block;
    font-weight: 500;
    font-size: 13px;
    text-align: center;
    margin-bottom: 5px;
    width:15%;
    height:44px;
    text-transform: uppercase;
    background: #82a130;
    color: #ffffff;
    border: 1px solid #82a130;
}
#feedback >>> .inputbox{
    display: block;
    width: 100%;
    height: 44px;
    min-height: 44px;
    padding: 10px 10px;
    margin: 0;
    line-height: 22px;
    border: 1px solid #cccccc;
    outline: none;
    background: #fff;
    color: #5f6a7d;
    font: 13px "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, sans-serif;
    margin-bottom: 15px;
    -webkit-appearance: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
}
#feedback >>> h1{
	font-family: Montserrat, sans-serif;
    font-weight: normal;
    font-size: 30px;
    text-transform: uppercase;
    line-height: 1.5;
    color: #8c8986;
    display: block;
    letter-spacing: 2px;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    margin: 0 auto 15px;
    clear: both;
    padding-top: 4px;
}

#feedback .viva-img{
	text-align: center;
}
#feedback >>> .vdp-datepicker input{
	display: block;
    width: 100%;
    height: 44px;
    min-height: 44px;
    padding: 0 10px;
    margin: 0;
    line-height: 22px;
    border: 1px solid #cccccc;
    outline: none;
    background: #fff;
    color: #5f6a7d;
    font: 13px "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, sans-serif;
    margin-bottom: 15px;
    -webkit-appearance: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
}
#feedback .red{
	color: #C33;
}
#feedback .icon-user{
	cursor: pointer;
	color: #716a65;
	font-size: 13px;
	letter-spacing: 1px;
}
#feedback .email-error{
	border: 2px solid #de2e2e;
}
#feedback >>> .login{
	width:25% !important;
}
#feedback >>> img {
	vertical-align: text-bottom;
}

#feedback >>> .v-select.disabled .dropdown-toggle input{
	 background-color: #0000;
}
#feedback >>> .v-select .open-indicator:before {
	border-left: 5px solid transparent;
 	border-right: 5px solid transparent;
 	border-top: 5px solid black;
 	content: "";
 	display: inline-block;
 	height: 0px;
 	width: 0px;
 	vertical-align: text-top;
 	transform: rotate(0deg) !important;
 	box-sizing: inherit;
}
#feedback >>> .v-select{	
	width: 100%;
}
 
#feedback >>> .v-select input[type=search]{
	font-style: normal;
}
#feedback >>> .v-select .vs__dropdown-menu .vs__dropdown-option--highlight{
	background-color:#82a130;
}
 
#feedback >>> .v-select .vs__dropdown-toggle{
 	height: 44px;
	border-radius: 2px;
	margin-bottom: 15px;
}
#feedback >>> .v-select .selected-tag{
	white-space: nowrap;
  	width: 120px;
  	overflow: hidden;
 	padding: .375rem 1.75rem .375rem .75rem;
 	font-weight: normal;
 	display: block;
 	color: #495057;
 	min-height: 1.2em;
 	padding: 0px 2px 1px;
 	font-style: normal;
 }
 
#feedback >>> .v-select .vs__dropdown-menu{
	max-height: 200px !important;
}
 
#feedback >>> .v-select .vs__dropdown-menu > li{
 	color: #495057 !important;
 	font-style: normal !important
}

#feedback >>> .header{
	font-size: 20px !important;
}
#feedback >>> .result-data{
	height: 200px;
	overflow-y: auto;
	overflow-x: hidden;
}
#feedback >>> .row-data{
	cursor: pointer;
	border: 1px solid #a09898;
	border-radius: 5px;
	margin-bottom: 1px;
}

#feedback >>> .modal-backdrop {
	  position: fixed;
	  top: 0;
	  bottom: 0;
	  left: 0;
	  right: 0;
	  background-color: rgb(100 169 61 / 30%);
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  opacity: 1;
}

#feedback >>> .modal {
	background: #FFFFFF;
	box-shadow: 2px 2px 20px 1px;
	display: flex;
	flex-direction: column;
	top:20%;
	left:25%;
	height:50%;
	width:50%;
}

#feedback >>> .modal-header,
.modal-footer {
	padding: 5px;
	display: flex;
}

#feedback >>> .modal-header {
	border-bottom: 1px solid #eeeeee;
	color: #4AAE9B;
	justify-content: space-between;
	display: table-column;
	text-align: center;
}

#feedback >>> .modal-footer {
	border-top: 1px solid #eeeeee;
	justify-content: flex-end;
}
#feedback >>> .modal-body {
	position: relative;
	padding: 20px 10px;
}

#feedback >>> .btn-close {
	  border: none;
	  font-size: 20px;
	  padding: 20px;
	  cursor: pointer;
	  font-weight: bold;
	  color: #4AAE9B;
	  background: transparent;
}

#feedback >>> .btn-green {
	  color: white;
	  background: #4AAE9B;
	  border: 1px solid #4AAE9B;
	  border-radius: 2px;
}
#feedback >>> .btn-close{
	float: right;
	display: contents;
}
#feedback >>> .res-data{
	color: #5E5C58;
	font-weight: 700;
	font-size: 20px;
	text-align: left;
	margin-bottom: 5px;
	text-transform: uppercase;
}
#feedback >>> .modal-label{
	text-align: left;
	font-size: 15px;
	font-weight: bold;
	padding: 5px;
}
#feedback >>> .lebel-data{
	padding:5px;
}

</style>
