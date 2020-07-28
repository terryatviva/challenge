<template id="Modal">
  <div class="modal-backdrop">
    <div class="modal">
      <div class="modal-header">
      	<div class="row">
      		<div class="col-md-10">
      			<span class="res-data">{{feedbackData.name}}</span>      			
      		</div>
      		<div class="col-md-2">
      			<button type="button" class="btn-close" @click="close">x</button>
      		</div>
      	</div>      	
      </div>
      <div class="modal-body">
      	<div class="row">
      		<div class="col-md-6">
      			<label class="label modal-label">Country</label>
      		</div>
      		<div class="col-md-6">
  				<span class="label lebel-data">{{feedbackData.country}}</span>
  			</div>  			
      	</div> 
      	<div class="row">
  			<div class="col-md-6">
  				<label class="label modal-label">City</label>
  			</div>
  			<div class="col-md-6">
				<span class="label lebel-data">{{feedbackData.city}}</span>
			</div>  			
		</div>
		<div class="row">
			<div class="col-md-6">
				<label class="label modal-label">Date of Birth</label>
			</div>
			<div class="col-md-6">
				<span class="label lebel-data">{{feedbackData.dob}}</span>
			</div>  			
		</div>
		<div class="row">
			<div class="col-md-6">
				<label class="label modal-label">Email</label>
			</div>
			<div class="col-md-6">
				<span class="label lebel-data">{{feedbackData.email}}</span>
			</div>  			
		</div>
		<div class="row">
			<div class="col-md-6">
				<label class="label modal-label">Things Like</label>
			</div>
			<div class="col-md-6">
				<span class="label lebel-data">{{feedbackData.like}}</span>
			</div>  			
		</div>
		<div class="row">
			<div class="col-md-6">
				<label class="label modal-label">Things Dislike</label>
			</div>
			<div class="col-md-6">
				<span class="label lebel-data">{{feedbackData.dislike}}</span>
			</div>  			
		</div>
      </div>
      <div class="modal-footer">
      </div>
    </div>
  </div>
</template>
    
<script>
export default {
	name: 'Modal',
	props:['feedbackData'],
	methods: {
		close: function() {
			this.$parent.showModal = false;
		},
	}
};
</script>
