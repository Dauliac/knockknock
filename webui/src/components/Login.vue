<template>
  <section class="hero is-dark is-fullheight">
    <div class="hero-body">
      <div class="container">
        <h1 class="title is-1 has-text-centered">Login form</h1>
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

        <div v-if="errors.length" v-for="(error, i) in errors" :key="i">
          <div class="message is-danger">
            <div class="message-header">
              <p>Danger</p>
              <button class="delete" aria-label="delete"></button>
            </div>
            <div class="message-body">{{ error }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Login',

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

<style scoped>
.message.is-danger {
  margin: 1rem 0;
}
.label {
  color: white;
}
</style>
