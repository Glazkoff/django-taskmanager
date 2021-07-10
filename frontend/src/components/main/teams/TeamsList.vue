<template>
  <v-container>
    <AddDeskDialog
      @close="closeAddDeskDialog"
      @refresh="refreshData"
      :dialog="addDeskDialog"
      ref="addDeskDialog"
    ></AddDeskDialog>
    <AddTeamDialog
      @close="closeAddTeamDialog"
      @refresh="refreshData"
      :dialog="addTeamDialog"
    ></AddTeamDialog>
    <v-row class="mt-2 mb-2">
      <v-col>
        <h1>Список команд</h1>
      </v-col>
    </v-row>
    <v-row class="mt-2">
      <v-col>
        <span class="mr-2">Фильтровать команды проектов:</span>
        <v-btn
          color="black"
          class="mr-2"
          v-for="project in projectsToChoose"
          :key="project.id"
          outlined
          @click="chosenFilterArr.push(project.id)"
        >
          {{ project.name }}
        </v-btn>
      </v-col>
    </v-row>
    <br />
    <v-divider></v-divider>
    <v-row class="mt-2">
      <v-col>
        <span class="mr-2">Список отфильтрован по проектам:</span>
        <v-chip
          v-for="project in projectsChosen"
          :key="project.id"
          class="ma-2"
          close
          @click:close="deleteFromFilter(project.id)"
        >
          {{ project.name }}
        </v-chip>
      </v-col>
    </v-row>
    <v-row>
      <v-col col="12">
        <v-btn
          color="black"
          class="mt-4 mb-4"
          block
          @click="startTeamAdding"
          dark
          outlined
        >
          Добавить новую команду
        </v-btn>
        <v-simple-table width="100%">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">ID</th>
                <th class="text-left">Название команды</th>
                <th class="text-left">Доски</th>
                <th class="text-left">Название проекта</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in filteredTeams" :key="team.id">
                <td>{{ team.id }}</td>
                <td>{{ team.name }}</td>
                <td>
                  <div v-for="(board, index) in team.boardSet" :key="board.id">
                    <v-btn
                      color="black"
                      dark
                      class="mb-2"
                      :class="{ 'mt-2': index == 0 }"
                      :to="`/board/${board.id}`"
                      block
                      >Перейти к доске "{{ board.name }}"</v-btn
                    >
                  </div>
                  <div v-if="isManagerOrAdmin">
                    <v-btn
                      dark
                      color="black"
                      class="mb-2"
                      block
                      :class="{ 'mt-2': team.boardSet.length == 0 }"
                      @click="startDeskAdding(team.id)"
                      outlined
                      >Добавить новую доску</v-btn
                    >
                  </div>
                </td>
                <td>{{ team.project.name }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AddTeamDialog from "@/components/main/teams/AddTeamDialog.vue";
import AddDeskDialog from "@/components/main/teams/AddDeskDialog.vue";
import { TEAMS_LIST, PROJECTS } from "@/graphql/queries.js";

export default {
  name: "TeamsList",
  apollo: {
    teams: {
      query: TEAMS_LIST
    },
    projects: {
      query: PROJECTS
    }
  },
  computed: {
    isManagerOrAdmin() {
      return this.$store.getters.isManager || this.$store.getters.isAdmin;
    },
    projectsToChoose() {
      if (this.projects != undefined) {
        return this.projects.filter((el) => {
          let findIndex = this.chosenFilterArr.findIndex(
            (element) => element == el.id
          );
          return findIndex == -1;
        });
      } else {
        return this.projects;
      }
    },
    projectsChosen() {
      if (this.projects != undefined) {
        return this.projects.filter((el) => {
          let findIndex = this.chosenFilterArr.findIndex(
            (element) => element == el.id
          );
          return findIndex !== -1;
        });
      } else {
        return this.projects;
      }
    },
    filteredTeams() {
      let teams = this.teams;
      if (teams !== undefined) {
        if (this.chosenFilterArr.length !== 0) {
          return teams.filter((el) => {
            let findIndex = this.chosenFilterArr.findIndex(
              (element) => element == el.project.id
            );
            return findIndex !== -1;
          });
        } else {
          return teams;
        }
      }
      return teams;
    }
  },
  data() {
    return {
      chosenFilterArr: [],
      addDeskDialog: false,
      addTeamDialog: false
    };
  },
  components: {
    AddDeskDialog,
    AddTeamDialog
  },
  methods: {
    startTeamAdding() {
      this.addTeamDialog = true;
    },
    startDeskAdding(teamId) {
      this.$refs.addDeskDialog.setTeamValue(teamId);
      this.addDeskDialog = true;
    },
    closeAddDeskDialog() {
      this.addDeskDialog = false;
    },
    closeAddTeamDialog() {
      this.addTeamDialog = false;
    },
    refreshData() {
      this.$apollo.queries.teams.refresh();
      this.$apollo.queries.teams.refetch();
    },
    deleteFromFilter(projectId) {
      let index = this.chosenFilterArr.findIndex((el) => el == projectId);
      if (index != -1) {
        this.chosenFilterArr.splice(index, 1);
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
