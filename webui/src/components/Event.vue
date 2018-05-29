<template>
  <div class="container">
    <div class="event">
    <h1>{{event.id}}</h1>
    <p>{{event.status}}</p>
    <p>{{event.replay_url}}</p>
    <p>{{event.timestamp}}</p>
    <button @click="replayStream()" class="btn">Revoir la video</button>
    </div>
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
.btn{
    margin-top:2%;
    width: 50%;
    height: 50%;
    border: 0;
    background-color: black;
    color:white;
    border-radius: 0.3em;
    font-family: 'Anton', sans-serif;
  }
  .btn:focus{
    background-color: red;
  }
.container{
    margin: auto;
    height:13em;
    width: 50%;
    border: 0px solid grey;
    box-shadow: 1px 1px 5px grey;
    border-radius: .3em;
  }
</style>
