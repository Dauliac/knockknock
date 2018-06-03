import config from '../../../config-api-route';
import axios from 'axios';

export default {
  state: {
    ringtones: [],
  },

  getters: {
    ringtones: state => state.ringtones
  },

  mutations: {
    loadRingtones(state, ringtones) {
      state.ringtones = ringtones;
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
    }
  }
}
