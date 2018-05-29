import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueSocketIo from 'vue-socket.io'
import socketio from 'socket.io-client'
import { url } from './config'

Vue.use(VueSocketIo, socketio(url), store);

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
