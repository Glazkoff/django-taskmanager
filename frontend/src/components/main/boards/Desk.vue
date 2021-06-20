<template>
  <v-container fluid height="100%">
    <v-row align="center" justify="center" v-if="loading">
      <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </v-row>
    <v-row v-else>
      <div id="status-list">
        <TaskDialog :dialog="addTaskDialog"></TaskDialog>
        <v-card
          class="mr-4 status-column"
          :class="{ 'ml-4': index == 0 }"
          min-width="400"
          max-width="400"
          tile
          v-for="(status, index) in statusSet"
          :key="status.id"
          flat
        >
          {{ specificTasksSet(1) }}
          <v-banner color="white" sticky>
            {{ status.title }}
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
            @end="onCardDrop($event)"
          >
            <transition-group type="transition" name="flip-list">
              <Task
                v-for="(task, index) in specificTasksSet(status.id)"
                :key="task.id"
                :task="task"
                :class="{ 'mt-4': index == 0 }"
                class="task"
                @updateStoryPoints="$emit('updateStoryPoints', $event)"
              ></Task>
            </transition-group>
          </draggable>
        </v-card>
      </div>
    </v-row>
  </v-container>
</template>

<script>
import { BOARD_BY_ID } from "@/graphql/queries.js";
import Task from "@/components/main/boards/Task.vue";
import TaskDialog from "@/components/main/boards/TaskDialog.vue";
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
  mounted() {
    console.log(this.routeId, this.board);
  },
  components: {
    Task,
    TaskDialog,
    draggable
  },
  data() {
    return {
      routeId: this.$route.params.id,
      addTaskDialog: false
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
    statusSet() {
      let taskListsArr = [];
      taskListsArr.push({
        id: 0,
        name: "Без статуса",
        tasks: []
      });
      if (this.board != null) {
        this.board.statusSet.forEach((el) => {
          let obj = {
            id: el.id,
            name: el.name,
            tasks: []
          };
          taskListsArr.push(obj);
        });
        this.board.taskSet.forEach((task) => {
          if (task.status != null) {
            taskListsArr.forEach((statusObj) => {
              if (statusObj.id == task.status.id) {
                statusObj.tasks.push(task);
              }
            });
          } else {
            taskListsArr[0].tasks.push(task);
          }

          //   let taskListObj = taskListsArr.find((status) => {
          //     status.id == task.status.id;
          //   });
          //   if (taskListObj != undefined) {
          //     taskListObj.tasks.push(task);
          //   } else {
          //     console.log("АЛЯРМА!", task.status.id);
          //   }
        });
      }
      return taskListsArr;
    }
  },
  methods: {
    onCardDrop(event) {
      console.log("!!!", event.added.element.id);
    },
    addTask(statusId) {
      console.log(statusId);
    },
    specificTasksSet(statusId) {
      if (this.board != null) {
        return this.board.taskSet.filter((el) => {
          if (el.status != null) {
            return el.status.id == statusId;
          } else {
            console.log(statusId);
            return statusId == 0;
          }
        });
      } else {
        return [];
      }
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
