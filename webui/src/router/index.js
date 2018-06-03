import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/pages/Home'
import Events from '@/components/pages/Events'
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
      path: '/events',
      name: 'Events',
      component: Events
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
    },
  ]
})
