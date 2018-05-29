<template>
    <div>
      <div>
        <img src="http://0.0.0.0:8080/stream?width=670&height=480" alt="">
        {{ stream }}
      </div>
    </div>
</template>

<script>
export default {
  name: "Stream",

  data() {
    return {
      stream: 'streamurl'
    }
  }
}
</script>

<style scoped>

</style>
