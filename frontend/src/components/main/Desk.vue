<template>
  <div id="status-list">
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
      <v-banner color="white" sticky>{{ status.title }}</v-banner>
      <draggable :list="status.tasks" draggable=".task" v-bind="dragOptions">
        <transition-group type="transition" name="flip-list">
          <Task
            v-for="(task, index) in status.tasks"
            :key="task.id"
            :task="task"
            :class="{ 'mt-4': index == 0 }"
            class="task"
          ></Task>
        </transition-group>
      </draggable>
    </v-card>
  </div>
</template>

<script>
import Task from "@/components/main/Task.vue";
import draggable from "vuedraggable";

export default {
  name: "Desk",
  props: ["statusList"],
  components: {
    Task,
    draggable
  },
  data() {
    return {
      tasks: [
        {
          id: 1,
          storyPoints: 1,
          body: "Купить коту еды",
          executor: 2,
          sprint: 1,
          status: 1,
          comments: []
        },
        {
          id: 2,
          storyPoints: 1,
          body: "Купить коту еды",
          executor: 2,
          sprint: 1,
          status: 1,
          comments: []
        },
        {
          id: 3,
          storyPoints: 1,
          body: "Купить коту еды",
          executor: 2,
          sprint: 1,
          status: 1,
          comments: []
        },
        {
          id: 4,
          storyPoints: 1,
          body: "Купить коту еды",
          executor: 2,
          sprint: 1,
          status: 1,
          comments: []
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
