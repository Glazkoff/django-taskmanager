import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    role: localStorage.getItem("role") || null
  },
  getters: {
    isUser: (state) => {
      return state.role === "USER";
    },
    isManager: (state) => {
      return state.role === "MANAGER";
    },
    isAdmin: (state) => {
      return state.role === "ADMIN";
    }
  },
  mutations: {
    SET_ROLE: (state, role) => {
      state.role = role;
    }
  },
  actions: {},
  modules: {}
});
