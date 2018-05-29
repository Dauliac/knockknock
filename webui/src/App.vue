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
    const socket = this.$store.getters.socket;

    socket.on('connected', (data) => {
      this.$store.dispatch('connected', data);
    });

    socket.on('call', (ringtone) => {
      console.log(ringtone);
    });

    socket.on('streaming', (video_url) => {
      console.log(video_url);
    });
  }
}
</script>

<style>

</style>
