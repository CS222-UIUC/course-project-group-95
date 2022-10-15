import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import Login from './views/login'
import Search from './views/search'
import Home from './views/home'
import SignUp from './views/sign-up'
import Profile from './views/profile'
import Notification from './views/notification'
import './style.css'

import { getAuth } from "firebase/auth";

Vue.use(Router)
Vue.use(Meta)

const routes = [
  {
    name: 'login',
    path: '/login',
    component: Login,
  },
  {
    name: 'Search',
    path: '/search',
    component: Search,
  },
  {
    name: 'Home',
    path: '/',
    component: Home,
  },
  {
    name: 'sign-up',
    path: '/sign-up',
    component: SignUp,
  },
  {
    name: 'Profile',
    path: '/profile',
    component: Profile,
  },
  {
    name: 'Notification',
    path: '/notification',
    component: Notification,
  }
];

const router = new Router({
  mode: 'history',
  routes,
});

// manage page access
router.beforeEach((to, from, next) => {
  const auth = getAuth();

  if (to.matched.some((record) => record.meta.authRequired)) {
    if (auth.currentUser) {
      next();
    } else {
      alert("You've must been logged to access this area");
      router.push("/");
    }
  } else {
    next();
  }
});

export default router;