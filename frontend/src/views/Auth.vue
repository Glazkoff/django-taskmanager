<template>
  <div>Auth {{ this.$apollo.queries.boards.loading }} {{ boards }}</div>
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
