<template>
  <div class="profilebasic-information-container" v-bind:class="rootClassName">
    <span>{{ text }}</span>
    <span>{{ text1 }}</span>
    <span>{{ text2 }}</span>
  </div>
</template>

<script>
export default {
  name: 'ProfilebasicInformation',
  props: {
    text: {
      type: String,
      default: 'Name',
    },
    rootClassName: String,
    text1: {
      type: String,
      default: 'Join Date',
    },
    text2: {
      type: String,
      default: 'Authority',
    },
  },
}
</script>

<style scoped>
.profilebasic-information-container {
  width: 100%;
  height: 400px;
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

</style>
