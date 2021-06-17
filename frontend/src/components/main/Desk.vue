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
      <Task
        v-for="(t, index) in 4"
        :key="t"
        :class="{ 'mt-4': index == 0 }"
      ></Task>
    </v-card>
  </div>
</template>

<script>
import Task from "@/components/main/Task.vue";

export default {
  name: "Desk",
  props: ["statusList"],
  components: {
    Task
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
</style>
