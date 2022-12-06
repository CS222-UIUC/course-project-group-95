<template>
  <nav class="notificationhead-nav" v-bind:class="rootClassName">
    <router-link to="/" class="notificationhead-text">{{ text }}</router-link>
    <router-link to="/search" class="notificationhead-navlink">
      {{ text1 }}
    </router-link>
    <span class="notificationhead-text1">{{ text2 }}</span>
    <router-link to="/profile" class="notificationhead-navlink1">
      {{ text4 }}
    </router-link>
  </nav>
</template>

<script>
export default {
  name: 'Notificationhead',
  props: {
    text2: {
      type: String,
      default: 'Notifications',
    },
    text: {
      type: String,
      default: 'Home',
    },
    text1: {
      type: String,
      default: 'Search',
    },
    text4: {
      type: String,
      default: 'Profile',
    },
    rootClassName: String,
  },
}
</script>

<style scoped>
.notificationhead-nav {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  flex-direction: row;
}
.notificationhead-text {
  color: rgba(0, 0, 0, 0.4);
  width: var(--dl-size-size-large);
  font-size: 30px;
  align-self: center;
  font-style: normal;
  transition: 0.3s;
  font-weight: 400;
  text-decoration: none;
}
.notificationhead-text:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.notificationhead-navlink {
  color: rgba(0, 0, 0, 0.4);
  width: var(--dl-size-size-large);
  font-size: 30px;
  font-style: normal;
  transition: 0.3s;
  font-weight: 400;
  margin-left: var(--dl-space-space-twounits);
  margin-right: var(--dl-space-space-unit);
  text-decoration: none;
}
.notificationhead-navlink:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.notificationhead-text1 {
  color: #000000;
  width: var(--dl-size-size-xlarge);
  font-size: 30px;
  transition: 0.3s;
  margin-left: var(--dl-space-space-twounits);
  margin-right: var(--dl-space-space-twounits);
}
.notificationhead-text1:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.notificationhead-navlink1 {
  color: rgba(0, 0, 0, 0.4);
  width: var(--dl-size-size-medium);
  font-size: 30px;
  font-style: normal;
  transition: 0.3s;
  font-weight: 400;
  margin-left: var(--dl-space-space-twounits);
  text-transform: capitalize;
  text-decoration:   none;
}
.notificationhead-navlink1:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}

@media(max-width: 767px) {
  .notificationhead-nav {
    align-items: flex-start;
    flex-direction: column;
  }
  .notificationhead-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .notificationhead-navlink {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .notificationhead-text1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .notificationhead-navlink1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .notificationhead-root-class-name {
    display: none;
  }
}
@media(max-width: 479px) {
  .notificationhead-root-class-name {
    display: none;
  }
}
</style>
