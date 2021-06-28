<template>
  <v-container>
    <AddProjectDialog
      :dialog="addProjectDialog"
      @close="closeAddProjectDialog"
      @refresh="refreshData"
    ></AddProjectDialog>
    <AddSprintDialog
      :dialog="addSprintDialog"
      @close="closeAddSprintDialog"
      @refresh="refreshData"
      ref="addSprintDialog"
    ></AddSprintDialog>
    <v-row class="mt-2">
      <h1>Список проектов</h1>
    </v-row>
    <v-row>
      <v-col col="12">
        <v-simple-table width="100%">
          <template v-slot:default>
            <thead>
              <tr>
                <td colspan="8">
                  <v-btn
                    color="black"
                    class="mt-4 mb-4"
                    block
                    @click="startProjectAdding"
                    dark
                    outlined
                  >
                    Добавить новый проект</v-btn
                  >
                </td>
              </tr>
            </thead>
            <thead>
              <tr>
                <th class="text-left">ID</th>
                <th class="text-left">Название проекта</th>
                <th class="text-left">Лидер проекта</th>
                <th class="text-left">Префикс задач</th>
                <th class="text-left">Является черновиком</th>
                <th class="text-left">Спринты</th>
                <th class="text-left">Команды</th>
                <th class="text-left">Настройки</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="project in projects"
                :key="project.id"
                class="pt-2 pb-2"
              >
                <td>{{ project.id }}</td>
                <td>{{ project.name }}</td>
                <td>
                  {{ project.leader != null ? project.leader.firstName : "-" }}
                  {{ project.leader != null ? project.leader.lastName : "-" }}
                  ({{ project.leader != null ? project.leader.username : "-" }})
                </td>
                <td>{{ project.prefix }}</td>
                <td>{{ project.draft }}</td>
                <td>
                  <div
                    v-for="(sprint, index) in project.sprintSet"
                    :key="sprint.id"
                  >
                    {{ index + 1 }}. {{ sprint.name }}
                  </div>
                  <div>
                    <v-btn
                      color="black"
                      text
                      small
                      @click="startSprintAdding(project.id)"
                      >Добавить спринт</v-btn
                    >
                  </div>
                </td>
                <td>
                  <div v-for="(team, index) in project.teams" :key="team.id">
                    {{ index + 1 }}. {{ team.name }}
                  </div>
                </td>
                <td>{{ project.settings }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AddProjectDialog from "@/components/main/projects/AddProjectDialog.vue";
import AddSprintDialog from "@/components/main/projects/AddSprintDialog.vue";

import { PROJECTS } from "@/graphql/queries.js";
export default {
  name: "ProjectsList",
  components: { AddProjectDialog, AddSprintDialog },
  apollo: {
    projects: {
      query: PROJECTS
    }
  },
  data() {
    return {
      addProjectDialog: false,
      addSprintDialog: false
    };
  },
  methods: {
    refreshData() {
      this.$apollo.queries.projects.refresh();
      this.$apollo.queries.projects.refetch();
    },
    startProjectAdding() {
      this.addProjectDialog = true;
    },
    startSprintAdding(projectId) {
      this.$refs.addSprintDialog.setProjectValue(projectId);
      this.addSprintDialog = true;
    },
    closeAddProjectDialog() {
      this.addProjectDialog = false;
    },
    closeAddSprintDialog() {
      this.addSprintDialog = false;
    }
  }
};
</script>

<style lang="scss" scoped></style>
