import Vue from "vue";
import VueRouter from "vue-router";
import Main from "../views/Main.vue";
import Auth from "../views/Auth.vue";
import LogIn from "../components/auth/LogIn.vue";
import TeamsList from "../components/main/teams/TeamsList.vue";
import TeamRedirect from "../components/main/teams/TeamRedirect.vue";
import NotFound from "../components/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/auth",
    component: Auth,
    childrens: [
      {
        path: "/",
        name: "LogIn",
        component: LogIn
      }
    ]
  },
  {
    path: "/",
    component: Main,
    childrens: [
      {
        path: "/teams",
        components: TeamsList,
        children: {
          path: "/:teamId",
          component: TeamRedirect,
          children: {
            path: "/board/:boardId"
          }
        }
      }
    ]
  },

  // {
  //   path: "/team/:id",
  //   name: "Main",
  //   component: Main
  // },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/404",
    name: "404",
    component: NotFound
  },
  {
    path: "*",
    redirect: "/404"
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
