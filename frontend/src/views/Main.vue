<template>
  <v-app id="main">
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer" v-if="canBeDrawer">
      </v-app-bar-nav-icon>
      <v-toolbar-title class="text-white">Таск-менеджер</v-toolbar-title>
      <v-btn text link class="ml-4 d-none d-sm-flex" to="/">
        Список команд</v-btn
      >
      <v-btn text link class="ml-2 d-none d-sm-flex" to="/projects">
        Список проектов</v-btn
      >
      <v-spacer></v-spacer>
      <v-menu transition="slide-y-transition" bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon>
            <v-icon> mdi-chevron-down </v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, i) in menuItems" :key="i" link>
            <v-list-item-title @click="updateRoute(item.to)">{{
              item.title
            }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" app v-if="canBeDrawer">
      <v-sheet color="grey lighten-4" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64"></v-avatar>
        <div>{{ name }}</div>
        <div>{{ name }}</div>
      </v-sheet>
      <v-divider></v-divider>
      <v-list v-for="team in teams" :key="team.id">
        <v-subheader>{{ team.name }}</v-subheader>
        <v-list-item v-for="board in team.boardSet" :key="board.id" link>
          <v-list-item-icon>
            <v-icon>mdi-heart</v-icon>
          </v-list-item-icon>
          <v-list-item-content @click="moveToBoard(board.id)">
            <v-list-item-title>{{ board.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="team.boardSet.length == 0">
          <v-list-item-title class="text--grey">
            <small>В этой команде<br />досок ещё нет</small>
          </v-list-item-title>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list color="white" dense style="position: sticky; bottom: 0; left: 0">
        <v-list-item link @click="moveToMain">
          <v-list-item-icon>
            <v-icon>mdi-arrow-left</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Назад</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view @openMenu="drawer = true"></router-view>
    </v-main>
    <v-footer>
      <v-card-text class="py-2 text-center">
        {{ new Date().getFullYear() }} —
        <strong>Глазков Никита, 181-321</strong>
      </v-card-text>
    </v-footer>
  </v-app>
</template>

<script>
import { TEAMS_LIST } from "@/graphql/queries.js";

export default {
  name: "Main",
  apollo: {
    teams: {
      query: TEAMS_LIST
    }
  },
  data() {
    return {
      drawer: false,
      menuItems: [
        {
          title: "Список команд",
          to: "/"
        },
        {
          title: "Список проектов",
          to: "/projects"
        },
        {
          title: "Выйти",
          to: "logout"
        }
      ]
    };
  },
  computed: {
    canBeDrawer() {
      return (
        this.$route.path != "/" &&
        this.$route.path != "/projects" &&
        this.$route.name != "ProjectDashboard"
      );
    },
    name() {
      let user = localStorage.getItem("user");
      if (user) {
        let parseUsr = JSON.parse(user);
        return parseUsr.user.firstName + parseUsr.user.lastName;
      } else return "-";
    },
    username() {
      let user = localStorage.getItem("user");
      if (user) {
        let parseUsr = JSON.parse(user);
        return parseUsr.user.username;
      } else return "-";
    }
  },
  methods: {
    updateRoute(to) {
      if (to == "logout") {
        localStorage.clear("user");
        localStorage.clear("role");
        localStorage.clear("isAuthorized");
        this.$router.push("/auth");
      } else {
        if (this.$route.path !== to) {
          this.$router.push(to);
        }
      }
    },
    updateStoryPoints(upd) {
      this.statusList.forEach((status) => {
        status.tasks.forEach((task) => {
          if (task.id == upd.taskId) {
            task.storyPoints = upd.storyPoints;
          }
        });
      });
    },
    moveToBoard(boardId) {
      let boardPath = `/board/${boardId}`;
      if (this.$route.path !== boardPath) {
        this.$router.push(boardPath);
      }
    },
    moveToMain() {
      if (this.$route.path !== "/") {
        this.$router.push("/");
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
