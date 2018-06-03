import axios from 'axios';
import config from '../../../config-api-route';

export default {
  state: {
    users: [],
    userId: null
  },

  getters: {
    users: state => state.users,
    userId: state => state.userId
  },


  mutations: {
    addUser (state, user) {
      state.users.push(user);
    },

    loadUsers(state, users) {
      state.users = users;
    },

    popUser (state, id) {
      state.users = state.users.filter(user => user.id != id);
    },
    changeId(state, user) {
      state.userId = user.id;
    }
  },

  actions: {
    async getUsers ({ commit }) {
      try {
        const response = await axios.get(`${config.url}users`);
        if (response.status === 200) {
          commit('loadUsers', response.data);
          return response.data;
        }
      } catch (e) {
        throw new Error('Api down.')
      }
    },

    async postUser ({ commit }, user) {
      try {
        const params = new URLSearchParams();
        params.append('email', user.mail);
        params.append('password', user.password);
        if (user.password !== '' && user.mail !== '') {
          const response = await axios.post(`${config.url}users/create`, params);
          if (response.status === 200) {
            commit('addUser', response.data);
            return response.data;
          }
        }
      } catch (e) {
        throw new Error('Api down.')
      }
    },

    async updateUser ({ commit, state }, user) {
      try {
        const params = new URLSearchParams();
        params.append('email', user.mail);
        const response = await axios.put(`${config.url}users/${state.userId}`, params);
        if (response.status === 200) {
          return response.data;
        }
      } catch (e) {
        throw new Error('Api down.')
      }
    },

    async removeUser ({ commit }, user) {
      try {
        const response = await axios.delete(`${config.url}users/${user.id}`);
        if (response.status === 200) {
          commit('popUser', user.id);
          return response.data;
        }
      } catch (e) {
        throw new Error('Api down.')
      }
    }
  }
}
