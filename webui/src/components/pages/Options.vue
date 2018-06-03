<template>
  <section class="container">
    <h1 class="title is-1 has-text-centered">Options</h1>

    <label>Telegram token :</label>
    <input class="input" type="text" placeholder="Text input">

    <h2 class="title is-2 has-text-centered">User list</h2>
    <a class="button is-success is-large is-pulled-right" @click="toggleModal()">Create</a>

    <user-table @delete="removeUser" @update="updateModal" v-if="isUsersLoaded"></user-table>
    <div class="columns" v-else>
      <div class="column is-12">
        <h3>{{ errorMessage }}</h3>
      </div>
    </div>

    <div class="modal" :class="{ 'is-active': isActive }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <form>
          <h3 class="title is-3">Create user</h3>
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
            <button class="button is-primary" @click="post(user)">Submit</button>
          </div>
        </form>
      </div>
      <button class="modal-close is-large" aria-label="close" @click="toggleModal()"></button>
    </div>

    <div class="modal" :class="{ 'is-active': updateActiveModal }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <form>
          <h3 class="title is-3">Update user</h3>
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="user.mail">
            </div>
          </div>
          <div class="control">
            <button class="button is-primary" @click="updateUser()">Submit</button>
          </div>
        </form>
      </div>
      <button class="modal-close is-large" aria-label="close" @click="updateModal()"></button>
    </div>


  </section>
</template>

<script>
import UserTable from "../UserTable";
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
      isActive: false,
      updateActiveModal: false,
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
      'removeUser',
      'postUser',
      'updateUser'
    ]),
    toggleModal() {
      this.isActive = !this.isActive;
    },
    updateModal() {
      this.updateActiveModal = !this.updateActiveModal;
    },
    resetModel() {
      this.user.password = '';
      this.user.mail = '';
    },
    async post () {
      try {
        const newUser = await this.postUser(this.user);
        this.toggleModal();
        this.resetModel();
      } catch (e) {
        //this.error
        this.resetModel();
      }
    },
    update() {
      this.updateActiveModal = !this.updateActiveModal;
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
h3 {
  color: white;
}
</style>
