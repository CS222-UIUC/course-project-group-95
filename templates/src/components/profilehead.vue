<template>
  <nav class="profilehead-nav" v-bind:class="rootClassName">
    <router-link to="/" class="profilehead-text">{{ text }}</router-link>
    <router-link to="/search" class="profilehead-navlink">
      {{ text1 }}
    </router-link>
    <router-link to="/notification" class="profilehead-navlink1">
      {{ text2 }}
    </router-link>
    <span class="profilehead-text1">{{ text4 }}</span>
  </nav>
</template>

<script>
export default {
  name: 'Profilehead',
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
.profilehead-nav {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  flex-direction: row;
}
.profilehead-text {
  color: rgba(0, 0, 0, 0.4);
  width: var(--dl-size-size-large);
  font-size: 30px;
  align-self: center;
  font-style: normal;
  transition: 0.3s;
  font-weight: 400;
  text-decoration: none;
}
.profilehead-text:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.profilehead-navlink {
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
.profilehead-navlink:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.profilehead-navlink1 {
  color: rgba(0, 0, 0, 0.4);
  width: var(--dl-size-size-xlarge);
  font-size: 30px;
  transition: 0.3s;
  margin-left: var(--dl-space-space-twounits);
  margin-right: var(--dl-space-space-twounits);
  text-decoration: none;
}
.profilehead-navlink1:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.profilehead-text1 {
  color: #000000;
  width: var(--dl-size-size-medium);
  font-size: 30px;
  font-style: normal;
  transition: 0.3s;
  font-weight: 400;
  margin-left: var(--dl-space-space-twounits);
  text-transform: capitalize;
}
.profilehead-text1:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}

@media(max-width: 767px) {
  .profilehead-nav {
    align-items: flex-start;
    flex-direction: column;
  }
  .profilehead-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .profilehead-navlink {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .profilehead-navlink1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .profilehead-text1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .profilehead-root-class-name {
    display: none;
  }
}
@media(max-width: 479px) {
  .profilehead-root-class-name {
    display: none;
  }
}
</style>
