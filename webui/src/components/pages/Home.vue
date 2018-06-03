<template>
  <section class="container">
    <h2>Welcome {{ user }}</h2>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';

axios.defaults.headers['Content-type'] =  'application/x-www-form-urlencoded'

export default {
  name: 'Home',

  data () {
    return {
      user: 'Admin'
    }
  },
  created () {
    axios.get('http://0.0.0.0:5000/api/users')
      .then(response => {
        console.log(response)
      })
      .catch(err => {
        console.error(err)
      })
    const params = new URLSearchParams();
    params.append('email', 'admin@example.com')
    params.append('password', 'password')

    axios.post('http://0.0.0.0:5000/api/login', params)
      .then(response => {
        console.log(response)
      })
      .catch(err => {
        console.error(err)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
