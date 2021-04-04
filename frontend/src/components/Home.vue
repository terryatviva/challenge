<template>
    <div>
        <h1>Product Feedback Survey</h1>

        <p style="margin-top:3%;"> Good day! We are currently collecting our users' opinion on our products.</p>
        <p>Your answers will allow us to find the best way to improve and meet your expectations.</p>
        <p> We thank you for your time!</p>
        
        <b-button 
            variant="primary" 
            @click="()=>{
                this.$router.push({path: 'user-form'})
            }"
        >
            Begin
        </b-button>
             
    </div>
</template>