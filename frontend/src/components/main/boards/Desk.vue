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
            @start="startUpdateStatus($event)"
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
                @updateStoryPoints="$apollo.queries.board.refresh()"
                :data-task_id="task.id"
              ></Task>
            </transition-group>
          </draggable>
        </v-card>
      </div>
    </v-row>
  </v-container>
</template>

<script>
import { BOARD_BY_ID, UPDATE_STATUS } from "@/graphql/queries.js";
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
    startUpdateStatus(event) {
      console.log(
        "START: ",
        event.item.dataset.task_id,
        event.from.parentNode.dataset.status_id
      );
    },
    endUpdateStatus(event) {
      console.log(
        "END: ",
        event.item.dataset.task_id,
        event.to.parentNode.dataset.status_id
      );
      this.$apollo.mutate({
        mutation: UPDATE_STATUS,
        variables: {
          taskId: event.item.dataset.task_id,
          statusId: event.to.parentNode.dataset.status_id
        }
      });
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
