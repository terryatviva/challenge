<template>
    <div>
        <user-card
            v-for="user in users"
            v-bind:key="user.id"
            v-bind:name="user.name"
            v-bind:dateOfBirth="user.date_of_birth"
            v-bind:email="user.email"
            v-bind:country="user.country"
            v-bind:city="user.city"
            v-bind:likes="user.likes"
            v-bind:dislikes="user.dislikes"
        >
        </user-card>
    </div>
</template>

<script>
import UserCard from './UserCard.vue'

export default {
    components: { UserCard },
    created () {
        this.fetchData()
    },
    methods: {
        fetchData() {
            fetch("http://127.0.0.1:8000/users")
            .then(async response => {
                const data = await response.json()                
                this.users = data.users
            })
        }
    },
    data: function() {
        return {
            users: []
        }
    },

}
</script>
