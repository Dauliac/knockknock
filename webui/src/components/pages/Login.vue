<template>
  <div class="test">
    <div class="container">
      <h1>Login</h1>
      <form class="form">
        <input class="form_field" type="text" placeholder="Username">
        <input class="form_field" type="password" placeholder="Password">
        <button class="btn" type="submit" id="login-button">Login</button>
      </form>
    </div>
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
  .test{
    height: 800px;
  }
  .container{
    margin: auto;
    height:20%;
    width: 50%;
    border: 0px solid grey;
    box-shadow: 5px 5px 5px grey;
    border-radius: .3em;
    font-family: 'Anton', sans-serif;
  }
  .form_field{
    display: flex;
    margin:auto;
    margin-top:1%;
    border:0;
    background-color: rgba(145, 145, 145, 0.281);
    opacity: 7%;
    font-family: 'Anton', sans-serif;
  }
  .btn{
    margin-top:2%;
    width: 50%;
    height: 50%;
    border: 0;
    background-color: black;
    color:white;
    border-radius: 0.5em;
    font-family: 'Anton', sans-serif;
  }
  .btn:focus{
    background-color: red;
  }
  .container:hover{
    background-color:rgba(223, 223, 223, 0.281);
    color:black;
  }
</style>
