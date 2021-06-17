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
      <v-card
        v-for="(t, index) in 4"
        :key="t"
        class="mb-4 h-100"
        :class="{ 'mt-4': index == 0 }"
        shaped
        outlined
        elevation="2"
      >
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Single-line item</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Two-line item</v-list-item-title>
            <v-list-item-subtitle>Secondary text</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item three-line>
          <v-list-item-content>
            <v-list-item-title>Three-line item</v-list-item-title>
            <v-list-item-subtitle>
              Secondary line text Lorem ipsum dolor sit amet,
            </v-list-item-subtitle>
            <v-list-item-subtitle>
              consectetur adipiscing elit.
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Desk",
  props: ["statusList"]
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
