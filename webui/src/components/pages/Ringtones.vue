<template>
    <section class="container">
      <div class="columns">
        <div class="column is-one-third">
          <div class="card">
            <div class="card-content">
              <p class="title">
                ringtone
              </p>
              <p class="subtitle">
                date
              </p>
            </div>
            <footer class="card-footer">
              <p class="card-footer-item">
                <span>
                  REVIEW
                </span>
              </p>
              <p class="card-footer-item">
                <span>
                  DELETE
                </span>
              </p>
            </footer>
          </div>
        </div>
      </div>
    </section>
</template>

<script>
import { mapGetters,  } from 'vuex';
export default {
  name: "Ringtones",

  mounted() {
    this.$store.dispatch('getRingtones');
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
