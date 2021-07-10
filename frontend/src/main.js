import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import VueApollo from "vue-apollo";
import { ApolloClient } from "apollo-client";
import { InMemoryCache } from "apollo-cache-inmemory";
import { createHttpLink } from "apollo-link-http";
import vuetify from "./plugins/vuetify";
import Cookies from "js-cookie";
import VueYandexMetrika from "vue-yandex-metrika";

Vue.config.productionTip = false;

// Кэш Apollo (Graphql)
const cache = new InMemoryCache({
  addTypename: true
});

// Создание ссылки для Apollo
const httpLink = new createHttpLink({
  uri: "http://localhost:8000/api/graphql/"
});

// Создание websocket ссылки для Subscription
// TODO: включить
// const wsLink = new WebSocketLink({
//   uri: "ws://localhost:8000/api/graphql",
//   options: {
//     reconnect: true
//   }
// });

// Клиент Apollo
const apolloClient = new ApolloClient({
  headers: {
    "X-CSRFToken": Cookies.get("csrftoken")
  },
  link: httpLink,
  cache,
  connectToDevTools: true
});

Vue.use(VueApollo);

// Провайдер Apollo (Graphql)
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

Vue.use(VueYandexMetrika, {
  id: process.env.VUE_APP_YANDEX_METRIKA,
  env: process.env.NODE_ENV,
  router,
  options: {
    clickmap: true,
    trackLinks: true,
    accurateTrackBounce: true
  }
});

new Vue({
  router,
  store,
  apolloProvider,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
