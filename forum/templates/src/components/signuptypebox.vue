<template>
  <div class="signuptypebox-container" v-bind:class="rootClassName">
    <div class="signuptypebox-container1">
      <span class="signuptypebox-text">{{ text1 }}</span>
      <input type="text" :placeholder="textinput_placeholder" class="input" />
    </div>
    <div class="signuptypebox-container2">
      <div class="signuptypebox-container3">
        <span class="signuptypebox-text1">{{ text }}</span>
      </div>
      <input
        type="text"
        :placeholder="textinput_placeholder1"
        class="signuptypebox-textinput1 input"
      />
    </div>
  </div>
</template>

<script>
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

export default {
  name: 'Signuptypebox',
  props: {
    textinput_placeholder: {
      type: String,
      default: 'placeholder',
    },
    text: {
      type: String,
      default: 'Password',
    },
    textinput_placeholder1: {
      type: String,
      default: 'placeholder',
    },
    rootClassName: String,
    text1: {
      type: String,
      default: 'Username',
    },
  },
   data() {
    return {
      textinput_placeholder: "",
      textinput_placeholder1: "",
    };
  },
  methods: {
    register(submitEvent) {
      // data update
      this.email = submitEvent.target.elements.textinput_placeholder.value;
      this.password = submitEvent.target.elements.textinput_placeholder1.value;
      // firebase registration
      const auth = getAuth();
      createUserWithEmailAndPassword(auth, this.email, this.password)
        .then((userCredential) => {
          const user = userCredential.user;
          console.log(user);
          console.log("Registration completed");
          this.$router.push("/");
        })
        .catch((error) => {
          const errorCode = error.code;
          const errorMessage = error.message;
          console.log(errorCode);
          console.log(errorMessage);
          let alert_2 = document.querySelector("#alert_2");
          alert_2.classList.remove("d-none");
          alert_2.innerHTML = errorMessage;
          console.log(alert_2);
        });
    },
    moveToLogin() {
      this.$router.push("/");
    },
  },
}
</script>

<style scoped>
.signuptypebox-container {
  width: 100%;
  height: 226px;
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.signuptypebox-container1 {
  width: 100%;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.signuptypebox-text {
  padding-right: var(--dl-space-space-twounits);
}
.signuptypebox-container2 {
  width: 100%;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.signuptypebox-container3 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.signuptypebox-text1 {
  padding-right: var(--dl-space-space-twounits);
}
.signuptypebox-textinput1 {
  padding-left: 12px;
  padding-right: 22px;
}

</style>
