<template>
    <header>
      <nav class="navbar is-black">
        <div class="container">
          <div class="navbar-brand">
          <span class="navbar-item">
            KnockKnock
          </span>
            <div class="navbar-burger burger" data-target="navbar">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>

          <div id="navbar" class="navbar-menu">
            <div class="navbar-start">
              <router-link class="navbar-item" v-for="(link, i) in links" :key="i" :to="{ name: link.path}">{{ link.title }}</router-link>
            </div>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <div class="field is-grouped">
                <p class="control">
                  <a class="button is-primary" href="https://github.com/jgthms/bulma/releases/download/0.7.1/bulma-0.7.1.zip">
              <span class="icon">
                <i class="fas fa-download"></i>
              </span>
                    <span>Deconnexion</span>
                  </a>
                </p>
              </div>
            </div>
          </div>
        </div>
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
          title: 'Stream',
          path: 'Stream'
        },
        {
          title: 'Options',
          path: 'Options'
        },
        {
          title: 'Ringtones history',
          path: 'Ringtones'
        }
      ]
    }
  }
}
</script>

<style scoped>
</style>
