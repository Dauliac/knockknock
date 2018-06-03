<template>
  <section class="container">

    <h2>Welcome {{ user }}</h2>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Home',

  data () {
    return {
      user: {
        mail: "",
        password: "",
      },
      errors: this.$store.state.errors,
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
