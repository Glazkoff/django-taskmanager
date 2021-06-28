import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    role: "admin"
  },
  getters: {
    isUser: (state) => {
      return state.role === "user";
    },
    isManager: (state) => {
      return state.role === "manager";
    },
    isAdmin: (state) => {
      return state.role === "admin";
    }
  },
  mutations: {},
  actions: {},
  modules: {}
});
