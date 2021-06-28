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
    <v-row class="mt-2">
      <h1>Список команд</h1>
    </v-row>
    <v-row>
      <v-col col="12">
        <v-simple-table width="100%">
          <template v-slot:default>
            <thead>
              <tr>
                <td colspan="4">
                  <v-btn
                    color="black"
                    class="mt-4 mb-4"
                    block
                    @click="startTeamAdding"
                    dark
                    outlined
                  >
                    Добавить новую команду</v-btn
                  >
                </td>
              </tr>
            </thead>
            <thead>
              <tr>
                <th class="text-left">ID</th>
                <th class="text-left">Название команды</th>
                <th class="text-left">Доски</th>
                <th class="text-left">Название проекта</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in teams" :key="team.id">
                <td>{{ team.id }}</td>
                <td>{{ team.name }}</td>
                <td>
                  <div v-for="(board, index) in team.boardSet" :key="board.id">
                    <v-btn
                      color="primary"
                      class="mb-2"
                      :class="{ 'mt-2': index == 0 }"
                      :to="`/board/${board.id}`"
                      block
                      >Перейти к доске "{{ board.name }}"</v-btn
                    >
                  </div>
                  <div>
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
import { TEAMS_LIST } from "@/graphql/queries.js";

export default {
  name: "TeamsList",
  apollo: {
    teams: {
      query: TEAMS_LIST
    }
  },
  data() {
    return {
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
    }
  }
};
</script>

<style lang="scss" scoped></style>
