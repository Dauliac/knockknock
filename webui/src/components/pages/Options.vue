<template>
  <section class="container">
    <h1 class="title is-1 has-text-centered">Options</h1>

    <label>Telegram token :</label>
    <input class="input" type="text" placeholder="Text input">

    <h2 class="title is-2 has-text-centered">User list</h2>
    <a class="button is-success is-large is-pulled-right" @click="toggleModal()">Create</a>

    <user-table @delete="removeUser" v-if="isUsersLoaded"></user-table>
    <div class="columns" v-else>
      <div class="column is-12">
        <h3>{{ errorMessage }}</h3>
      </div>
    </div>

    <div class="modal" :class="{ 'is-active': isActive }">
      <div class="modal-background"></div>
      <div class="modal-content">
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
            <button class="button is-primary" @click="postUser">Submit</button>
          </div>
        </form>
      </div>
      <button class="modal-close is-large" aria-label="close" @click="toggleModal()"></button>
    </div>
  </section>
</template>

<script>
import UserTable from "../UserTable";
import axios from 'axios';
import configApi from '../../../config-api-route';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "Options",
  components: {
    UserTable
  },
  computed: {
    ...mapGetters([
      'users'
    ])
  },
  data() {
    return {
      telegramToken: '',
      users: [],
      isActive: false,
      user: {
        password: '',
        mail: ''
      },
      isUsersLoaded: false,
      errorMessage: ''
    }
  },

  methods: {
    ...mapActions([
      'removeUser'
    ]),
    toggleModal() {
      this.isActive = !this.isActive;
    },
    resetModel() {
      this.user.password = '';
      this.user.mail = '';
    },
    postUser() {
      const params = new URLSearchParams();
      params.append('email', this.user.mail);
      params.append('password', this.user.password);
      axios.post(configApi.url + 'users/create', params)
        .then(res => {
          console.log(res);
          this.resetModel();
        })
        .catch(err => console.log(err))
    },
  },

  mounted() {
    if (this.users.length !== 0) {
      this.isUsersLoaded = true;
    } else {
      this.$store.dispatch('getUsers')
        .then(() => {
          this.isUsersLoaded = true;
        })
        .catch(err => {
          this.errorMessage = err.message;
        });
    }
  }
}
</script>

<style scoped>
.label {
  color: white;
}
</style>
