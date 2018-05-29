<template>
  <div>
    <h1>Login</h1>
    <user-form :user="user"></user-form>
  </div>
</template>

<script>
import axios from 'axios';
import UserForm from "../UserForm";

export default {
  name: "Login",
  components: {
    UserForm
  },
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
