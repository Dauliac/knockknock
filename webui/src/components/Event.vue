<template>
  <div class="event">
    <p>{{event.id}}</p>
    <p>{{event.status}}</p>
    <p>{{event.replay_url}}</p>
    <p>{{event.timestamp}}</p>
    <button @click="replayStream()">Revoir la video</button>
  </div>
</template>

<script>
export default {
  name: "Event",

  props: ['event'],

  methods: {
    replayStream() {
      console.log("replay")
    }
  }
}
</script>

<style scoped>

</style>
