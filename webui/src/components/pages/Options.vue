<template>
  <div>
    <div>
      <label>Telegram token :</label>
      <input v-model="telegramToken"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "Options",

  data() {
    return {
      telegramToken: ''
    }
  }
}
</script>

<style scoped>

</style>
