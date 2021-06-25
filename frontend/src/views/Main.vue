<template>
  <v-app id="main">
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-white">Таск-менеджер</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu transition="slide-y-transition" bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon>
            <v-icon> mdi-chevron-down </v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, i) in menuItems" :key="i" link>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <!-- <v-system-bar></v-system-bar> -->
    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="grey lighten-4" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64"></v-avatar>
        <div>Никита Глазков</div>
        <div>contact@nglazkov.ru</div>
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
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view></router-view>
      <!-- <Desk
        :statusList="statusList"
        @updateStoryPoints="updateStoryPoints($event)"
      ></Desk> -->
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
  // components: {
  //   // Desk
  // },
  apollo: {
    teams: {
      query: TEAMS_LIST
    }
  },
  data() {
    return {
      drawer: false,
      links: [
        // ["mdi-home", "Главная", "/"],
        ["mdi-bike-fast", "Доска1", "/order-delivery"],
        ["mdi-clipboard-list", "Доска2", "/orders"],
        ["mdi-alert-octagon", "Доска3", "/auth"]
      ],
      menuItems: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" }
      ]
    };
  },
  methods: {
    updateStoryPoints(upd) {
      this.statusList.forEach((status) => {
        status.tasks.forEach((task) => {
          if (task.id == upd.taskId) {
            console.log("TASK: ", task);
            task.storyPoints = upd.storyPoints;
          }
        });
      });
      console.log("!!", upd);
    },
    moveToBoard(boardId) {
      let boardPath = `/board/${boardId}`;
      if (this.$route.path !== boardPath) {
        this.$router.push(boardPath);
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
