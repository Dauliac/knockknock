import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueSocketIo from 'vue-socket.io'
import { url } from './config'

Vue.use(VueSocketIo, 'http://0.0.0.0:5000', store);
Vue.config.productionTip = false;

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
