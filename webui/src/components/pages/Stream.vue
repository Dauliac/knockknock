<template>
  <section>
    <div  v-if="isActive === false">
      <loader></loader>
      <button @click="makeActive">click</button>
    </div>
    <div v-else>
      <div class="modal" :class="{ 'is-active': isActive }" v-if="ringtonePending.length > 0">
        <div class="modal-background"></div>
        <div class="modal-content">
          <img :src="ringtonePending[0].replay_url">
          <button class="button is-success" @click="open(ringtonePending[0])">Open</button>
          <button class="button is-danger" @click="close(ringtonePending[0])">Close</button>
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
      isActive: false,
      errorMessage: ''
    }
  },

  mounted() {
    setInterval( () => {
      this.$store.dispatch('getRingtonePending')
        .then(ringtones => {
          this.errorMessage = ''
        })
        .catch(e => {
          this.errorMessage = e.message;
          console.log(e.message)
        });
    }, 4500)
  },

  methods: {
    async open (ringtone) {
      ringtone.status = 3;
      await this.updateRingtone(ringtone);
      this.makeActive();
    },
    async close (ringtone) {
      ringtone.status = 4;
      await this.udpateRingtone(ringtone);
      this.makeActive();
    },
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
