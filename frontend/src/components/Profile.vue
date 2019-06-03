<template>
  <div class="profile">
    <div class="container">
      <h1>Your Profile</h1>
      <p>Name: {{ this.usersdata.username }}</p>
      <p>Email: {{ this.usersdata.email }}</p>
    </div>
  </div>

</template>

<script>
// import axios from 'axios'

export default {
  data () {
    return {
      usersdata: ''
    }
  },
  mounted () {
    this.getUsers()
  },
  methods: {
    getUsers () {
      this.$api.UserProfile(this.$store.state.user.user_id)
      .then(response => {
        console.log('response => ', response)
        if (response.data) {
          this.usersdata = response.data
        }
      })
      .catch(e => {
        console.log(e)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
