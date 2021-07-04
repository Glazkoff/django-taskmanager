<template>
  <v-container>
    <h1>Дашборд проекта #{{ projectId }}</h1>
    <div>ProjectsDashboard</div>
  </v-container>
</template>

<script>
export default {
  name: "ProjectsDashboard",
  computed: {
    projectId() {
      return this.$route.params.id;
    }
  }
};
</script>

<style lang="scss" scoped></style>
