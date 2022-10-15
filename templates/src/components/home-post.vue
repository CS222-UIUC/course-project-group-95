<template>
  <div class="home-post-container" v-bind:class="rootClassName">
    <span class="home-post-text">{{ text1 }}</span>
    <span class="home-post-text1">{{ text }}</span>
  </div>
</template>

<script>
export default {
  name: 'HomePost',
  props: {
    text1: {
      type: String,
      default: 'Title',
    },
    text: {
      type: String,
      default:
        'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontent',
    },
    rootClassName: String,
  },
}
</script>

<style scoped>
.home-post-container {
  width: 100%;
  height: 118px;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.home-post-text {
  font-size: 30px;
  align-self: center;
  font-style: normal;
  font-family: Arial;
  font-weight: 700;
  padding-top: var(--dl-space-space-oneandhalfunits);
}
.home-post-text1 {
  height: auto;
  align-self: center;
  padding-top: var(--dl-space-space-unit);
}
.home-post-root-class-name {
  align-self: center;
}


</style>
