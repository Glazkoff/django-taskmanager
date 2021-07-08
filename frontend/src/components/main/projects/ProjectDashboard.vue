<template>
  <v-container class="dashboard" fill-height>
    <v-layout>
      <v-flex>
        <v-row>
          <v-col>
            <h1 class="mb-2">Дашборд проекта #{{ projectId }}</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" xs="12" sm="6" md="6" lg="4">
            <v-card class="pa-2" height="100%">
              <h5 class="text-center">
                Данные о количестве задач<br />по всем доскам в командах
              </h5>
              <TeamsDoughnut
                :chart-data="allTasksInTeamsDataCollection"
                :options="options"
                :height="200"
                v-if="!noTeamsStatistics"
              ></TeamsDoughnut>
              <v-layout justify-content align-center fill-height v-else>
                <v-flex>
                  <p class="text-center">Нет команд</p>
                </v-flex>
              </v-layout>
            </v-card>
          </v-col>
          <v-col cols="12" xs="12" sm="6" md="6" lg="4">
            <v-card class="pa-2" height="100%">
              <h5 class="text-center">
                Текущее количество команд <br />
                по всему проекту
              </h5>
              <v-layout justify-content align-center fill-height>
                <v-flex>
                  <p
                    class="display-1 text-center"
                    style="
                      font-size: 6rem !important;
                      font-weight: bold;
                      line-height: 6rem;
                    "
                  >
                    {{ statistics == undefined ? "-" : statistics.teamsCount }}
                  </p>
                </v-flex>
              </v-layout>
            </v-card>
          </v-col>
          <v-col cols="12" xs="12" sm="6" md="6" lg="4">
            <v-card class="pa-2" height="100%">
              <h5 class="text-center">
                Среднее количество статусов<br />
                по всем доскам в командах
              </h5>
              <v-layout justify-content align-center fill-height>
                <v-flex>
                  <p
                    class="display-1 text-center"
                    style="
                      font-size: 6rem !important;
                      font-weight: bold;
                      line-height: 6rem;
                    "
                  >
                    {{
                      statistics == undefined
                        ? "-"
                        : Math.ceil(statistics.statusAverage * 100) / 100
                    }}
                  </p>
                </v-flex>
              </v-layout>
            </v-card>
          </v-col>
          <v-col cols="12" xs="12" sm="6" md="6" lg="4">
            <v-card class="pa-2" height="100%">
              <h5 class="text-center">
                Данные о количестве досок<br />
                по всем командам
              </h5>
              <TeamsDoughnut
                :chart-data="allBoardsInTeamsDataCollection"
                :options="options"
                :height="200"
                v-if="!noBoardsStatistics"
              ></TeamsDoughnut>
              <v-layout justify-content align-center fill-height v-else>
                <v-flex>
                  <p class="text-center">Досок нет</p>
                </v-flex>
              </v-layout>
            </v-card>
          </v-col>
          <v-col cols="12" xs="12" sm="6" md="6" lg="4">
            <v-card class="pa-2" height="100%">
              <h5 class="text-center">
                Данные о количестве спринтов<br />
                по всему проекту
              </h5>
              <v-layout justify-content align-center fill-height>
                <v-flex>
                  <p
                    class="display-1 text-center"
                    style="
                      font-size: 6rem !important;
                      font-weight: bold;
                      line-height: 6rem;
                    "
                  >
                    {{
                      statistics == undefined ? "-" : statistics.sprintsCount
                    }}
                  </p>
                </v-flex>
              </v-layout>
            </v-card>
          </v-col>
          <v-col cols="12" xs="12" sm="6" md="6" lg="4">
            <v-card class="pa-2 d-print-none" height="100%">
              <h5 class="text-center">Действия</h5>
              <v-layout justify-content align-center fill-height>
                <v-flex class="text-center">
                  <v-btn dark class="mb-2" color="black" :to="'/projects'"
                    >Вернуться к списку</v-btn
                  ><br />
                  <v-btn dark class="mb-2" color="error" @click="deleteProject"
                    >Удалить проект</v-btn
                  >
                </v-flex>
              </v-layout>
            </v-card>
          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import TeamsDoughnut from "@/components/main/projects/charts/TeamsDoughnut.vue";
