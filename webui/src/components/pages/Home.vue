<template>
  <section class="container">
    <h2>Welcome {{ user }}</h2>
    <form>
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="user.mail">
        </div>
      </div>
      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" type="password" placeholder="password" v-model="user.password">
        </div>
      </div>
      <div class="control">
        <button class="button is-primary" @click="login(user)">Submit</button>
      </div>
    </form>
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
      user: {
        mail: "",
        password: ""
      }
    }
  },
  computed: {
    ...mapGetters([
      'isAuthenticated'
    ]),
  },

  methods: {
    ...mapActions([
      'login'
    ]),
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
