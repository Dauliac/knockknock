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

  computed: {
    ...mapGetters([
      'isAuthenticated'
    ]),
  },

  methods: {
    ...mapActions([
      'login'
    ])
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
