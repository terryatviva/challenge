<template>
 <div class="container mt-100"><br>
    <!-- heading -->
    <div class="mb-4">
		<Divider><h4 class="p-bottom-2" style="color:#f15a22;padding: 20px 40px;">Users List</h4></Divider>
    </div>
	<div class="clearfix"></div>
	<div class="Inventory">
		<div class="container">
			<div class="users-table">
				<table class="user-table-tabs">
					<thead>
						<th>NAME</th>
            <th>DATE OF BIRTH</th>
            <th>EMAIL</th>
            <th>COUNTRY</th>
						<th>CITY</th>
					</thead>
          <!-- List the Users -->
					<tr v-for="(item, index) in userdata" :key="index">
						<td class="text-capitalize" style="color:#1D1655">{{item.name}}</td>
            <td class="text-capitalize" style="color:#1D1655">{{item.date_of_birth}}</td>
            <td style="color:#1D1655">{{item.email}}</td>
            <td class="text-capitalize" style="color:#1D1655">{{item.country}}</td>
            <td class="text-capitalize" style="color:#1D1655">{{item.city}}</td>
					</tr>
				</table>
				<div v-if="userdata.length === 0">
					<p class="text-center" style="font-size: 14px; color: rgb(51, 102, 153); padding: 10px;">No Users Available</p>
				</div>
			</div>
		</div>
	</div>
 </div>
</template>
<script src="./AdminPanel.js"></script>
<style src="./AdminPanel-styl.styl" lang="stylus" scoped></style>
