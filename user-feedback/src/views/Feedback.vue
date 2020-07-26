<template>
  <div>
    <div class="container">
      <div id="feedback-form">
        <h1 class="text-3xl">Register</h1>
        <p class="m-4">Please fill in this form to submit your feedback about our products.</p>
        <hr />

        <div class="flex flex-col items-start">
          <label class="text-left" for="name">
            <b>Name</b>
          </label>
          <input
            type="text"
            v-model="userFeedback.name"
            placeholder="Enter Name"
            name="name"
            id="name"
            required
          />
        </div>

        <div class="flex flex-col items-start">
          <label class="text-left" for="dateOfBirth">
            <b>Date of birth</b>
          </label>
          <input
            type="date"
            v-model="userFeedback.dateOfBirth"
            placeholder="Enter Date of birth"
            name="dateOfBirth"
            id="dateOfBirth"
            required
          />
        </div>

        <div class="flex flex-col items-start">
          <label class="text-left" for="email">
            <b>Email</b>
          </label>
          <input
            type="email"
            v-model="userFeedback.email"
            placeholder="Enter email"
            name="email"
            id="email"
            required
          />
        </div>

        <div class="flex flex-col items-start">
          <label class="text-left" for="country">
            <b>Country</b>
          </label>
          <input
            type="text"
            v-model="userFeedback.country"
            placeholder="Enter Country"
            name="country"
            id="country"
            required
          />
        </div>

        <div class="flex flex-col items-start">
          <label class="text-left" for="city">
            <b>City</b>
          </label>
          <input
            type="text"
            v-model="userFeedback.city"
            placeholder="Enter City"
            name="city"
            id="city"
            required
          />
        </div>

        <div class="flex flex-col items-start">
          <label class="text-left" for="thingsLiked">
            <b>Things you like about our products</b>
          </label>
          <input
            type="text"
            v-model="userFeedback.thingsLiked"
            placeholder="Enter things you like about our products"
            name="thingsLiked"
            id="thingsLiked"
            required
          />
        </div>

        <div class="flex flex-col items-start">
          <label class="text-left" for="thingsDisliked">
            <b>Things you dislike about our products</b>
          </label>
          <input
            type="text"
            v-model="userFeedback.thingsDisliked"
            placeholder="Enter things you dislike about our products"
            name="thingsDisliked"
            id="thingsDisliked"
            required
          />
        </div>

        <div class="w-full">
          <div class="flex-none flex justify-center my-3">
            <button class="cv-btn cv-btn-primary" v-on:click="saveUserFeedback">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <div id="successModalPopup" class="modal hidden">
      <div class="p-5 fixed z-50 overflow-hidden w-screen bg-custom left-0 top-0 m-8 outline-none">
        <div class="flex flex-col">
          <div class="flex items-center flex-col text-center ">
              <img src="../assets/success.png" width="20%" alt="Sussess">
          </div>
          <div>
            <h1 class="text-xl font-bold">Completed</h1>
          </div>
          <div class="text-base">
            <h3>
              Thanks for your valueable feedback.
              <br />All the Best!
            </h3>
          </div>
          <div>
            <button class="cv-btn cv-btn-custom mt-6" v-on:click="home">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Axios from "axios";
export default {
  name: "feedback",
  data() {
    return {
      displaySuccessModal: null,
      userFeedback: {
        name: null,
        dateOfBirth: null,
        email: null,
        country: null,
        city: null,
        thingsLiked: null,
        thingsDisliked: null,
      },
    };
  },
  created() {
      this.displaySuccessModal = document.getElementById("successModalPopup");
      this.displaySuccessModal.style.display = "block";
  },
  methods: {
    saveUserFeedback() {
      console.log("feedback=", this.userFeedback);
      const _self = this;
      _self.displaySuccessModal = document.getElementById("successModalPopup");
      let httpOptions = {
        headers: { "Content-Type": "application/json" },
      };
      Axios.post(
        "http://localhost:8080/userFeedback",
        this.userFeedback,
        httpOptions
      ).then((response) => {
        console.log("response", response);
        if (response.status == 200) {
          //alert("Thanks for responding");
          _self.displaySuccessModal.style.display = "block";
        }
      });
    },
    home(){
        this.$router.push("/");
    }
  },
};
</script>
<style>
.container {
  padding: 16px;
  background-color: white;
}
/* Full-width input fields */
input[type="text"],
input[type="password"],
input[type="date"],
input[type="email"] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type="text"]:focus,
input[type="password"]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}
</style>