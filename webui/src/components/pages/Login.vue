<template>
  <div>
    <h1>Login</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Login",

  data() {
    return {
      user: {
        email: '',
        password: ''
      }
    }
  },

  methods: {
    resetUser() {
      this.user.email = '';
      this.user.password = '';
    },

    async checkToken(token) {
      const check = await axios.get('/authenticate');
    },

    async postRequest() {
      const post = await axios.post('/login', {
        email: this.user.email,
        password: this.user.password
      });
      console.log(post);
      this.resetUser();
    }
  }
}
</script>

<style scoped>

</style>
