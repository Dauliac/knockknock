<template>
    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-one-third" v-for="ring in ringtones" :key="ring.id">
            <div class="card">
              <div class="card-content">
                <p class="title">
                  <a class="link" :href="ring.replay_url">
                    {{ ring.id }}
                  </a>
                </p>
                <p class="subtitle">
                  {{ ring.timestamp }}
                </p>
              </div>
              <footer class="card-footer">
                <p class="card-footer-item">
                  <span>
                    {{ statuts }}
                  </span>
                </p>
                <p class="card-footer-item">
                  <a class="button is-danger" @click="removeRingtone(ring.id)">
                    Delete
                  </a>
                </p>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "Ringtones",

  async mounted() {
    await this.getRingtones();
  },

  methods: {
    ...mapActions([
      'updateRingtone',
      'removeRingtone',
      'getRingtones'
    ])
  },

  computed: {
    ...mapGetters([
      'ringtones'
    ])
  }

}
</script>

<style scoped>
.columns {
  flex-wrap: wrap;
}
</style>
