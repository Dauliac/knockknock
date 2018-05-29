<template>
  <section class="container">
    <h2>Welcome {{ user }}</h2>
    <button @click="login(user)">click</button>

    <button @click="clickButton(1)">Socket emit</button>
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

  sockets:{
    connect () {
      console.log('socket connected')
      console.log(this.$socket.emit('connected', 'Hello!'))
    },
    customEmit (val) {
      console.log('this method was fired by the socket server. eg: io.emit("customEmit", data)')
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

    clickButton(val) {
      this.$socket.emit('connected', val);
    }
  },

  mounted () {
    this.$options.sockets.connected = (data) => {
      console.log('Yoyoyo!', data)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
