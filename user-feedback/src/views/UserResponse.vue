<template>
  <div>
    <div class="flex items-center flex-col text-center cv-bg-primary">
        <h3 class="text-3xl">User Responses</h3>
    </div>
    <div>
      <table class="table table-striped table-bordered" id="user-response">
        <thead>
          <tr>
            <th class="px-4 py-2">Name</th>
            <th class="px-4 py-2">DOB</th>
            <th class="px-4 py-2">Email</th>
            <th class="px-4 py-2">Country</th>
            <th class="px-4 py-2">City</th>
            <th class="px-4 py-2">Things they like</th>
            <th class="px-4 py-2">Things they dislike</th>
          </tr>
        </thead>
      </table>
    </div>
  </div>
</template>
<script>
import Axios from "axios";
import moment from "moment";
export default {
  name: "user-feedback",
  data() {
    return {
      feedbackList: [],
    };
  },
  created() {
    Axios.get("http://localhost:8080/userFeedbacks").then((response) => {
      console.log("response", response);
      this.feedbackList = response.data;
      let datatable = $("#user-response").DataTable({
        data: this.feedbackList,

        columns: [
          {
            data: "name",
          },
          {
            data: "dateOfBirth",
            render: function (data) {
              return moment(data).format("MMM Do YYYY");
            },
          },
          { data: "email", orderable: "false" },
          { data: "country" },
          { data: "city" },
          { data: "thingsLiked", orderable: "false" },
          { data: "thingsDisliked", orderable: "false" },
        ],
      });
    });
  },
  methods: {
    getDate(date) {
      return moment(date).format("MMM Do YYYY");
    },
  },
};
</script>
<style>
.cv-bg-primary {
  background-color: #42cbf5;
}
</style>