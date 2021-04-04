<template>
    <div
      class="d-flex align-items-center justify-content-center"
      style="bottom: 0; overflow-y: auto; margin-bottom:50px;"
    >
        <b-card style="width:40%;background-color:#B3E5FC" :title=name :sub-title=email>
          <br>
          <b-card-text>
            <b>Date of birth</b>: {{ dateOfBirth }} <br>
            <b>Country</b>: {{ country }} <br>
            <b>City</b>: {{ city }} <br>
          </b-card-text>

          <b-card-text>
            <b>Likes</b>: {{ likes }} <br>
          </b-card-text>

          <b-card-text>
            <b>Dislikes</b>: {{ dislikes }}
          </b-card-text>

        </b-card>
    </div>
</template>

<script>

export default {
  props: {
    name: {
      type: String,
      required: true,
      default: "",
    },
    dateOfBirth: {
      type: String,
      required: true,
      default: "",
    },
    email: {
      type: String,
      required: true,
      default: "",
    },
    country: {
      type: String,
      required: true,
      default: "",
    },
    city: {
      type: String,
      required: true,
      default: "",
    },
    likes: {
      type: String,
      required: true,
      default: "",
    },
    dislikes: {
      type: String,
      required: true,
      default: "",
    },
  }
}
</script>
