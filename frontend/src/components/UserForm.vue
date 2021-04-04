<template>
  <div>
    <b-overlay :show="showOverlay" rounded="sm"     
        class="fixed-top d-flex align-items-center justify-content-center"
        style="bottom: 0; overflow-y: auto;"
    >
        <b-card style="width:50%;">
            <div v-if="errors.length">
                <ul class="alert alert-danger" style="list-style-type:none;">
                    <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
                </ul>
            </div>
            <b-form-group 
                label="Name"
                label-for="name"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-input
                    id="name"
                    v-model="name"
                    type="text"
                ></b-form-input>
            </b-form-group>

            <b-form-group 
                label="Date of birth"
                label-for="dateOfBirth"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-input
                    id="dateOfBirth"
                    v-model="dateOfBirth"
                    type="date"
                    name="dateOfBirth"
                ></b-form-input>
            </b-form-group>

            <b-form-group 
                label="Email"
                label-for="email"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-input
                    id="email"
                    v-model="email"
                    type="email"
                    name="email"
                    placeholder="example@gmail.com"
                ></b-form-input>
            </b-form-group>

            <b-form-group 
                label="Country"
                label-for="country"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-input
                    id="country"
                    v-model="country"
                    type="text"
                    name="country"
                ></b-form-input>
            </b-form-group>

            <b-form-group 
                label="City"
                label-for="city"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-input
                    id="city"
                    v-model="city"
                    type="text"
                    name="city"
                ></b-form-input>
            </b-form-group>

            <b-form-group 
                label="Likes"
                label-for="likes"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-textarea
                    id="likes"
                    v-model="likes"
                    placeholder="Tell us what you liked about our products"
                    rows="3"
                    max-rows="6"
                ></b-form-textarea>
            </b-form-group>

            <b-form-group 
                label="Dislikes"
                label-for="dislikes"
                label-cols-sm="4"
                label-cols-lg="3"
                content-cols-sm
                content-cols-lg="7"
            >
                <b-form-textarea
                    id="dislikes"
                    v-model="dislikes"
                    placeholder="Tell us what you disliked about our products"
                    rows="3"
                    max-rows="6"
                ></b-form-textarea>
            </b-form-group>

            <b-button
            :disabled="!isFormComplete"
            variant="primary"
            @click="submit"
            >
                Submit
            </b-button>

        </b-card>
    </b-overlay>
  </div>
</template>

<script>

export default {
  name: "UserForm",
  data: function() {
    return {
      name: null,
      dateOfBirth: null,
      email: null,
      country: null,
      city: null,
      likes: null,
      dislikes: null,
      errors: [],
      showOverlay: false,
    }
  },
  computed: {
      isFormComplete() {
          return this.name && this.dateOfBirth && this.email && this.country
            && this.city && this.likes && this.dislikes
      }
  },
  methods: {
    submit: function(e) {
      e.preventDefault()
      this.showOverlay = true
      this.errors = []

      let request = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          name: this.name,
          date_of_birth: this.dateOfBirth,
          email: this.email,
          country: this.country,
          city: this.city,
          likes: this.likes,
          dislikes: this.dislikes,
        })
      }

      fetch("http://127.0.0.1:8000/users", request)
      .then(async response => {
        const data = await response.json()
        if (response.status === 200) {
          this.$router.push({path: 'complete'})
        } else {
          this.errors.push(data.message)
        }
      })
      .catch(error => {
        this.errors.push(error)
      })
      .finally(() => {
          this.showOverlay = false
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
    