<template>
  <v-card class="mb-4 h-100 ml-2 mr-2" shaped outlined elevation="2">
    <v-list-item two-line>
      <v-list-item-content>
        <v-container fluid>
          <v-row>
            <div class="text-overline">{{ prefix }}{{ task.id }}</div>
            <v-spacer></v-spacer>
            <v-menu
              v-model="storyPointMenu"
              bottom
              left
              transition="scale-transition"
              origin="top right"
            >
              <template v-slot:activator="{ on }">
                <v-chip
                  v-on="on"
                  class="darken-2"
                  :color="colorClassSP(task.storyPoints)"
                  text-color="white"
                >
                  <v-avatar
                    left
                    class="darken-4"
                    :class="colorClassSP(task.storyPoints)"
                  >
                    {{ task.storyPoints != 0 ? task.storyPoints : "-" }}
                  </v-avatar>
                  SP
                </v-chip>
              </template>
              <v-card width="300">
                <v-list
                  class="darken-2"
                  :color="colorClassSP(task.storyPoints)"
                  dark
                >
                  <v-list-item>
                    <v-list-item-avatar
                      class="darken-4"
                      :class="colorClassSP(task.storyPoints)"
                    >
                      {{ task.storyPoints }}
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title>STORY POINT(S)</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-btn icon @click="storyPointMenu = false">
                        <v-icon>mdi-close-circle</v-icon>
                      </v-btn>
                    </v-list-item-action>
                  </v-list-item>
                </v-list>
                <v-list>
                  <v-list-item
                    v-for="(sp, index) in storyPointEstimate"
                    :key="index"
                    @click="updateStoryPoints(sp.number)"
                  >
                    <v-list-item-action>
                      <v-avatar
                        size="30"
                        left
                        dark
                        :class="sp.color"
                        class="darken-4 white--text"
                      >
                        {{ sp.number }}
                      </v-avatar>
                    </v-list-item-action>
                    <v-list-item-subtitle
                      >Установить {{ sp.number }} SP</v-list-item-subtitle
                    >
                  </v-list-item>
                </v-list>
              </v-card>
            </v-menu>
          </v-row>
        </v-container>
        <v-list-item-subtitle>{{
          task.sprint != null ? `Спринт "${task.sprint.name}"` : "Без спринта"
        }}</v-list-item-subtitle>
        <v-list-item-subtitle>{{
          task.executor != null
            ? `Исполнитель: ${task.executor.lastName} ${task.executor.firstName}`
            : "Без исоплнителя"
        }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>{{ task.body }}</v-list-item-title>
        <!-- <v-list-item-subtitle>
          Secondary line text Lorem ipsum dolor sit amet,
        </v-list-item-subtitle> -->
      </v-list-item-content>
    </v-list-item>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn rounded text @click="onTaskEditStart">Редактировать</v-btn>
      <!-- <v-btn outlined rounded text>Button</v-btn> -->
    </v-card-actions>
  </v-card>
</template>

<script>
import { UPDATE_SP } from "@/graphql/queries.js";

export default {
  name: "Task",
  props: ["task", "storyPointEstimate", "prefix"],
  data() {
    return {
      storyPointMenu: false
    };
  },
  methods: {
    updateStoryPoints(newStoryPoints) {
      let newSp = newStoryPoints;
      if (newSp == "-") newSp = 0;
      this.$apollo.mutate({
        mutation: UPDATE_SP,
        variables: {
          taskId: this.task.id,
          storyPoints: newSp
        }
      });
      this.$emit("updateStoryPoints", {
        taskId: this.task.id,
        storyPoints: newStoryPoints
      });
    },
    colorClassSP(number) {
      let objSP = this.storyPointEstimate.find((el) => {
        return el.number == number;
      });
      if (objSP != undefined) {
        return objSP.color;
      } else {
        return "";
      }
    },
    onTaskEditStart() {
      this.$emit("editTask", this.task.id);
    }
  }
};
</script>

<style lang="scss" scoped></style>
