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
        <div>john@vuetifyjs.com</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-subheader>Доски</v-subheader>
        <v-list-item v-for="[icon, text] in links" :key="icon" link>
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <Desk
        :statusList="statusList"
        @updateStoryPoints="updateStoryPoints($event)"
      ></Desk>
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
import Desk from "@/components/main/boards/Desk.vue";

export default {
  name: "Main",
  components: {
    Desk
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
      ],
      statusList: [
        {
          id: 1,
          title: "Запланированно",
          tasks: [
            {
              id: 1,
              storyPoints: 1,
              body: "Купить коту еды",
              executor: 2,
              sprint: 1,
              status: 1,
              comments: []
            },
            {
              id: 2,
              storyPoints: 1,
              body: "Купить коту еды",
              executor: 2,
              sprint: 1,
              status: 1,
              comments: []
            }
          ]
        },
        {
          id: 2,
          title: "В работе",
          tasks: [
            {
              id: 3,
              storyPoints: 1,
              body: "Прикол",
              executor: 2,
              sprint: 1,
              status: 1,
              comments: []
            }
          ]
        },
        { id: 3, title: "Завершено", tasks: [] },
        { id: 4, title: "Бэклогч1", tasks: [] }
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
    }
  }
};
</script>

<style lang="scss" scoped></style>
