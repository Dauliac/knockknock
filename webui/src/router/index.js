import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/pages/Home'
import Ringtones from '@/components/pages/Ringtones'
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
      path: '/ringtones',
      name: 'Ringtones',
      component: Ringtones
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
