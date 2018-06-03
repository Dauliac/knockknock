<template>
  <div id="app">

    <div v-if="isAuthenticated">
      <navbar></navbar>
      <router-view/>
    </div>

    <login v-else></login>
  </div>
</template>

<script>
import 'normalize.css';
import 'bulma/css/bulma.css';
import './assets/css/helper.css';
import Navbar from './components/Navbar';
import Login from './components/Login';
import { mapGetters } from 'vuex';

export default {
  name: 'App',
  components: {
    Navbar,
    Login
  },

  computed: {
    ...mapGetters([
      'isAuthenticated'
    ])
  }
}
</script>

<style>

</style>
