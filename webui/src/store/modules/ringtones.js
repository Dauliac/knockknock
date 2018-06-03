import config from '../../../config-api-route';
import axios from 'axios';

export default {
  state: {
    ringtones: [],
    ringtonePending: []
  },

  getters: {
    ringtones: state => state.ringtones,
    ringtonePending: state => state.ringtonePending
  },

  mutations: {
    loadRingtones(state, ringtones) {
      state.ringtones = ringtones;
    },
    popRingtone(state, id) {
      state.ringtones = state.ringtones.filter(r => r.id !== id);
    },
    pendingRingtone(state, ringtone) {
      state.ringtonePending = ringtone;
    }
  },

  actions: {
    async getRingtones({commit}) {
      try {
        const res = await axios.get(`${config.url}ringtones`);
        if (res.status === 200) {
          commit('loadRingtones', res.data);
          return res.data;
        }
      }
      catch (e) {
        throw new Error('Api down');
      }
    },
    async removeRingtone({ commit }, id) {
      try {
        const res = await axios.delete(`${config.url}ringtones/${id}`);
        if (res.status === 200) {
          commit('popRingtone', id);
          return res.status;
        }
      } catch (e) {
        throw new Error('Api down');
      }
    },
    async updateRingtone({ commit, state }) {
      const id = state.ringtonePending[0].id;
      try {
        const params = new URLSearchParams();
        params.append('status', 3);
        const res = await axios.put(`${config.url}ringtones/${id}`, params);
        if (res.status === 200) {
          commit('loadRingtones');
        }
      }
      catch (e) {
        throw new Error('Api down');
      }
    },
    async getRingtonePending({ commit }) {
      try {
        const res = await axios.get(`${config.url}ringtones/pending`);
        commit('pendingRingtone', res.data);
        console.log(res.data)
      }
      catch (e) {
        throw new Error('Api down');
      }
    }
  }
}
