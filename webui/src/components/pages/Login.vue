<template>
  <div class="test">
    <div class="container" v-if="!isAuthenticated">
      <h1>Login</h1>
      <form class="form">
        <input v-model="user.email"class="form_field" type="text" placeholder="Username">
        <input v-model="user.password" class="form_field" type="password" placeholder="Password">
        <button class="btn" type="submit" id="login-button" @click="login(user)">
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "Login",

  computed: {
    ...mapGetters([
      'isAuthenticated'
    ])
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
    ...mapActions([
      'login'
    ]),

    resetUser() {
      this.user.email = '';
      this.user.password = '';
    },

    async checkToken(token) {
      const check = await axios.get('/authenticate');
    },

    async postRequest() {
      // const post = await axios.post('/login', {
      //   email: this.user.email,
      //   password: this.user.password
      // });
    }
  }
}
</script>

<style scoped>
  .container{
    margin: auto;
    height:9em;
    width: 50%;
    border: 0px solid grey;
    box-shadow: 1px 1px 5px grey;
    border-radius: .3em;
    font-family: 'Anton', sans-serif;
  }
  .container:hover{
    background-color:rgba(223, 223, 223, 0.281);
    color:black;
  }
</style>
