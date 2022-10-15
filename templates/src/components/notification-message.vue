<template>
  <div class="notification-message-container" v-bind:class="rootClassName">
    <div class="notification-message-container1">
      <span>{{ text1 }}</span>
      <span class="notification-message-text1">Date</span>
    </div>
    <span>{{ text2 }}</span>
  </div>
</template>

<script>
export default {
  name: 'NotificationMessage',
  props: {
    text2: {
      type: String,
      default: 'asdkklasjda;skljdkas;djaskldja;ldjasjd;asjdas;kdsadas;',
    },
    rootClassName: String,
    text: {
      type: String,
      default:
        'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontent',
    },
    text1: {
      type: String,
      default: 'User Name',
    },
  },
}
</script>

<style scoped>
.notification-message-container {
  width: 100%;
  height: 116px;
  display: flex;
  position: relative;
  align-items: flex-start;
  padding-top: 40px;
  padding-left: 270px;
  padding-right: 270px;
  flex-direction: column;
  justify-content: flex-start;
}
.notification-message-container1 {
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.notification-message-text1 {
  color: var(--dl-color-gray-black);
  font-style: normal;
  font-weight: 500;
}
.notification-message-root-class-name {
  width: 100%;
  height: 100%;
}
.notification-message-root-class-name1 {
  width: 100%;
  height: 100%;
}
.notification-message-root-class-name2 {
  width: 100%;
  height: 100%;
}
@media(max-width: 479px) {
  .notification-message-container1 {
    padding-left: 0px;
    padding-right: 0px;
  }
  .notification-message-text1 {
    width: auto;
  }
}
</style>
