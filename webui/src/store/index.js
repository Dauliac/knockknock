/*
 * Author      : github.com/TonyChG
 * Date        : Tue 29 May 2018 12:28:19 PM CEST
 * Description :
**/

import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default () => {
  return new Vuex.Store({
    state: {
      isAuthenticated: false,
      userMail: '',
      userToken: '',
    },
    getters: {
      isAuthenticated: state => state.isAuthenticated,
      userMail: state => state.userMail,
      userToken: state => state.userToken
    },
    actions: {
      login ({ state,vu }) {
        state.isAuthenticated = !state.isAuthenticated;
        state.userMail = user.mail;
        state.userToken = user.token;
        console.log(state);
      },

      connected ({ state }, { userMail, userToken }) {
        state.userMail = userMail;
        state.userToken = userToken;
      }
    }
  });
}
