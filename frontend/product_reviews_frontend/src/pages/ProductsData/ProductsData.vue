<template>
 <div class="container mt-100"><br>
    <!-- heading -->
    <div class="mb-4">
		<Divider><h4 class="p-bottom-2" style="color:#f15a22;padding: 20px 40px;">Products List</h4></Divider>
    </div>
	<div class="clearfix"></div>
	<!-- List the product details and Add Review Button -->
	<div class="Inventory">
		<div class="container">
			<div class="users-table">
				<table class="user-table-tabs">
					<thead>
						<th>PRODUCT NAME</th>
						<th>ACTIONS</th>
					</thead>
					<tr v-for="(item, index) in productsData" :key="index">
						<td class="text-capitalize" style="color:#1D1655">{{item.name}}</td>
						<td>
							<div>
								<Tooltip content="Add Review" placement="top">
									<a style="padding-right:10px" @click="closeInvent = true, reviewTypeDetail = 'add', productPropData = item">
										<Button type="primary">Add Review</Button>
									</a>
								</Tooltip>
							</div>
						</td>
					</tr>
				</table>
				<div v-if="productsData.length === 0">
					<p class="text-center" style="font-size: 14px; color: rgb(51, 102, 153); padding: 10px;">No Items Available</p>
				</div>
			</div>
		</div>
	</div>
   <div v-if="closeInvent">
      <AddProductReview :createBoolean="closeInvent" :reviewTypeDetail="reviewTypeDetail" :productData="productPropData" v-on:closeInventories="closeInventories"></AddProductReview>
   </div>
 </div>
</template>
<script src="./ProductsData.js"></script>
<style src="./ProductsData-stylus.styl" lang="stylus" scoped></style>
