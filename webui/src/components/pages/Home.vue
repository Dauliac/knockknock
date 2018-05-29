<template>
  <div>
    <h1>Home</h1>
    <h2>Welcome {{ user }}</h2>
  </div>
</template>

<script>
import Navbar from '../Navbar';

export default {
  name: 'Home',

  components: {
    Navbar
  },

  data () {
    return {
      user: 'Admin'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
