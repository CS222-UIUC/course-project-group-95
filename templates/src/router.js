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

Vue.use(Router)
Vue.use(Meta)
export default new Router({
  mode: 'history',
  routes: [
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
    },
  ],
})
