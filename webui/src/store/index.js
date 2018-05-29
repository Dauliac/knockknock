/*
 * Author      : github.com/TonyChG
 * Date        : Tue 29 May 2018 12:28:19 PM CEST
 * Description :
**/

import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex)

export default () => {
  return new Vuex.Store({
      state: {
        isAuthenticated: false
      },
      getters: {
        isAuthenticated: state => state.isAuthenticated
      },
      mutations: {
      },
      actions: {
        login ({ state }, user) {
          console.log(user);
          console.log(`${state.isAuthenticated}`);
          state.isAuthenticated = !state.isAuthenticated;
        }
      }
    });
}
