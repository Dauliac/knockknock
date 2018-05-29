<template>
    <header>
      <nav>
        <ul>
          <li v-for="(link, i) in links" :key="i">
            <router-link :to="{ name: link.path}">{{ link.title }}</router-link>
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
  margin: 0;
  padding: 0;
  height: 100%;
  width: 80%;
}
ul li {
  height: 100%;
  width: 100%;
}
</style>
