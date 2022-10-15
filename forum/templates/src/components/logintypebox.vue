<template>
  <div class="logintypebox-container" v-bind:class="rootClassName">
    <div class="logintypebox-container1">
      <span class="logintypebox-text">{{ text1 }}</span>
      <input type="text" :placeholder="textinput_placeholder" class="input" name="email"/>
    </div>
    <div class="logintypebox-container2">
      <div class="logintypebox-container3">
        <span class="logintypebox-text1">{{ text }}</span>
      </div>
      <input
        type="text"
        :placeholder="textinput_placeholder1"
        class="logintypebox-textinput1 input"
        name="password"
      />
    </div>
  </div>
</template>

<script>
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

export default {
  name: 'Logintypebox',
  props: {
    textinput_placeholder: {
      type: String,
      default: 'email@address.com',
    },
    textinput_placeholder1: {
      type: String,
      default: 'password123',
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
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login(submitEvent) {
      this.email = submitEvent.target.elements.email.value;
      this.password = submitEvent.target.elements.password.value;
      const auth = getAuth();
      signInWithEmailAndPassword(auth, this.email, this.password)
        .then(() => {
          this.$router.push("/search");
        })
        .catch((error) => {
          const errorCode = error.code;
          const errorMessage = error.message;
          console.log(errorCode);
          console.log(errorMessage);
          let alert_1 = document.querySelector("#alert_1");
          alert_1.classList.remove("d-none");
          alert_1.innerHTML = errorMessage;
          console.log(alert_1);
        });
    },
    moveToRegister() {
      this.$router.push("/");
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
