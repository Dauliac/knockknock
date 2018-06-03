<template>
  <section>

    <div  v-if="isActive === false">
      <loader></loader>
      <button @click="makeActive">click</button>
    </div>
    <div v-else>
      <div class="modal" :class="{ 'is-active': isActive }">
        <div class="modal-background"></div>
        <div class="modal-content">
          <img :src="ringtonePending[0].replay_url">
          <button class="button is-success" @click="updateRingtone">Open</button>
          <button class="button is-danger" @click="updateRingtone">Close</button>
        </div>
        <button class="modal-close is-large" aria-label="close" @click="makeActive"></button>
      </div>
    </div>

  </section>
</template>

<script>
import Loader from "../Loader";
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "Stream",
  components: {
    Loader
  },
  data() {
    return {
      isActive: false
    }
  },

  mounted() {
    setInterval( () => {
      return this.$store.dispatch('getRingtonePending')
    }, 3000)
  },

  methods: {
    makeActive() {
      this.isActive = !this.isActive;
    },
    ...mapActions([
      'updateRingtone',
      'getRingtonePending'
    ]),
  },

  computed: {
    ...mapGetters([
      'ringtonePending'
    ])
  }


}
</script>

<style scoped>
</style>
