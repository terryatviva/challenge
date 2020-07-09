<template>
    <div class="navigation">
		<div class="container-fluid">
			<div class="row">
				<div class="col-1 pb-1">
					<span class="inm-diagonal-white">
						<img src="../assets/title_image.png" height="64px" class="" alt="ProductReview App">
					</span>
				</div>
                <div class="col-3 pl-0"><p></p>
                    <span class="navbar-brand">Product Review System</span>
                </div>
				<div class="col-4 text-center inventory">
					<ul>
						<li>
							<router-link  to="/productsdata"><p>HOME</p></router-link>
						</li>
					</ul>
				</div>
				<div class="col-4 text-right inventory">
					<ul>
						<li>
							<router-link  to="/adminpanel"><p>ADMIN - PANEL</p></router-link>
						</li>
					</ul>
				</div>
			</div>
		</div>
    </div>
</template>
<script>
export default {
	components: {
	},
	data() {
		return {
			data: 'This is navigation component',
		};
	},
	computed: {
	},
	async created() {
	},
	methods: {
	}
};
</script>
<style lang="stylus" scoped>
//color variables
navbar-color = #02AEDA
navbar-bg-color = #02AEDA
font-size = 14px
model-color = #E7ECF1
//styles
.navigation
	height 65px
	background-color #C46210
	color #ffffff
	position sticky 
	top 0px
	z-index 999
	img 
		padding 5px
		padding-left 20px
	&:before
		content: "";
		position: absolute;
		top: 0;
		left: 13px;
		width: 390px
		height: 100%;
		background: #fff;
		z-index: -1;
		-webkit-transform: skewX(-22.5deg);
		transform: skewX(-22.5deg);
	.navbar-brand
		color #AB274F
		font-family fantasy;
		font-weight bold
        padding 17px 0px
        vertical-align middle
	#inventory
		color #ffffff
        font-size 14px
		font-weight bold
		background-color white-space nowrap
.inventory ul
	list-style-type none 
	padding 0px
	margin 0px
	li
		a
			font-size 14px
			font-weight 500
			// line-height 6px
			color #FFFFFF
			border none
			font-family: 'BentonSans bold';
		p
			font-size 20px
			font-weight 400
			line-height 20px
			margin-top 20px
			// padding-right 10px
			font-family: 'BentonSans';
			color #fff

</style>