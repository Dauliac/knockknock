<template>
  <table class="table is-fullwidth is-hoverable">
    <thead>
    <tr>
      <th>ID</th>
      <th>Email</th>
      <th>Created at</th>
      <th></th>
      <th></th>
    </tr>
    </thead>

    <tbody>
    <tr v-for="(user, i) in users" :key="i">
      <th>{{ user.id }}</th>
      <th>{{ user.email }}</th>
      <th>{{ user.created }}</th>
      <th><a class="button is-warning" @click="updateUser(user)">Update</a></th>
      <th><a class="button is-danger" @click="deleteUser(user)">Delete</a></th>
    </tr>
    </tbody>
  </table>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: "UserTable",

  computed: {
    ...mapGetters([
      'users'
    ])
  },

  methods: {
    deleteUser(user) {
      this.$emit('delete', user);
    },
    updateUser(user) {
      this.$emit('update', user);
    }
  }
}
</script>

<style scoped>

</style>