import { STATISTICS, DELETE_PROJECT } from "@/graphql/queries.js";

export default {
  name: "ProjectsDashboard",
  apollo: {
    statistics: {
      query: STATISTICS,
      variables() {
        return {
          projectId: this.projectId
        };
      }
    }
  },
  data() {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  components: {
    TeamsDoughnut
  },
  computed: {
    noTeamsStatistics() {
      if (this.allTasksInTeamsDataCollection != undefined) {
        if (this.allTasksInTeamsDataCollection.datasets != undefined) {
          if (this.allTasksInTeamsDataCollection.datasets.length !== 0) {
            return (
              this.allTasksInTeamsDataCollection.datasets[0].data.length == 0
            );
          } else {
            return false;
          }
        } else {
          return false;
        }
      } else {
        return false;
      }
    },
    noBoardsStatistics() {
      if (this.allBoardsInTeamsDataCollection != undefined) {
        if (this.allBoardsInTeamsDataCollection.datasets != undefined) {
          if (this.allBoardsInTeamsDataCollection.datasets.length !== 0) {
            return (
              this.allBoardsInTeamsDataCollection.datasets[0].data.length == 0
            );
          } else {
            return false;
          }
        } else {
          return false;
        }
      } else {
        return false;
      }
    },
    projectId() {
      return this.$route.params.id;
    },
    allTasksInTeamsDataCollection() {
      let dataCollection = {
        labels: [],
        datasets: [
          {
            label: "Dataset",
            backgroundColor: "#f87979",
            data: []
          }
        ]
      };
      if (!this.$apollo.queries.statistics.loading && this.statistics != null) {
        for (let index = 0; index < this.statistics.teams.length; index++) {
          const team = this.statistics.teams[index];
          let allTasksOfTeam = 0;
          for (let index = 0; index < team.boardSet.length; index++) {
            const board = team.boardSet[index];
            allTasksOfTeam += board.tasksCount;
          }
          dataCollection.labels.push(`Задачи команды "${team.name}"`);
          dataCollection.datasets[0].data.push(allTasksOfTeam);
        }
      }
      return dataCollection;
    },
    allBoardsInTeamsDataCollection() {
      let dataCollection = {
        labels: [],
        datasets: [
          {
            label: "Dataset",
            backgroundColor: "#f87979",
            data: []
          }
        ]
      };
      if (!this.$apollo.queries.statistics.loading && this.statistics != null) {
        for (let index = 0; index < this.statistics.teams.length; index++) {
          const team = this.statistics.teams[index];
          dataCollection.labels.push(`Доски команды "${team.name}"`);
          dataCollection.datasets[0].data.push(team.boardsCount);
        }
      }
      return dataCollection;
    }
  },
  methods: {
    deleteProject() {
      this.$apollo
        .mutate({
          mutation: DELETE_PROJECT,
          variables: {
            projectId: this.projectId
          }
        })
        .then(() => {
          this.$router.push("/projects");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.chartjs-render-monitor {
  max-height: 30vh;
  height: 30vh;
}
.v-card__title {
  display: unset;
}
@media print {
  body {
    font-size: 28px;
  }
  @page {
    margin: 1cm;
  }
  // .v-sheet.v-card:not(.v-sheet--outlined) {
  //   box-shadow: unset !important;

  //   page-break-before: always;
  // }
  .col-12 {
    width: 50% !important;
    flex: unset !important;
  }
  .v-row {
    display: flex;
  }
  *,
  *:before,
  *:after,
  *:first-letter,
  p:first-line,
  div:first-line,
  blockquote:first-line,
  li:first-line {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  h1 {
    margin-bottom: 4rem;
    text-align: center !important;
  }
  h1:before {
    content: url(https://chart.googleapis.com/chart?cht=qr&chs=150x150&chl=http://localhost:8000/projects&choe=UTF-8);
    position: absolute;
    right: 0;
    bottom: 0;
  }
  .row + .row {
    margin-top: 60px;
  }
}
</style>
