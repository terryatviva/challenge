<template>
  <div class="home">
    <div class="flex items-center flex-col text-center">
      <h1 class="text-4xl">User Feedback Survey</h1>
    </div>
    <div class="content">
      <h3 class="p-4 m-4">we wanted to improve our products by taking out a quick survey from our customers 
        asking what they like & dislike about our products.</h3>
      
      <div class="fixed w-full">
        <div class="flex-none flex justify-center my-3">
          <button class="cv-btn cv-btn-primary" v-on:click="proceed" >PROCEED</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods:{
    proceed(){
      this.$router.push("/feedback");
    }
  }
};
</script>
