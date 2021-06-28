<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить новый проект </v-card-title>
      <v-card-text>
        <v-text-field
          label="Название проекта"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="project.name"
          outlined
        ></v-text-field>
        <v-text-field
          label="Префикс задач"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="project.prefix"
          outlined
        ></v-text-field>
        <v-select
          v-model="project.leader"
          :items="users"
          item-value="id"
          label="Лидер"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.firstName }} {{ item.lastName }} ({{ item.username }})
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.firstName }} {{ item.lastName }} ({{ item.username }})
          </template>
        </v-select>
        <v-select
          v-model="project.teams"
          :items="teams"
          item-value="id"
          label="Команды"
          outlined
          multiple
          chips
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.name }} ({{ item.id }})
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.name }} ({{ item.id }})
          </template>
        </v-select>
        <!-- <v-text-field
          label="Ограничение количества участников"
          v-model="project.settings.teamCount"
          outlined
        ></v-text-field>
        <v-text-field
          label="Ограничение длительности спринта участников"
          v-model="project.settings.sprintCount"
          outlined
        ></v-text-field> -->
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
import { USERS, TEAMS_LIST, CREATE_PROJECT } from "@/graphql/queries.js";

export default {
  name: "AddProjectDialog",
  props: ["dialog"],
  apollo: {
    users: {
      query: USERS
    },
    teams: {
      query: TEAMS_LIST
    }
  },
  data() {
    return {
      project: {
        name: null,
        leader: null,
        prefix: null,
        settings: {
          teamCount: null,
          sprintCount: null
        },
        teams: []
      }
    };
  },
  methods: {
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      this.$apollo
        .mutate({
          mutation: CREATE_PROJECT,
          variables: {
            name: this.project.name,
            leaderId: this.project.leader,
            prefix: this.project.prefix,
            teams: this.project.teams
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
