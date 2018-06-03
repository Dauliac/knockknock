<template>
  <section class="container">
    <h1 class="title is-1 has-text-centered">Options</h1>

    <label>Telegram token :</label>
    <input class="input" type="text" placeholder="Text input">

    <h2 class="title is-2 has-text-centered">User list</h2>
    <a class="button is-success is-large is-pulled-right">Create</a>

    <user-table :users="users"></user-table>

  </section>
</template>

<script>
import UserTable from "../UserTable";
import axios from 'axios';
import configApi from '../../../config-api-route';

export default {
  name: "Options",
  components: {UserTable},
  data() {
    return {
      telegramToken: '',
      users: []
    }
  },

  mounted() {
    axios.get(configApi.url + 'users')
      .then(res => {
        console.log(res.data);
        this.users = res.data;
      })
      .catch(err => console.log(err))
  }
}
</script>

<style scoped>

</style>
