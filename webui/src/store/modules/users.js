
import axios from 'axios';
import config from '../../../config-api-route';

export default {
  state: {
    users: []
  },

  getters: {
    users: state => state.users,
  },


  mutations: {
    loadUsers(state, users) {
      state.users = users;
    },

    popUser (state, id) {
      state.users = state.users.filter(user => user.id != id);
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

    async removeUser ({ commit }, user) {
      try {
        const response = await axios.delete(`${config.url}users/${user.id}`);
        if (response.status === 200) {
          commit('popUser', response.data);
          return response.data;
        }
      } catch (e) {
        throw new Error('Api down.')
      }
    }
  }
}
