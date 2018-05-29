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

</style>
