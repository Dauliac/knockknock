<template>
      <form class="form">
        <input class="form_field" id="email" type="email" name="email" v-model="user.email"/>
        <input class="form_field" id="password" type="password" name="password" v-model="user.password"/>
        <button class="btn" type="submit" id="login-button">Login</button>
      </form>
</template>

<script>
export default {
  name: "UserForm",
  props: ['user']
}
</script>

<style scoped>
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
</style>
