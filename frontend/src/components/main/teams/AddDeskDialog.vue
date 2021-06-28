<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить новую доску </v-card-title>
      <v-card-text>
        <v-text-field
          label="Название доски"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="desk.name"
          outlined
        ></v-text-field>
        <v-select
          v-model="desk.team"
          :items="teams"
          item-text="name"
          item-value="id"
          label="Команда"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        ></v-select>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="primary" text @click="onCancel">Отменить</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="onSave">Сохранить</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { TEAMS_LIST, CREATE_BOARD } from "@/graphql/queries.js";
export default {
  name: "AddDeskDialog",
  props: ["dialog"],
  data() {
    return {
      desk: {
        name: null,
        team: null
      }
    };
  },
  apollo: {
    teams: {
      query: TEAMS_LIST
    }
  },
  methods: {
    setTeamValue(teamValue) {
      this.desk.team = teamValue;
    },
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      this.$apollo
        .mutate({
          mutation: CREATE_BOARD,
          variables: {
            name: this.desk.name,
            teamId: this.desk.team
          }
        })
        .then(() => {
          this.$emit("refresh");
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
