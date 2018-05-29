<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<script>
import 'normalize.css';
import 'bulma/css/bulma.css';
import './assets/css/helper.css';
import Navbar from './components/Navbar';
import io from 'socket.io-client';

export default {
  name: 'App',
  components: {
    Navbar
  },
  mounted () {
    const socket = io('http://0.0.0.0:5000');

    socket.on('connected', (data) => {
      this.$store.dispatch('connected', data);
    });

  }
}
</script>

<style>

</style>
