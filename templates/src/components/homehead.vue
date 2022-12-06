<template>
  <nav class="homehead-nav" v-bind:class="rootClassName">
    <router-link to="/" class="homehead-text">{{ text }}</router-link>
    <router-link to="/search" class="homehead-navlink">{{ text1 }}</router-link>
    <router-link to="/notification" class="homehead-navlink1">
      {{ text2 }}
    </router-link>
    <router-link to="/profile" class="homehead-navlink2">{{ text4 }}</router-link>
  </nav>
</template>

<script>
export default {
  name: 'Homehead',
  props: {
    new_prop: {
      default: () => {},
    },
    text4: {
      type: String,
      default: 'Profile',
    },
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
    rootClassName: String,
  },
}
</script>

<style scoped>
.homehead-nav {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  flex-direction: row;
}
.homehead-text {
  color: #000000;
  width: var(--dl-size-size-large);
  font-size: 30px;
  align-self: center;
  font-style: normal;
  transition: 0.3s;
  font-weight: 400;
  text-decoration: none;
}
.homehead-text:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.homehead-navlink {
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
.homehead-navlink:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.homehead-navlink1 {
  color: rgba(0, 0, 0, 0.4);
  width: var(--dl-size-size-xlarge);
  font-size: 30px;
  transition: 0.3s;
  margin-left: var(--dl-space-space-twounits);
  margin-right: var(--dl-space-space-twounits);
  text-decoration: none;
}
.homehead-navlink1:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}
.homehead-navlink2 {
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
.homehead-navlink2:hover {
  color: #000000;
  font-style: normal;
  font-weight: 500;
}


























@media(max-width: 767px) {
  .homehead-nav {
    align-items: flex-start;
    flex-direction: column;
  }
  .homehead-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .homehead-navlink {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .homehead-navlink1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .homehead-navlink2 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .homehead-root-class-name16 {
    display: none;
  }
  .homehead-root-class-name18 {
    display: none;
  }
  .homehead-root-class-name24 {
    display: none;
  }
  .homehead-root-class-name26 {
    display: none;
  }
}
@media(max-width: 479px) {
  .homehead-root-class-name16 {
    display: none;
  }
  .homehead-root-class-name18 {
    display: none;
  }
  .homehead-root-class-name24 {
    display: none;
  }
  .homehead-root-class-name26 {
    display: none;
  }
}
</style>
