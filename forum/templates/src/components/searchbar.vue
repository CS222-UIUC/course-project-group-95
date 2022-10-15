<template>
  <div class="searchbar-container" v-bind:class="rootClassName">
    <input type="text" :placeholder="textinput_placeholder" class="input" />
  </div>
</template>

<script>
export default {
  name: 'Searchbar',
  props: {
    rootClassName: String,
    textinput_placeholder: {
      type: String,
      default: 'placeholder',
    },
  },
}
</script>

<style scoped>
.searchbar-container {
  width: 100%;
  height: 400px;
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}


</style>
