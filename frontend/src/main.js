import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import VueApollo from "vue-apollo";
import { ApolloClient } from "apollo-client";
import { InMemoryCache } from "apollo-cache-inmemory";
import { createHttpLink } from "apollo-link-http";
import { WebSocketLink } from "apollo-link-ws";
import { getMainDefinition } from "apollo-utilities";
import { split } from "apollo-link";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

// Кэш Apollo (Graphql)
const cache = new InMemoryCache({
  addTypename: true
});

// Создание ссылки для Apollo
const httpLink = new createHttpLink({
  uri: process.env.VUE_APP_GRAPHQL_URL
});

// Создание websocket ссылки для Subscription
const wsLink = new WebSocketLink({
  uri: "ws://localhost:8000/api/graphql",
  options: {
    reconnect: true
  }
});

const link = split(
  // split based on operation type
  ({ query }) => {
    const definition = getMainDefinition(query);
    return (
      definition.kind === "OperationDefinition" &&
      definition.operation === "subscription"
    );
  },
  wsLink,
  httpLink
);

// Клиент Apollo
const apolloClient = new ApolloClient({
  link,
  cache,
  connectToDevTools: true
});

Vue.use(VueApollo);

// Провайдер Apollo (Graphql)
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

new Vue({
  router,
  store,
  apolloProvider,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
