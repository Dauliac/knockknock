/*
 * Author      : github.com/TonyChG
 * Date        : Tue 29 May 2018 12:28:19 PM CEST
 * Description :
**/

import Vue from 'vue'
import Vuex from 'vuex';
import configApi from "../../config-api-route";
import axios from 'axios';
import qs from 'qs';

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
      userToken: state => state.userToken,
    },
    mutations: {

    },
    actions: {
      login ({ state }, user) {
        // state.isAuthenticated = !state.isAuthenticated;
        // state.userMail = user.mail;
        // state.userToken = user.token;
        axios.post(configApi.url + 'login', qs.stringify({user}))
          .then( res => {
            console.log(res)
          })
          .catch(err => console.log(err))
      },
      connected ({ state }, { userMail, userToken }) {
        state.userMail = userMail;
        state.userToken = userToken;
      }
    }
  });
}
