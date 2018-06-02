<template>
  <section class="container">
    <h2>Welcome {{ user }}</h2>
    <button @click="login(user)">click</button>

<<<<<<< HEAD
    <button @click="clickButton(1)">Socket emit</button>

    <div class="buttons has-addons is-boxed">
      <span class="button is-success is-selected is-rounded">Accept rington</span>
      <span class="button is-danger is-rounded">Decline ringtion</span>
    </div>



    <div class="card">
      <div class="card-content">
        <p class="title">
          Appel en cours ...
        </p>
      </div>
      <footer class="card-footer">
        <p class="card-footer-item">
          <span class="button is-success">Accept rington</span>
        </p>
        <p class="card-footer-item">
      <span>
        Share on <a href="#">Facebook</a>
      </span>
        </p>
      </footer>
    </div>
=======
    <button @click="simulateCall">Simulate Call</button>
>>>>>>> 31f367dc49e666058bc8babdc5042e12a02b9a0b
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
