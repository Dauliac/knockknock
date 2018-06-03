<template>
  <section>
    <img :src="streamUrl">
    <loader></loader>
  </section>
</template>

<script>
import Loader from "../Loader";
export default {
  name: "Stream",
  components: {Loader},
  data() {
    return {
      streamUrl: '127.0.0.1:8080/stream'
    }
  }
}
</script>

<style scoped>

</style>
