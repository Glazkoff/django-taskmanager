<template>
  <v-card class="mb-4 h-100 ml-2 mr-2" shaped outlined elevation="2">
    <v-list-item two-line>
      <v-list-item-content>
        <v-container fluid>
          <v-row>
            <div class="text-overline">PJ1-213</div>
            <v-spacer></v-spacer>
            <v-chip class="" color="green" text-color="white">
              <v-avatar left class="green darken-4"> 1 </v-avatar>
              SP
            </v-chip>
          </v-row>
        </v-container>
        <v-list-item-subtitle>Спринт #1</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>Купить коту еды</v-list-item-title>
        <!-- <v-list-item-subtitle>
          Secondary line text Lorem ipsum dolor sit amet,
        </v-list-item-subtitle> -->
      </v-list-item-content>
    </v-list-item>
    <v-card-actions>
      <v-btn rounded text>Подробнее</v-btn>
      <v-spacer></v-spacer>
      <v-btn outlined rounded text>Button</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Task"
};
</script>

<style lang="scss" scoped></style>
