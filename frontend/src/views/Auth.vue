<template>
  <div>
    <p>Auth {{ this.$apollo.queries.boards.loading }} {{ boards }}</p>
    <router-view></router-view>
  </div>
</template>

<script>
import { BOARDS } from "@/graphql/queries.js";

export default {
  name: "Auth",
  apollo: {
    boards: {
      query: BOARDS
    }
  }
};
</script>

<style lang="scss" scoped></style>
