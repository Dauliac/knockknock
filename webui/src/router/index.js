import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/pages/Home'
import Login from '@/components/pages/Login'
import Rings from '@/components/pages/Rings'
import Stream from '@/components/pages/Stream'
import Options from '@/components/pages/Options'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/rings',
      name: 'Rings',
      component: Rings
    },
    {
      path: '/stream',
      name: 'Stream',
      component: Stream
    },
    {
      path: '/options',
      name: 'Options',
      component: Options
    }
  ]
})
