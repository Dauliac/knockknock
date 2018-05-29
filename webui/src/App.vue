<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<script>
import 'normalize.css';
import 'bulma/css/bulma.css';
import './assets/css/helper.css';
import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>

</style>
