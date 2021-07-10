<template>
  <v-container fluid height="100%">
    <v-row align="center" justify="center" v-if="loading">
      <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </v-row>
    <v-row v-else>
      <div id="status-list">
        <AddStatusDialog
          :dialog="addStatusDialog"
          @close="addStatusDialog = false"
          @data-refresh="refreshData"
        ></AddStatusDialog>
        <AddTaskDialog
          @close="closeTaskDialog"
          @refresh="refreshData"
          :dialog="addTaskDialog"
          :story-point-estimate="storyPointEstimate"
          :status-set="board.statusSet"
          :employees="board.team.participants"
          :sprints="board.team.project.sprintSet"
          :new-status-id="addTaskStatusId"
          :editTaskObj="editTaskObj"
          ref="taskDialog"
        ></AddTaskDialog>
        <v-card
          class="mr-4 status-column"
          :class="{ 'ml-4': index == 0 }"
          min-width="400"
          max-width="400"
          tile
          v-for="(status, index) in modernizedStatusSet"
          :key="status.id"
          flat
        >
          <v-banner color="white" sticky class="mb-4">
            <v-container>
              <v-row>
                {{ status.name }} <v-spacer></v-spacer>
                <v-btn
                  color="black"
                  icon
                  v-if="status.id !== 0 && isManagerOrAdmin"
                  @click="deleteStatus(status.id)"
                  ><v-icon>mdi-close</v-icon>
                </v-btn>
              </v-row>
            </v-container>
            <div>
              <v-btn
                rounded
                text
                block
                class="mt-2"
                :class="{ 'mt-5': status.id == 0 && isManagerOrAdmin }"
                @click="addTask(status.id)"
              >
                Добавить задачу</v-btn
              >
            </div>
          </v-banner>
          <draggable
            :list="status.tasks"
            draggable=".task"
            v-bind="dragOptions"
            :empty-insert-threshold="100"
            @end="endUpdateStatus($event)"
            @move="changeUpdateStatus($event)"
            :data-status_id="status.id"
          >
            <transition-group type="transition" name="flip-list">
              <Task
                v-for="task in specificTasksSet(status.id)"
                :key="task.id"
                :task="task"
                class="task"
                @updateStoryPoints="refreshData"
                @editTask="startEditTask($event)"
                :data-task_id="task.id"
                :story-point-estimate="storyPointEstimate"
                :prefix="board.team.project.prefix"
              ></Task>
            </transition-group>
          </draggable>
        </v-card>
        <v-card
          class="mr-4 status-column"
          min-width="400"
          max-width="400"
          tile
          flat
          v-if="isManagerOrAdmin"
        >
          <v-banner color="white" sticky class="mb-4 pt-2">
            <!-- Новый статус задач -->
            <v-btn
              rounded
              outlined
              block
              class="mt-5"
              @click="openAddStatusDialog"
            >
              Добавить новый статус
            </v-btn>
          </v-banner>
        </v-card>
      </div>
    </v-row>
  </v-container>
</template>

<script>
import {
  BOARD_BY_ID,
  UPDATE_STATUS,
  DELETE_STATUS
} from "@/graphql/queries.js";
import Task from "@/components/main/boards/Task.vue";
import AddTaskDialog from "@/components/main/boards/AddTaskDialog.vue";
import AddStatusDialog from "@/components/main/boards/AddStatusDialog.vue";
import draggable from "vuedraggable";

export default {
  name: "Desk",
  apollo: {
    board: {
      query: BOARD_BY_ID,
      variables: function () {
        return {
          boardId: this.routeId
        };
      }
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.$apollo.queries.board.refetch({
      boardId: to.params.id
    });
    next();
  },
  components: {
    Task,
    AddTaskDialog,
    AddStatusDialog,
    draggable
  },
  data() {
    return {
      editTaskObj: null,
      addTaskStatusId: null,
      routeId: this.$route.params.id,
      addTaskDialog: false,
      addStatusDialog: false,
      storyPointEstimate: [
        {
          number: 0,
          color: "grey"
        },
        {
          number: 1,
          color: "blue"
        },
        {
          number: 2,
          color: "green"
        },
        {
          number: 3,
          color: "yellow"
        },
        {
          number: 5,
          color: "orange"
        },
        {
          number: 8,
          color: "red"
        },
        {
          number: 13,
          color: "pink"
        }
      ]
    };
  },
  computed: {
    isManagerOrAdmin() {
      return this.$store.getters.isManager || this.$store.getters.isAdmin;
    },
    dragOptions() {
      return {
        animation: 0,
        group: "tasks",
        disabled: false,
        ghostClass: "ghost"
      };
    },
    loading() {
      return this.$apollo.queries.board.loading;
    },
    modernizedStatusSet() {
      let newStatusSet = [];
      newStatusSet.push({
        id: 0,
        name: "Без статуса"
      });
      if (this.board != undefined) {
        if (this.board.statusSet != undefined) {
          this.board.statusSet.forEach((el) => {
            newStatusSet.push(el);
          });
        }
      }
      return newStatusSet;
    }
  },
  methods: {
    closeTaskDialog() {
      this.editTaskId = null;
      this.addTaskDialog = false;
    },
    startEditTask(taskId) {
      let taskObj = this.board.taskSet.find((el) => el.id === taskId);
      this.editTaskObj = taskObj;
      this.$refs.taskDialog.setValues(taskObj);
      this.addTaskDialog = true;
    },
    deleteStatus(statusId) {
      this.$apollo
        .mutate({
          mutation: DELETE_STATUS,
          variables: {
            statusId
          }
        })
        .then(() => {
          this.refreshData();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addTask(statusId) {
      this.editTaskId = null;
      this.$refs.taskDialog.setStatusValue(statusId);
      this.addTaskStatusId = statusId;
      this.addTaskDialog = true;
    },
    specificTasksSet(statusId) {
      if (this.board != null) {
        return this.board.taskSet.filter((el) => {
          if (el.status != null) {
            return el.status.id == statusId;
          } else {
            return statusId == 0;
          }
        });
      } else {
        return [];
      }
    },
    endUpdateStatus(event) {
      this.$apollo.mutate({
        mutation: UPDATE_STATUS,
        variables: {
          taskId: event.item.dataset.task_id,
          statusId: event.to.parentNode.dataset.status_id
        }
      });
    },
    openAddStatusDialog() {
      this.addStatusDialog = true;
    },
    refreshData() {
      this.$apollo.queries.board.refresh();
      this.$apollo.queries.board.refetch();
    }
  },
  mounted() {
    this.$emit("openMenu");
  }
};
</script>

<style lang="scss" scoped>
$columnHeight: calc(100vh - 64px - 50px);

html {
  overflow-y: auto;
}

#status-list {
  display: flex;
  flex-direction: row;
  overflow-x: auto;
  overflow-y: auto;
  height: $columnHeight;
  max-height: $columnHeight;
  & .status-column {
    height: 100%;
    max-height: 100%;
    overflow-y: auto;
  }
}

.flip-list-move {
  transition: transform 0.5s;
}

.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
</style>
