import Vue from "vue";
import VueRouter from "vue-router";
import Main from "../views/Main.vue";
import Auth from "../views/Auth.vue";
import LogIn from "../components/auth/LogIn.vue";
import TeamsList from "../components/main/teams/TeamsList.vue";
import ProjectsList from "../components/main/projects/ProjectsList.vue";
import Desk from "../components/main/boards/Desk.vue";
import ProjectDashboard from "../components/main/projects/ProjectDashboard.vue";

Vue.use(VueRouter);

const ifNotAuthenticated = (to, from, next) => {
  let role = localStorage.getItem("role");
  if (!role) {
    next();
    return;
  }
  next("/");
};

const ifAuthenticated = (to, from, next) => {
  let role = localStorage.getItem("role");
  if (role) {
    next();
    return;
  }
  next("/auth");
};

const routes = [
  {
    path: "/auth",
    component: Auth,
    beforeEnter: ifNotAuthenticated,
    children: [
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
    beforeEnter: ifAuthenticated,
    children: [
      {
        path: "/",
        component: TeamsList
      },
      {
        path: "/board/:id",
        component: Desk
      },
      {
        path: "/projects",
        component: ProjectsList
      },
      {
        path: "/dashboard/:id",
        name: "ProjectDashboard",
        component: ProjectDashboard
      }
    ]
  },
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // },
  {
    path: "/404",
    name: "404",
    component: () =>
      import(/* webpackChunkName: "notfound" */ "../components/NotFound.vue")
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
