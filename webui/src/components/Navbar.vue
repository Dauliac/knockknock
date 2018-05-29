<template>
    <header>
      <nav>
        <ul class="d-flex flex-row">
          <li v-for="(link, i) in links" :key="i">
            <router-link :to="{ name: link.path}" class="d-flex justify-center align-center">{{ link.title }}</router-link>
          </li>
        </ul>
      </nav>
    </header>
</template>

<script>
export default {
  name: "Navbar",

  data() {
    return {
      links: [
        {
          title: 'Home',
          path: 'Home'
        },
        {
          title: 'Login',
          path: 'Login'
        },
        {
          title: 'Stream',
          path: 'Stream'
        },
        {
          title: 'Options',
          path: 'Options'
        },
        {
          title: 'Events historic',
          path: 'Events'
        }
      ]
    }
  }
}
</script>

<style scoped>
nav {
  background-color: white;
  height: 64px;
  text-transform: uppercase;
  border-bottom: 1px solid black;
}
ul {
  list-style: none;
  margin: 0 auto;
  padding: 0;
  height: 100%;
  width: 50%;
}
ul li, a {
  height: 100%;
  width: 100%;
}
ul li a {
  color: black;
  text-decoration: none;
  transition: all .3s ease-in-out;
}
ul li a:hover {
  background-color: black;
  color: white;
}
</style>
