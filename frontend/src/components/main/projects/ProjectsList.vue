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
      <v-text-field label="Поиск проекта" outlined v-model="projectsSearch">
        <v-icon slot="append" color="black"> mdi-magnify </v-icon>
      </v-text-field>
    </v-row>
    <v-row class="mt-2">
      <h1>Список проектов</h1>
    </v-row>
    <v-row>
      <v-col col="12">
        <v-simple-table width="100%">
          <template v-slot:default>
            <thead>
              <tr>
                <td colspan="9">
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
                <th class="text-left">Дашборд</th>
                <th class="text-left"></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="project in filteredProjectsArr"
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
                      >Добавить<br />спринт</v-btn
                    >
                  </div>
                </td>
                <td>
                  <div v-for="(team, index) in project.teams" :key="team.id">
                    {{ index + 1 }}. {{ team.name }}
                  </div>
                </td>
                <td>
                  <v-btn dark color="black" @click="goToDashBoard(project.id)"
                    >Перейти к дашборду</v-btn
                  >
                </td>
                <td>
                  <v-btn color="black" icon @click="deleteProject(project.id)">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </td>
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

import { PROJECTS, DELETE_PROJECT } from "@/graphql/queries.js";
export default {
  name: "ProjectsList",
  components: { AddProjectDialog, AddSprintDialog },
  apollo: {
    projects: {
      query: PROJECTS
    }
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      vm.refreshData();
    });
  },
  data() {
    return {
      addProjectDialog: false,
      addSprintDialog: false,
      projectsSearch: ""
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
    },
    goToDashBoard(projectId) {
      this.$router.push({
        name: "ProjectDashboard",
        params: { id: projectId }
      });
    },
    deleteProject(projectId) {
      this.$apollo
        .mutate({
          mutation: DELETE_PROJECT,
          variables: {
            projectId
          }
        })
        .then(() => {
          this.refreshData();
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  computed: {
    filteredProjectsArr() {
      let projects = this.projects;
      if (projects !== undefined) {
        projects = projects.filter((el) => {
          let findIndexName = el.name
            .toLowerCase()
            .indexOf(this.projectsSearch.toLowerCase());
          let findIndexPrefix = el.prefix
            .toLowerCase()
            .indexOf(this.projectsSearch.toLowerCase());
          return findIndexName !== -1 || findIndexPrefix !== -1;
        });
      }
      return projects;
    }
  }
};
</script>

<style lang="scss" scoped></style>
