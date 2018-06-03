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
    <tr v-for="(user, i) in users">
      <th>{{ user.id }}</th>
      <th>{{ user.email }}</th>
      <th>{{ user.created }}</th>
      <th><a class="button is-warning">Update</a></th>
      <th><a class="button is-danger">Delete</a></th>
    </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "UserTable",
  props: ['users'],
}
</script>

<style scoped>

</style>
