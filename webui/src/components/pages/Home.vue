<template>
  <section class="container">
    <h2>Welcome {{ user }}</h2>
    <button @click="login(user)">click</button>

    <button @click="simulateCall">Simulate Call</button>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Home',

  data () {
    return {
      user: 'Admin'
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

    simulateCall () {
      const socket = this.$store.getters.socket;
      socket.emit('message', 'ping');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
