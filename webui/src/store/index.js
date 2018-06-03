/*
 * Author      : github.com/TonyChG
 * Date        : Tue 29 May 2018 12:28:19 PM CEST
 * Description :
**/

import Vue from 'vue'
import Vuex from 'vuex';
import configApi from "../../config-api-route";
import axios from 'axios';

Vue.use(Vuex);

export default () => {
  return new Vuex.Store({
    state: {
      isAuthenticated: false,
      userMail: '',
      userToken: '',
      errors: []
    },
    getters: {
      isAuthenticated: state => state.isAuthenticated,
      userMail: state => state.userMail,
      userToken: state => state.userToken,
    },
    mutations: {
      TOKEN_CHANGED(state, payload) {
        state.userToken = payload;
        state.isAuthenticated = true;
      }
    },
    actions: {
      login ({ commit, state }, user) {
        // state.isAuthenticated = !state.isAuthenticated;
        // state.userMail = user.mail;
        // state.userToken = user.token;
        const params = new URLSearchParams();
        params.append('email', user.mail);
        params.append('password', user.password);
        axios.post(configApi.url + 'login', params)
          .then( res => {
            console.log(res);
            state.userMail = user.mail;
            commit('TOKEN_CHANGED', res.data.token);
          })
          .catch(err => {
            console.log(err);
            state.errors.push(err.message);
            console.log(state.errors)
          })
      },
      // connected ({ state }, { userMail, userToken }) {
      //   state.userMail = userMail;
      //   state.userToken = userToken;
      // }
    }
  });
}
