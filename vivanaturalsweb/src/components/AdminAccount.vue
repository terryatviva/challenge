<template>
	<div id="admin" v-if="!loginData">
		<div class="row ">
			<div class="col-md-12">
				<h1 class="admin">Admin Login</h1><hr/>
			</div>  			
		</div> 
		<div class="row">
			<div class="col-md-3">
			</div>
			<div class="col-md-6">
				<label class="label">User Name</label>
			</div>
			<div class="col-md-3">
			</div>
		</div>
		<div class="row">
			<div class="col-md-3">
			</div>
			<div class="col-md-6">
				<input class="inputbox" v-model="user"/>
			</div>
			<div class="col-md-3">
			</div>
		</div>
		<div class="row">
			<div class="col-md-3">
			</div>
			<div class="col-md-6">
				<label class="label">Password</label>
			</div>
			<div class="col-md-3">
			</div>
		</div>
		<div class="row">
			<div class="col-md-3">
			</div>
			<div class="col-md-6">
				<input type="password" class="inputbox" v-model="password"/>
			</div>
			<div class="col-md-3">
			</div>
		</div>
		<div class="row">
			<div class="col-md-3">
			</div>
			<div class="col-md-6">
				<button class="button login" @click="login">Login</button>
			</div>
			<div class="col-md-3">
			</div>
		</div>
	</div>
	<div v-else-if="loginData">
		<div class="col-md-12 result">
			<div class="row">
				<label class="header col-md-3 label">Name</label>
				<label class="header col-md-3 label">Country</label>
				<label class="header col-md-3 label">City</label>
				<label class="header col-md-3 label">Date Ins</label>
			</div><hr/>			
			<div class="result-data">
				<div v-for="data in resultArray">
					<div class="row row-data" @click="showData(data)">
						<div class="col-md-3"><span class="label lebel-data">{{data.name}}</span></div>	
						<div class="col-md-3"><span class="label lebel-data">{{data.country}}</span></div>
						<div class="col-md-3"><span class="label lebel-data">{{data.city}}</span></div>
						<div class="col-md-3"><span class="label lebel-data">{{data.dateIns}}</span></div>
					</div>
				</div>
			</div><hr/>
		</div>
		<Modal v-if="showModal" :feedbackData="itemData"></Modal>
	</div>
</template>

<script>
import ajax from '../utils/http-common'
import Modal from './ShowModal.vue'
export default{
	name:'Admin',
	components:{Modal},
	data(){
		return{
			user:'',
			password:'',
			loginData:false,
			resultArray :[],
			showModal:false,
			itemData:{}
		}
	},
	methods:{
		login: function(){
			if(this.user==='Admin' && this.password==='Admin'){
				this.loginData=true;
				this.$parent.logoutdata = true;
				ajax.get(`http://localhost:8085/feedback`).then(res=>this.resultArray=res.data);
			}
		},
		showData: function(data){console.log(data);
			this.itemData = data;
			this.showModal = true;			
		}
	}
}
</script>
<style scoped>

</style>