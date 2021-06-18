<template>
  <div id="status-list">
    <TaskDialog :dialog="addTaskDialog"></TaskDialog>
    <v-card
      class="mr-4 status-column"
      :class="{ 'ml-4': index == 0 }"
      min-width="400"
      max-width="400"
      tile
      v-for="(status, index) in statusList"
      :key="status.id"
      flat
    >
      <v-banner color="white" sticky>
        {{ status.title }}
        <div>
          <v-btn rounded text block class="mt-2" @click="addTask(status.id)">
            Добавить задачу</v-btn
          >
        </div>
      </v-banner>

      <draggable
        :list="status.tasks"
        draggable=".task"
        v-bind="dragOptions"
        :empty-insert-threshold="100"
      >
        <transition-group type="transition" name="flip-list">
          <Task
            v-for="(task, index) in status.tasks"
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
</template>

<script>
import Task from "@/components/main/boards/Task.vue";
import TaskDialog from "@/components/main/boards/TaskDialog.vue";
import draggable from "vuedraggable";

export default {
  name: "Desk",
  props: ["statusList"],
  components: {
    Task,
    TaskDialog,
    draggable
  },
  data() {
    return {
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
    }
  },
  methods: {
    addTask(statusId) {
      console.log(statusId);
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
