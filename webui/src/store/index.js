/*
 * Author      : github.com/TonyChG
 * Date        : Tue 29 May 2018 12:28:19 PM CEST
 * Description :
**/

import Vue from 'vue'
import Vuex from 'vuex';
import configApi from "../../config-api-route";
import axios from 'axios';
import usersStore from './modules/users';
import localstore from 'store';

Vue.use(Vuex);

export default () => {
  return new Vuex.Store({
    modules: {
      usersStore
    },
    state: {
      isAuthenticated: false,
      userMail: '',
      userToken: '',
      errors: [],
    },
    getters: {
      isAuthenticated: state => state.isAuthenticated,
      userMail: state => state.userMail,
      userToken: state => state.userToken,
    },
    mutations: {
      TOKEN_CHANGED(state, token) {
        state.userToken = token;
        state.isAuthenticated = true;
      }
    },
    actions: {
      async checkAuth ({ commit, state }) {
        try {
          const token = localstore.get(configApi.tokenName);
          if (token) {
            commit('TOKEN_CHANGED', token);
          }
        } catch (e) {
          throw new Error('Unauthenticated.');
        }
      },
      login ({ commit, state }, user) {
        const params = new URLSearchParams();

        params.append('email', user.mail);
        params.append('password', user.password);

        axios.post(configApi.url + 'login', params)
          .then( res => {
            console.log(res);
            state.userMail = user.mail;
            localstore.set(configApi.tokenName, res.data.token);
            commit('TOKEN_CHANGED', res.data.token);
          })
          .catch(err => {
            console.log(err);
            state.errors.push(err.message);
            console.log(state.errors)
          })
      },
      deleteUser(user) {
        axios.delete(configApi.url + `users/${user.id}`)
          .then(res => console.log(res))
          .catch(err => console.error(err))
      }
    }
  });
}
