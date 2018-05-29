<template>
    <div>
      <h1>Events</h1>
      <div v-for="(event, i) in events" :key="i">
        <p>{{event.id}}</p>
        <p>{{event.status}}</p>
        <p>{{event.replay_url}}</p>
        <p>{{event.timestamp}}</p>
      </div>
    </div>
</template>

<script>
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

  data() {
    return {
      events
    }
  }
}
</script>

<style scoped>

</style>
