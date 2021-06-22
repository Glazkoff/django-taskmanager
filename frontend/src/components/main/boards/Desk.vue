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
          :dialog="addTaskDialog"
          @close="addTaskDialog = false"
          :story-point-estimate="storyPointEstimate"
          :status-set="board.statusSet"
          :employees="board.team.participants"
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
            {{ status.name }}
            <div>
              <v-btn
                rounded
                text
                block
                class="mt-2"
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
import { BOARD_BY_ID, UPDATE_STATUS } from "@/graphql/queries.js";
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
  components: {
    Task,
    AddTaskDialog,
    AddStatusDialog,
    draggable
  },
  data() {
    return {
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
    addTask(statusId) {
      console.log(statusId);
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
