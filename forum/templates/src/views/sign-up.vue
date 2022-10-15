<template>
  <div class="sign-up-container">
    <app-signuptypebox
      rootClassName="signuptypebox-root-class-name"
    ></app-signuptypebox>
    <router-link to="/login" class="sign-up-navlink button">
      <span>Sign Up</span>
    </router-link>
    <router-link to="/login" class="sign-up-navlink1">Login</router-link>
  </div>
</template>

<script>
import AppSignuptypebox from '../components/signuptypebox'
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

export default {
  name: 'SignUp',
  components: {
    AppSignuptypebox,
  },
  metaInfo: {
    title: 'sign-up - Chat Forum',
    meta: [
      {
        property: 'og:title',
        content: 'sign-up - Chat Forum',
      },
    ],
  },
}
</script>

<style scoped>
.sign-up-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.sign-up-navlink {
  align-self: center;
  text-decoration: none;
}
.sign-up-navlink1 {
  align-self: center;
  padding-top: var(--dl-space-space-fourunits);
  padding-bottom: var(--dl-space-space-fourunits);
  text-decoration: underline;
}
</style>
