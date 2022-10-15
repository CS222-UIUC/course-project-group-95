<template>
  <div class="login-container">
    <app-logintypebox
      rootClassName="logintypebox-root-class-name"
    ></app-logintypebox>
    <router-link to="/" class="login-navlink button">
      <span>
        <span>Login</span>
        <br />
      </span>
    </router-link>
    <router-link to="/sign-up" class="login-navlink1">
      <span class="login-text3">Sign Up</span>
      <br />
    </router-link>
  </div>
</template>

<script>
import AppLogintypebox from '../components/logintypebox'

export default {
  name: 'Login',
  components: {
    AppLogintypebox,
  },
  metaInfo: {
    title: 'login - Chat Forum',
    meta: [
      {
        property: 'og:title',
        content: 'login - Chat Forum',
      },
    ],
  },
}
</script>

<style scoped>
.login-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: flex-end;
  flex-direction: column;
  justify-content: center;
}
.login-navlink {
  align-self: center;
  text-decoration: none;
}
.login-navlink1 {
  align-self: center;
  padding-top: var(--dl-space-space-fourunits);
  padding-bottom: var(--dl-space-space-fourunits);
  text-decoration: none;
}
.login-text3 {
  text-decoration: underline;
}
</style>
