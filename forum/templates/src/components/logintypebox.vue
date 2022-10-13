<template>
  <div class="logintypebox-container" v-bind:class="rootClassName">
    <div class="logintypebox-container1">
      <span class="logintypebox-text">{{ text1 }}</span>
      <input type="text" :placeholder="textinput_placeholder" class="input" />
    </div>
    <div class="logintypebox-container2">
      <div class="logintypebox-container3">
        <span class="logintypebox-text1">{{ text }}</span>
      </div>
      <input
        type="text"
        :placeholder="textinput_placeholder1"
        class="logintypebox-textinput1 input"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Logintypebox',
  props: {
    textinput_placeholder: {
      type: String,
      default: 'placeholder',
    },
    textinput_placeholder1: {
      type: String,
      default: 'placeholder',
    },
    text1: {
      type: String,
      default: 'Username',
    },
    rootClassName: String,
    text: {
      type: String,
      default: 'Password',
    },
  },
}
</script>

<style scoped>
.logintypebox-container {
  width: 100%;
  height: 226px;
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.logintypebox-container1 {
  width: 100%;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.logintypebox-text {
  padding-right: var(--dl-space-space-twounits);
}
.logintypebox-container2 {
  width: 100%;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.logintypebox-container3 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.logintypebox-text1 {
  padding-right: var(--dl-space-space-twounits);
}
.logintypebox-textinput1 {
  padding-left: 12px;
  padding-right: 22px;
}

</style>
