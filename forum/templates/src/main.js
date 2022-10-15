
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
// var firebase = require('firebase');
// var firebaseui = require('firebaseui');
// var ui = new firebaseui.auth.AuthUI(firebase.auth());

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs } from 'firebase/firestore/lite';
import { getAuth } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDR2t_PQX1q70m_s-66Cibs2p6OqdNeKyI",
  authDomain: "cs222-forum.firebaseapp.com",
  projectId: "cs222-forum",
  storageBucket: "cs222-forum.appspot.com",
  messagingSenderId: "75423260397",
  appId: "1:75423260397:web:02c2a985ab0f84938db6e4",
  measurementId: "G-K0FGB5W2XB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);
const analytics = getAnalytics(app);
const db = getFirestore(app);
export { app };

new Vue({
  render: h => h(App),
  router
}).$mount('#app')

