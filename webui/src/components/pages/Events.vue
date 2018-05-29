<template>
    <div>
      <h1>Events</h1>
        <event v-for="(event, i) in events" :event="event" :key="i"></event>
    </div>
</template>

<script>
import Event from '../Event';

let events = [];
for(let i = 1; i < 21; i++) {
  events.push({
    id: i,
    status: 'int ' + i,
    replay_url: 'localhost:8080/events'+i,
    timestamp: new Date()
  })
}

export default {
  name: "Events",
  components: {
    Event
  },

  data() {
    return {
      events
    }
  },
}
</script>

<style scoped>

</style>
